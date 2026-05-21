# Nosy v1 — Tailscale Presence Watcher

Nosy v1 is a lightweight daemon that monitors your Tailscale network and sends
Pushover notifications when devices appear, disappear, or change state.

It runs as a systemd service and polls `tailscale status --json` every 30 seconds.

---

## Features

- Detects when a Tailscale node comes online
- Detects when a node goes offline
- Detects new nodes joining the tailnet
- Detects nodes removed from the tailnet
- Sends alerts via a simple `notify.sh` script (Pushover by default)
- Persists state to `/opt/nosyneighbour/tailscale_state.json`
- Runs as a systemd service for reliability

---

## Installation

### 1. Copy files

sudo cp tailscale-watcher.py /usr/local/bin/
sudo chmod +x /usr/local/bin/tailscale-watcher.py


### 2. Create the working directory

sudo mkdir -p /opt/nosyneighbour
sudo cp opt/tailscale_state.json.example /opt/nosyneighbour/tailscale_state.json


### 3. Configure notifications

Copy the example:

udo cp notify.sh.example /opt/nosyneighbour/notify.sh
sudo chmod +x /opt/nosyneighbour/notify.sh


Edit it and insert your Pushover token + user key.

---

## Systemd Service

Install the service:

sudo cp tailscale-watcher.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable tailscale-watcher
sudo systemctl start tailscale-watcher

Check status:


---

## Logs


---

## Directory Layout

/usr/local/bin/tailscale-watcher.py
/opt/nosyneighbour/notify.sh
/opt/nosyneighbour/tailscale_state.json
/etc/systemd/system/tailscale-watcher.service


---

## Requirements

- Python 3
- Tailscale installed and authenticated
- Pushover account (or modify notify.sh for another service)

---

## License

MIT (or whatever you prefer)
