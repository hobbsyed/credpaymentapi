# Credit Card Payment Environment
This repo consist of api local environment for credit card payment . Each `.py` file is designed to run on ``localhost`` on different ports.



```python
pip install -r requirements.txt
```

### app.py

Please run the above python file first to activate credit card api service. Below given URI is used to reach the api service.

```url
http://127.0.0.1:5001/processpayment 
```

#### Parameters
   **ccno**- Credit Card Number (mandatory)
   **cardhold**- Credit Card Holder Name (mandatory)
   **expdt**- Credit Card Expiry Date Eg : 10/22 for October 20222 (mandatory)
   **secode**- Credit Card Security Code (CVV)  (optional) 
   **amount**- Amount (mandatory)
   

### gateway.py

This class selects the payment gateway based on the amount given to the api . 

```This class is called on the app.py so no need to run seperately```


### cheapserver.py   expenseserver.py    premiumserver.py

 ```Please run the above servers based on the test cases```.
```url
http://127.0.0.1:5002/cheap
http://127.0.0.1:5002/cheap
http://127.0.0.1:5004/premium

```
