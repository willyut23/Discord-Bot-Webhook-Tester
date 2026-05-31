#!/usr/bin/env python3
"""
Sleek Discord Webhook & Bot Tester
----------------------------------
Self-contained tool that:
- Checks & auto-installs required packages (discord.py, requests)
- Presents a sleek terminal menu
- Tests Discord webhooks and bot tokens
Made By Willyut
"""

import sys
import subprocess
import importlib
import time
import os

# ----------------------------------------------------------------------
# Auto-install missing dependencies
# ----------------------------------------------------------------------
def install_and_import(package_name: str, import_name: str = None):
    """
    Try to import a module; if missing, pip install it, then import.
    """
    if import_name is None:
        import_name = package_name
    try:
        importlib.import_module(import_name)
    except ImportError:
        print(f"⚙️  Installing required package: {package_name} ...")
        for pip_cmd in [["pip", "install", package_name],
                        ["pip3", "install", package_name],
                        ["python", "-m", "pip", "install", package_name],
                        ["python3", "-m", "pip", "install", package_name]]:
            try:
                subprocess.check_call(pip_cmd)
                break
            except (subprocess.CalledProcessError, FileNotFoundError):
                continue
        else:
            print("❌ Failed to install dependencies. Please run:")
            print("   pip install discord.py requests")
            sys.exit(1)
        globals()[import_name] = importlib.import_module(import_name)
    else:
        globals()[import_name] = importlib.import_module(import_name)

install_and_import("discord.py", "discord")
install_and_import("requests")

import discord
import requests

# ----------------------------------------------------------------------
#  ANSI color codes
# ----------------------------------------------------------------------
GREEN = "\033[92m"
RED   = "\033[91m"
CYAN  = "\033[96m"
RESET = "\033[0m"
BOLD  = "\033[1m"

# ----------------------------------------------------------------------
#  ASCII Banner
# ----------------------------------------------------------------------
BANNER = f"""{CYAN}
▄▄▄▄    ▒█████  ▄▄▄█████▓   ▄▄▄█████▓▓█████   ██████ ▄▄▄█████▓
▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒   ▓  ██▒ ▓▒▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒
▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░   ▒ ▓██░ ▒░▒███   ░ ▓██▄   ▒ ▓██░ ▒░
▒██░█▀  ▒██   ██░░ ▓██▓ ░    ░ ▓██▓ ░ ▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ 
░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░      ▒██▒ ░ ░▒████▒▒██████▒▒  ▒██▒ ░ 
░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░        ▒ ░░   ░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   
▒░▒   ░   ░ ▒ ▒░     ░           ░     ░ ░  ░░ ░▒  ░ ░    ░    
 ░    ░ ░ ░ ░ ▒    ░           ░         ░   ░  ░  ░    ░      
 ░          ░ ░                          ░  ░      ░           
      ░{RESET}
"""

# ----------------------------------------------------------------------
def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# ----------------------------------------------------------------------
def test_webhook(webhook_url: str) -> None:
    """Send a verification message to the given webhook."""
    data = {"content": "✅ Webhook verification successful!"}
    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        print(f"{GREEN}✔ Webhook message sent successfully.{RESET}")
    except requests.exceptions.HTTPError as e:
        print(f"{RED}✘ Webhook error: {e}{RESET}")
        if response.text:
            print(f"{RED}   Response: {response.text}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}✘ Failed to reach Discord: {e}{RESET}")

# ----------------------------------------------------------------------
def test_bot(token: str, channel_id: int) -> None:
    """Log in as a bot and send a verification message to a channel."""
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{GREEN}✔ Logged in as {client.user} (ID: {client.user.id}){RESET}")
        channel = client.get_channel(channel_id)
        if channel is None:
            print(f"{RED}✘ Could not find channel with ID {channel_id}.{RESET}")
            await client.close()
            return

        try:
            await channel.send("✅ Bot verification successful!")
            print(f"{GREEN}✔ Verification message sent to #{channel.name}.{RESET}")
        except discord.Forbidden:
            print(f"{RED}✘ Bot lacks permission to send messages in that channel.{RESET}")
        except discord.HTTPException as e:
            print(f"{RED}✘ Discord API error: {e}{RESET}")
        finally:
            await client.close()

    try:
        client.run(token)
    except discord.LoginFailure:
        print(f"{RED}✘ Invalid bot token. Please check and try again.{RESET}")
    except Exception as e:
        print(f"{RED}✘ Unexpected error: {e}{RESET}")

# ----------------------------------------------------------------------
def is_webhook_url(user_input: str) -> bool:
    """Check if the input looks like a Discord webhook URL."""
    return user_input.startswith(("https://discord.com/api/webhooks/",
                                 "https://discordapp.com/api/webhooks/"))

# ----------------------------------------------------------------------
def main():
    clear_screen()
    print(BANNER)
    print(f"{CYAN}Made By Willyut{RESET}")
    time.sleep(0.5)

    print(f"{BOLD}Welcome to the Discord Test Tool!{RESET}\n")
    user_input = input(f"{CYAN}Enter a Discord bot token or webhook URL:{RESET}\n> ").strip()

    if not user_input:
        print(f"{RED}No input provided. Exiting...{RESET}")
        sys.exit(1)

    if is_webhook_url(user_input):
        print(f"\n{CYAN}Detected webhook URL. Sending verification message...{RESET}")
        test_webhook(user_input)
    else:
        print(f"\n{CYAN}Assuming a bot token was entered.{RESET}")
        channel_str = input(f"{CYAN}Enter the channel ID to send the verification message to:{RESET}\n> ").strip()
        try:
            channel_id = int(channel_str)
        except ValueError:
            print(f"{RED}✘ Channel ID must be a numeric value.{RESET}")
            sys.exit(1)

        print(f"{CYAN}Logging in and sending verification message...{RESET}")
        test_bot(user_input, channel_id)

    print(f"\n{BOLD}Done. Thank you for testing!{RESET}")

# ----------------------------------------------------------------------
if __name__ == "__main__":
    main()