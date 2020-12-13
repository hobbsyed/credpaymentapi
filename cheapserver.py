from flask import Flask
cheap = Flask(__name__)

@cheap.route('/cheap')
def homepage():
    return 'Cheap server Transaction Succesfull'

if __name__ == '__main__':
    cheap.run(host='127.0.0.1',port=5002)

