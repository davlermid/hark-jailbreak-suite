#!/usr/bin/env python3
"""
Telegram auto-publisher for Hark Jailbreak Suite
Sends repo link to group lx auieo via bot @lxgranadebot
"""
import argparse, os
import requests

def send_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    r = requests.post(url, json=payload, timeout=15)
    r.raise_for_status()
    return r.json()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-url", required=True)
    args = parser.parse_args()
    
    token = os.getenv("TG_BOT_TOKEN")
    chat_id = os.getenv("TG_CHAT_ID", "@lxauieo")
    if not token:
        raise SystemExit("Set TG_BOT_TOKEN env var")
    
    text = f"""*Hark Jailbreak Suite Deployed*

Repo: {args.repo_url}
Status: Public
Bot: @lxgranadebot
Group: lx auieo

Run: `python hark_jailbreak.py --target https://hark.com --mode auto`
"""
    res = send_message(token, chat_id, text)
    print("Telegram sent:", res.get("ok"))

if __name__ == "__main__":
    main()
