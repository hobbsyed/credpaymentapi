# Credit Card Payment Environment
This repo consist of api local environment for credit card payment . Each `.py` file is designed to run on ``localhost`` on different ports.



```python
pip install -r requirements.txt
```

### app.py

Please run the above python file first to activate credit card api service.Below give URI is used to reach the api service.

```url
http://127.0.0.1:5001/processpayment 
```

### gateway.py

This class selects the payment gateway based on the amount given to the api
