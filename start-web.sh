#!/bin/bash
# Quick start script for public web server

echo "🎮 CATEGORIES Game - Web Server Launcher"
echo "========================================"

# Check if Flask is installed
python3 -c "import flask" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📦 Installing Flask..."
    pip install Flask --quiet
fi

echo ""
echo "✅ Starting web server..."
echo "📍 Game URL: http://localhost:5000"
echo ""
echo "In Codespaces:"
echo "  - Look for the 'Ports' notification at the bottom of VS Code"
echo "  - Click the globe icon next to port 5000"
echo "  - This gives you a PUBLIC URL anyone can access"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py
