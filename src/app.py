from flask import Flask, send_file, jsonify
import os
import sys

# Initialize Flask to look at the root directory (..) for static files
app = Flask(__name__, static_folder='../', static_url_path='')

@app.route('/')
def index():
    # Serve index.html from the root
    return send_file('../index.html', mimetype='text/html')

@app.route('/data/master_category_bank.json')
def get_categories():
    # Serve data from the data/ directory
    file_path = os.path.join('..', 'data', 'master_category_bank.json')
    if os.path.exists(file_path):
        return send_file(file_path, mimetype='application/json')
    else:
        return jsonify({"error": "Category data not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
