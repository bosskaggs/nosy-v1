# How It Works

1. On startup, Nosy loads the previous state from disk.
2. It sends a "watcher started" notification.
3. Every 30 seconds, it polls Tailscale for the current state.
4. It compares the new state to the old state.
5. It detects:
   - New nodes
   - Nodes going online
   - Nodes going offline
   - Nodes removed from the tailnet
6. For each event, it calls notify.sh with a message.
7. It writes the new state back to disk.
8. Loop forever.
