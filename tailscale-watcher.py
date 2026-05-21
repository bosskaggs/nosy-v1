#!/usr/bin/env python3
import subprocess
import json
import time
import os
from datetime import datetime

NOTIFY_SCRIPT = "/opt/nosyneighbour/notify.sh"
STATE_FILE = "/opt/nosyneighbour/tailscale_state.json"
POLL_INTERVAL = 30  # seconds

def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{result.stderr}")
    return result.stdout

def load_state():
    if not os.path.exists(STATE_FILE):
        return {}
    with open(STATE_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def notify(message):
    subprocess.run([NOTIFY_SCRIPT, message])

def get_tailscale_status():
    out = run(["tailscale", "status", "--json"])
    data = json.loads(out)
    nodes = {}
    for peer in data.get("Peer", {}).values():
        name = peer.get("HostName") or peer.get("DNSName") or peer.get("TailscaleIPs", ["unknown"])[0]
        online = not peer.get("Online", False) is False  # Online is bool
        nodes[name] = {
            "online": online,
            "ips": peer.get("TailscaleIPs", []),
        }
    # Include self node
    self_node = data.get("Self", {})
    self_name = self_node.get("HostName") or self_node.get("DNSName") or "self"
    nodes[self_name] = {
        "online": True,
        "ips": self_node.get("TailscaleIPs", []),
    }
    return nodes

def main():
    state = load_state()
    notify("Tailscale watcher started on nosyneigbour")

    while True:
        try:
            current = get_tailscale_status()
        except Exception as e:
            notify(f"Tailscale watcher error: {e}")
            time.sleep(POLL_INTERVAL)
            continue

        # Detect changes
        for name, info in current.items():
            was = state.get(name, {}).get("online")
            now = info["online"]
            if was is None:
                # First time seeing this node
                msg = f"[TS] Discovered node: {name} ({', '.join(info['ips'])})"
                notify(msg)
            elif was is False and now is True:
                msg = f"[TS] Node ONLINE: {name} ({', '.join(info['ips'])})"
                notify(msg)
            elif was is True and now is False:
                msg = f"[TS] Node OFFLINE: {name}"
                notify(msg)

        # Detect nodes that disappeared entirely
        for name in list(state.keys()):
            if name not in current:
                notify(f"[TS] Node REMOVED from tailnet: {name}")
                state.pop(name, None)

        # Update state
        new_state = {}
        for name, info in current.items():
            new_state[name] = {"online": info["online"], "ips": info["ips"]}
        state = new_state
        save_state(state)

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()
