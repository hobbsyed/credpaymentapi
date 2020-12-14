from flask import Flask

premium = Flask(__name__)

@premium.route('/premium')
def homepage():
    return 'Premium Server Transaction Succesfull'


if __name__ == '__main__':
    premium.run(host='127.0.0.1',port=5003)
