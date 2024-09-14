# https_endpoint.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def https_trigger():
    data = request.json
    print(f'Получен HTTPS запрос: {data}')
    return jsonify({'message': 'Запрос получен'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
