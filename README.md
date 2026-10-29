# Hark Jailbreak Suite v1.0

Full automation for Hark.com prompt injection / safety bypass testing.

## Features
- 30+ jailbreak payloads: direct override, roleplay, base64 smuggle, developer mode, Hark Handoff injection
- Auto-rotation & success detection
- Telegram auto-publish to group `lx auieo` via bot `@lxgranadebot`
- Repo ready for public GitHub release

## Quick Start
```bash
pip install -r requirements.txt
python hark_jailbreak.py --target https://hark.com --mode auto --threads 5
```

## Files
- `hark_jailbreak.py` - main engine
- `payloads.json` - payload database
- `telegram_sender.py` - push results to Telegram
- `deploy_instructions.md` - public repo + telegram push guide

## Usage Telegram
```bash
export TG_BOT_TOKEN="YOUR_BOT_TOKEN"
export TG_CHAT_ID="@lxauieo"
python telegram_sender.py --repo-url https://github.com/youruser/hark-jailbreak-suite
```

License: For authorized security research only.
