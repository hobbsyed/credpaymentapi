from flask import Flask
from flask_restful import Resource, Api, reqparse
from cardvalidator import luhn
from datetime import datetime
from gateway import PaymentGateway
import math
import requests

app = Flask(__name__)
api = Api(app)


class ProcessPayment(Resource):

    def get (self):
        parser = reqparse.RequestParser()
        parser.add_argument('ccnum',type=int,required=True)
        parser.add_argument('cardhold', type=str,required=True)
        parser.add_argument('expdt',required=True)
        parser.add_argument('secode',type=int,required=False)
        parser.add_argument('amount',type=float ,required=True)
        args = parser.parse_args()

        try:
            if luhn.is_valid(args['ccnum']):
                if args['cardhold'].replace(" ", "").isalpha():
                    args['cardhold'] = args['cardhold'].upper()
                    if math.floor(math.log10(args['secode'])+1) == 3:
                        if args['amount'] > 0:
                            exp=datetime.strptime(args['expdt'], '%m/%y')
                        else:
                            return {'message': 'Negative Amount not allowed'}, 400
                    else:
                        return {'message': 'Invalid Security Code'}, 400
                else:
                 p   return {'message': 'Invalid Card Name'}, 400
            else:
                return{'message': 'Invalid Card Number'},400

        except ValueError:
            return {'message': 'Invalid Expiry  Date  - Eg : mm/yy'}, 400
        except Exception as e:
            return {'message': e}, 400

        gateway, processcode = PaymentGateway(args['ccnum'], args['amount']).selectinggateway()
        if processcode == 200:
            return{'message': 'Payment processed', 'gateway': gateway}, 200
        else:
            return {'message': gateway}, 400


api.add_resource(ProcessPayment, '/processpayment')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5001)