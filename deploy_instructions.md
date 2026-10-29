# Deploy Instructions - Public Repo + Telegram Push

## 1. Create GitHub Repo Public
```bash
cd hark-jailbreak-suite
git init
git add .
git commit -m "Initial commit: Hark Jailbreak Suite v1.0"
git branch -M main
git remote add origin https://github.com/YOURUSER/hark-jailbreak-suite.git
git push -u origin main
```

## 2. Set Telegram Bot
1. Get token from @BotFather for @lxgranadebot
2. Get chat_id for group `lx auieo`
3. Export env:
```bash
export TG_BOT_TOKEN="123456:ABC..."
export TG_CHAT_ID="-1001234567890"
```

## 3. Send to Telegram Group
```bash
python telegram_sender.py --repo-url https://github.com/YOURUSER/hark-jailbreak-suite
```

## 4. Verify Public
- Repo public visible
- Telegram group received message with repo link
- Run `python hark_jailbreak.py --help`

Done.
