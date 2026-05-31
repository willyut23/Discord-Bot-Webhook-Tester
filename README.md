# Discord-Bot-Webhook-Tester
Sleek terminal tool to verify your Discord webhooks and bot tokens instantly.

**Made By Willyut**

---

## Features

- **Auto-install dependencies** – No manual `pip install` needed; the script installs required packages automatically.
- **Smart input detection** – Paste a webhook URL or a bot token; the tool figures out which you want to test.
- **Instant verification** – Sends a test message to confirm everything works.
- **Beautiful terminal UI** – Colored output, clear success/error indicators, and an ASCII banner.

---

## Requirements

- **Python 3.8+**
- Packages (installed automatically on first run):
  - `discord.py` (the modern Discord API wrapper)
  - `requests`

---

## Installation & Usage

### 1. Download the script
Clone or download `bot_tester.py` (or whatever you named it).

### 2. Run it
```bash
python bot_tester.py
That's it The script will:

Check if discord.py and requests are installed.

Install them automatically if they're missing (you may see a brief "Installing..." message).

Clear the terminal and display the banner.

Prompt you to enter a Discord bot token or a webhook URL.

How to test
Webhook
Paste a full webhook URL (e.g., https://discord.com/api/webhooks/123456789/abc...).

A Webhook verification successful! message will appear in the designated channel.

Bot
Paste your bot token (from the Discord Developer Portal).

Enter the channel ID where you want the test message to appear (enable Developer Mode in Discord to copy IDs).

The bot will log in, send Bot verification successful! to that channel, and log out.
