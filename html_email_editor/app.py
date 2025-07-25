from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

@app.route('/')
def index():
    return render_template('editor.html')

@app.route('/save', methods=['POST'])
def save():
    data = request.json
    html_content = data.get('html', '')
    filename = data.get('filename', 'template.html')
    with open(os.path.join(TEMPLATE_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(html_content)
    return jsonify({'status': 'success'})

@app.route('/load/<filename>')
def load_template(filename):
    try:
        with open(os.path.join(TEMPLATE_DIR, filename), 'r', encoding='utf-8') as f:
            html_content = f.read()
        return jsonify({'html': html_content})
    except Exception:
        return jsonify({'html': ''})

if __name__ == '__main__':
    app.run(debug=True)
