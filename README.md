# Nosy v2  
A lightweight Python tool for detecting new devices on your LAN and sending instant alerts via Pushover.

Nosy watches your network for new or unexpected devices.  
It’s simple, fast, and reliable — no agents, no daemons, no cloud accounts, no subscriptions.

Originally built to monitor a Tailscale fleet, Nosy works with **any** device on your network.

---

## 🚀 Features
- Detects new devices via ARP scanning  
- Sends instant alerts via Pushover  
- Tracks first‑seen timestamps  
- Optional device name overrides  
- Runs manually or as a systemd service  
- Works on VMs, Raspberry Pi, or bare metal  
- Zero external dependencies beyond Python + scapy  

---

## 📦 Minimum Requirements
- Python 3.8+  
- pip3  
- scapy  
- requests  
- A network interface (wired or WiFi)

---

## 🧪 Tested On
- Ubuntu Server (Proxmox VM)  
- Debian 12  
- Raspberry Pi OS  
- Windows 10/11 (WSL)  
- Tailscale networks  
- Standard home LANs  

---

## 🔔 Why Pushover?
Pushover is used because it is:

- Fast  
- Reliable  
- Cross‑platform  
- Works even when your phone is on silent  
- Has a simple API  
- Doesn’t require phone numbers or email  

### But Pushover is optional  
Nosy’s notification system is modular.  
You can replace it with:

- Discord  
- Slack  
- Telegram  
- Email  
- SMS  
- Webhooks  
- Home Assistant  
- Anything with an API  

Modify the `notify()` function in `nosy.py`.

---

## 🛠 Installation

### Install dependencies
```bash
sudo apt update
sudo apt install -y python3 python3-pip
pip install scapy requests
sudo pip3 install scapy requests
#Running Manually sudo python3 nosy.py
#Running as a systemd Service #sudo mkdir -p /opt/nosy
#sudo cp * /opt/nosy/
#sudo chown -R "user":"user" /opt/nosy
