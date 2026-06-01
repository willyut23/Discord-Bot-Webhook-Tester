# Discord Webhook & Bot Tester

A sleek terminal tool to quickly test Discord webhooks and bot tokens.  
Self-contained — auto-installs dependencies on first run.

---

## ✨ Features

- **Auto‑install** — missing packages (`discord.py`, `requests`) are installed automatically
- **Smart detection** — paste a webhook URL or a bot token; the tool figures it out
- **Instant verification** — sends a test message to confirm everything works
- **Clean terminal UI** — coloured output, ASCII banner, clear prompts
- **No configuration files** — just run the script and go
- **Made By Willyut**

---

## 📦 Setup

**Requirements:** Python 3.7 or later.  
Everything else is handled automatically.

    # Download the script (or clone the repo)
    # Then run it:
    python discord_tester.py

On first run it will install `discord.py` and `requests` if they're not already present.

---

## 🚀 Usage

1. Run the script.
2. Paste your **Discord webhook URL** or **bot token** when prompted.
3. If you pasted a bot token, you'll also be asked for a **channel ID** (the numeric ID where the bot should send a test message).
4. The tool will attempt to send a verification message and report success or failure.

### Example (Webhook)

    Enter a Discord bot token or webhook URL:
    > https://discord.com/api/webhooks/123456/abc...

    Detected webhook URL. Sending verification message...
    ✔ Webhook message sent successfully.

### Example (Bot)

    Enter a Discord bot token or webhook URL:
    > MTAxMjM0NTY3ODkwMTIzNDU2Nzg5.MTIzND...

    Assuming a bot token was entered.
    Enter the channel ID to send the verification message to:
    > 987654321098765432

    Logging in and sending verification message...
    ✔ Logged in as MyBot#1234 (ID: 123456789012345678)
    ✔ Verification message sent to #general.

---

## 🧰 How It Works

- **Webhook test** — sends a simple JSON payload to the Discord webhook endpoint using `requests`.
- **Bot test** — logs into Discord with the token, finds the specified channel, sends a message, then logs out.
- **Dependency handling** — tries multiple `pip` variants to install packages if they're missing, ensuring it works across different Python setups.

---

## ⚠️ Notes

- Your bot must have **Send Messages** permission in the target channel.
- Webhook URLs are one‑time secrets — be careful where you paste them.
- The tool does not store or log any credentials.

---

## 📄 License

Open source and provided as‑is for personal testing and learning.

---

Made by **Willyut**
