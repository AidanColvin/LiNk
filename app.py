from flask import Flask, send_file, jsonify
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return send_file('index.html', mimetype='text/html')

@app.route('/master_category_bank.json')
def get_categories():
    if os.path.exists('master_category_bank.json'):
        return send_file('master_category_bank.json', mimetype='application/json')
    return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    print("Game running on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000)
