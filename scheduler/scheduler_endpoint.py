# scheduler_endpoint.py
from flask import Flask

app = Flask(__name__)

@app.route('/scheduler', methods=['GET'])
def scheduler_trigger():
    print('Запланированное задание выполнено')
    return 'Задание выполнено', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)