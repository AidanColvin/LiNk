# 🌐 CATEGORIES Game - Web Server Setup Guide

## Quick Start (Choose One)

### Option 1️⃣: Use Makefile (Easiest)
```bash
make web
```

### Option 2️⃣: Use the Shell Script
```bash
bash start-web.sh
```

### Option 3️⃣: Run Flask Directly
```bash
python3 app.py
```

---

## 📍 Accessing Your Game

### In Your Local Machine
Once the server starts, open this URL in your browser:
```
http://localhost:5000
```

### 🚀 In GitHub Codespaces (CRITICAL FOR PUBLIC ACCESS)

**This is how you get a PUBLIC URL anyone can access:**

1. **Look at the bottom of VS Code** for the "Ports" panel
   - If you don't see it, go to Terminal → Ports

2. **Find port 5000** in the list

3. **Click the globe/world icon** next to port 5000
   - This creates a public URL

4. **Copy the public URL** that appears in the dialog
   - It will look like: `https://username-hash-5000.preview.app.github.dev`

5. **Share this URL** with anyone - they can play without login!

---

## ✅ What Works

The game includes:
- ✅ 4x4 word grid
- ✅ Interactive selection 
- ✅ Real-time feedback ("One off", "2 off", etc.)
- ✅ Shuffle button
- ✅ Definitions & phonetics
- ✅ New Game button
- ✅ All game logic fully client-side (no backend needed)

---

## 🎮 How to Play

1. **Click 4 words** that you think belong together
2. **Click Submit** (or press Enter)
3. **Get feedback:**
   - ✅ Match found → Category revealed
   - "One off" → 3 out of 4 were correct
   - "2 off" → 2 out of 4 were correct
   - "Try again" → 0-1 out of 4 correct
4. **4 mistakes allowed** - shown as circles at bottom

---

## 🔧 Troubleshooting

### Server won't start
```bash
# Check Python version
python3 --version

# Install Flask if needed
pip install Flask

# Try running directly
python3 app.py
```

### Can't access http://localhost:5000
- Make sure the server process is running
- Check if port 5000 is already in use:
  ```bash
  lsof -i :5000  # Show what's using port 5000
  ```

### Codespaces public URL not working
- Make sure port 5000 is marked as "Public" (not Private)
- In Ports panel, right-click port 5000 → Port Visibility → Public

---

## 📊 Architecture

- **Frontend:** `index.html` - Pure HTML/CSS/JavaScript
- **Data:** `master_category_bank.json` - Game categories
- **Server:** `app.py` - Flask web server (serves files only)
- **Zero backend processing** - All game logic runs in browser!

---

## 🎯 Why This Works

✅ **No sign-in required** - Static files served over HTTP
✅ **Anyone can access** - Public URL works for unlimited users  
✅ **No database needed** - Game state lives in browser
✅ **Fast & responsive** - No server computation required
✅ **Offline capable** - Works even if server goes down (after first load)

Enjoy! 🎉
