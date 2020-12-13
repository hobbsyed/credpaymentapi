
import requests

class PaymentGateway () :
    def __init__(self,ccno,amount):
        self.ccno = ccno
        self.amount = amount


    def expensivepayementgateway(self):
        try:
            response = requests.get(url='http://127.0.0.1:5004/expensive')
            return 'Expensive Payment Gateway', 200
        except Exception as e:
            return 'Expensive Payment server is not available', 404

    def premiumpayementgateway(self):
        try:
            response = requests.get(url='http://127.0.0.1:5003/premium')
            return 'Premium Payment Gateway', 200
        except Exception as e:
            return 'Premium Payment server is not available', 404

    def cheappaymentgateway(self):
        try:
            response=requests.get(url='http://127.0.0.1:5002/cheap')
            return 'Cheap payment gateway', 200
        except Exception as e :
            return  'Cheap payment server is not available', 404



    def selectinggateway(self):
        if self.amount < 20:
            gateway, code = self.cheappaymentgateway()

        if self.amount >= 20 and  self.amount <= 500:
            gateway, code = self.expensivepayementgateway()
            if code==404 :
                print('Trying with Cheap Payment server')
                gateway1, code1 = self.cheappaymentgateway()
                if code1==200:
                    gateway, code= gateway1, code1

        if self.amount > 500:
                counter=1
                while True :
                    gateway, code = self.premiumpayementgateway()
                    if code !=200 and counter!=4:
                        print('Retrying Premium Payment Gateway', +counter)
                        counter=counter+1
                    else :
                        break

        return gateway, code

