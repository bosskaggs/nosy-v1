# Architecture Overview

Nosy v1 is a simple polling daemon that monitors Tailscale device presence.

It works by calling:

    tailscale status --json

This returns a JSON structure containing all peers, their online state,
their IPs, and metadata.

Nosy v1 compares the current state to the previous state stored in:

    /opt/nosyneighbour/tailscale_state.json

Any changes trigger a call to:

    /opt/nosyneighbour/notify.sh

This script is user-defined and typically sends a Pushover alert.

The watcher runs indefinitely under systemd.
