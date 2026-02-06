"""
Flask web server to serve the CATEGORIES game publicly.
Allows anyone with the URL to play without signing in.

Usage:
    python app.py          # Runs on localhost:5000
    python app.py --port 8000   # Runs on custom port
"""

from flask import Flask, send_file, jsonify
import os
import sys

app = Flask(__name__, static_folder='.', static_url_path='')

# Configure CORS for full accessibility
try:
    from flask_cors import CORS
    CORS(app)
except ImportError:
    pass  # CORS not required for local usage

@app.route('/')
def index():
    """Serve the main game HTML file."""
    return send_file('index.html', mimetype='text/html')

@app.route('/master_category_bank.json')
def get_categories():
    """Serve the category data JSON file."""
    if os.path.exists('master_category_bank.json'):
        return send_file('master_category_bank.json', mimetype='application/json')
    else:
        return jsonify({"error": "Category data not found"}), 404

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors gracefully."""
    return jsonify({"error": "File not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors gracefully."""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Get port from command line or use default
    port = 5000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1].replace('--port', '').strip())
        except (ValueError, IndexError):
            pass
    
    print(f"""
    🎮 CATEGORIES Game Web Server
    ════════════════════════════
    
    ✅ Server running on:
       Local:  http://localhost:{port}
       
    📍 In GitHub Codespaces:
       1. Look for "Ports" at the bottom of VS Code
       2. Click the globe icon next to port {port}
       3. Share the public URL with anyone - no login needed!
       
    Press Ctrl+C to stop
    """)
    
    # Bind to 0.0.0.0 to make it accessible from any network
    app.run(host='0.0.0.0', port=port, debug=False)
