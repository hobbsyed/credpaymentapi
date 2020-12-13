from flask import Flask

expensive = Flask(__name__)

@expensive.route('/expensive')
def homepage():
    return 'Expense Server Transaction Succesfull'

if __name__ == '__main__':
    expensive.run(host='127.0.0.1', port=5004)