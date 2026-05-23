<img src="https://github.com/user-attachments/assets/b3d15fbd-3086-4911-b2ff-113a3483d96e" width="250" alt="Lucky_Logo" valign="left" />

<img src="https://github.com/user-attachments/assets/63e3de5e-a7f2-4eb6-b3e2-8bebc9a30c07" width="120" alt="Lucky" valign="middle" />


A community-driven, decentralized high-availability backup proxy network. By routing production traffic through the Lucky cluster, developers can safeguard their applications against server failures and unexpected dropouts.

---

## How the Infrastructure Works

Lucky acts as a reverse proxy shield sitting between your users and your real infrastructure node. 

1. **Traffic Entry:** Visitors connect to your domain, which handles a fallback route directly to our central cluster nodes.
2. **Proxy Pass:** If your server is running safely, Lucky transparently pulls the content from your primary IP and hands it to the browser.
3. **Failover Execution:** If your primary node stops responding, Lucky intercepts the drop within 4 seconds and serves a clean, unified backup screen to prevent a 404 or a browser "Server Not Found" crash window.

---

## Architecture Lifecycle Blueprint

[ Visitor Browser ] ➔ Requests Your Domain ➔ [ Lucky Master Proxy Node ]
                                                        │
                                          ┌─────────────┴─────────────┐
                                          ▼                           ▼
                           [ Your Primary Host Server ]    [ Lucky Backup Engine ]
                              (🟢 Target Responsive)         (🔴 Target Crashed)
                                       │                              │
                            Serves Live App Content       Serves Failover Screen

---

## Step-by-Step Configuration Guide

To secure your server under the Lucky cluster network, follow these configuration phases carefully.

### Phase A: Submit Your Server Coordinates (GitHub PR)

1. **Fork** this repository to your personal GitHub profile by clicking the **Fork** button at the top right of this page.
2. Navigate into the **`nodes/`** directory within your personal fork.
3. Tap **Add file** ➔ **Create new file**.
4. Name the file exactly after your custom root domain path plus a `.json` property extension (e.g., `nodes/mycoolapp.com.json`).
5. Paste the structural parameter code schema below inside your file, changing the strings to match your real endpoints:

{
  "domain": "mycoolapp.com",
  "primary_target_url": "http://192.0.2.1:8080"
}

*Note: Make sure your `primary_target_url` contains your specific open application port (like `:80`, `:8080`, or `:3000`) and has no missing quotes or trailing commas.*

6. Commit the file changes and submit a **Pull Request** back to our `main` branch.
7. The automated **Lucky Node Validator Bot** will scan your formatting. If it passes, an administrator will approve and merge your server parameters into active proxy memory!

---

### Phase B: Hook Up Your Network Routing (Using the Render URL)

Once your Pull Request is merged, you must instruct the global domain system to route traffic through the Lucky central shield. You achieve this using our public **Render Master Node Address**.

#### How to configure your DNS records:


| Record Type | Host / Name | Target / Value / Points To | TTL |
| :--- | :--- | :--- | :--- |
| CNAME | @ (or leave empty) | luckysrvr.onrender.com | Automatic / 1 Hour |
| CNAME | www | luckysrvr.onrender.com | Automatic / 1 Hour |

*Crucial Note: Substitute the value target field with the precise, unique public live web app link running on our Render instance.*

5. **Save** the record changes. Allow up to 5-15 minutes for the new DNS instructions to update across the internet.

---

## Advanced: Hosting a Lucky Master Node on a VPS

If you do not want to use Render and prefer to host your own independent Lucky cluster node on a Virtual Private Server (VPS) with 24/7 uptime and custom port flexibility, follow this enterprise installation manual.

### 🏗️ Minimum Server Requirements
- **Operating System:** Ubuntu 22.04 LTS or Ubuntu 24.04 LTS (Clean installation)
- **Specs:** 1 vCPU, 1 GB RAM (Lightweight, zero-dependency script)
- **Ports to open:** 8000 (Proxy Engine) and 22 (SSH Management)

### 🛠️ Step-by-Step VPS Deployment Manual

#### 1. Establish Secure Connection to Your VPS
Open your computer's terminal (or the iSH App on iPad) and authenticate into your remote machine using your server's public IP address:
ssh root@YOUR_VPS_PUBLIC_IP

#### 2. System Optimization & Dependency Setup
Update the native Ubuntu packages and pull down the Python core environment tools:
sudo apt update && sudo apt upgrade -y
sudo apt install python3 git -y

#### 3. Clone the Cluster Repository
Pull the stable node logic directly into your server architecture:
git clone https://github.com/LuckySrvr/LuckySrvr
cd LuckySrvr

#### 4. Configure as a Persistent Background Daemon (Systemd)
To ensure lucky_core.py doesn't crash when you close your terminal, and automatically restarts if the VPS reboots, create an automated system service manager rule:

sudo cat << 'EOF' > /etc/systemd/system/lucky.service
[Unit]
Description=Lucky Failover Proxy Cluster Node
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/Lucky
ExecStart=/usr/bin/python3 /root/Lucky/lucky_core.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

#### 5. Ignite the Server Core Engine
Reload the service manager, hook your script into the boot sequence, and turn it on:
sudo systemctl daemon-reload
sudo systemctl enable lucky.service
sudo systemctl start lucky.service

#### 6. Inspect Active Log Streams
Verify that your VPS has successfully read the community nodes/ folder configurations and is actively listening for incoming public connections:
sudo journalctl -u lucky.service -f

*(If successful, you will see output reading: Master cluster initialization sequence complete. Listening on port 8000...)*

---

### 📡 Mapping Domains to Your Custom VPS Node

When users configure their DNS routing tables for a VPS node rather than Render, they cannot use a CNAME record for their root domain. Instead, they must implement a standard A Record:


| Record Type | Host / Name | Target / Value / Points To | TTL |
| :--- | :--- | :--- | :--- |
| A | @ (or leave empty) | YOUR_VPS_PUBLIC_IP | 1 Hour |
| CNAME | www | yourdomain.com | 1 Hour |

---

### 🔄 How to Synchronize New PRs to the VPS Automatically

When you merge a new user configuration on GitHub, the VPS node needs to pull those changes down. To handle this without touching the terminal, add an automated interval pull loop rule (Cronjob):

1. Open your server's scheduler panel:
   crontab -e
2. Paste this rule at the very bottom of the file to auto-sync git changes every 5 minutes:
   */5 * * * * cd /root/Lucky && git pull && sudo systemctl restart lucky.service
3. Save and close. Your VPS will now run completely on autopilot!

---

## Cluster Health and Maintenance Verifications

Developers can test their active configurations or inspect the macro health status of the network at any time:

* **Inspect Network Pulse:** Navigate straight to your cluster's proxy address in your browser. This contacts the node to verify that the core proxy processes are awake and listening 24/7.
* **Format Checking:** If you encounter error logs during your submission, run your file through Python's local parser tool inside your workstation terminal to spot layout typos:
  python3 -m json.tool nodes/yourdomain.json

---

## Licensing & Operational Terms
This open-source cluster setup uses the MIT License standard. By routing nodes through Lucky, developers acknowledge that backup nodes act as voluntary high-availability endpoints without strict commercial service-level agreements.
