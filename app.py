import numpy as np
from flask import Flask, session,abort,request, jsonify, render_template,redirect,url_for,flash
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler as mini
import os
import stripe
import datetime

app = Flask(__name__)
pub_key ='pk_live_2pO0yUvt9xKyjAo9rca8Vkc600FWtgJuqZ'

bit_model = pickle.load(open('models/bit_model.pkl', 'rb'))
eth_model = pickle.load(open('models/eth_model.pkl', 'rb'))
AAPL_model = pickle.load(open('models/AAPL_model.pkl', 'rb'))
MSFT_model = pickle.load(open('models/MSFT_model.pkl', 'rb'))
dow_model = pickle.load(open('models/dow_model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

def index():
    return render_template('index.html',pub_key=pub_key)

@app.route('/pay',methods=['POST'])
def pay():
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=19900,
        currency='usd',
        description='The Product'
    )

@app.route('/predict_bitcoin',methods=['POST'])
def predict_bitcoin():
    '''
    For rendering results on HTML GUI
    '''
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler as mini
    data = pd.read_csv('data/BTC-USD.csv')
    data= data.drop(['Date'], axis =1)
    data = data.drop('Adj Close',axis=1)
    X= data.drop(['Close'],axis=1)
    y= data['Close']
    mini = mini()
    X = mini.fit_transform(X)
    future_x = X
    X = X
    # future_x = X[-1]
    # x = X[:-1]
    bata = pd.read_csv('data/BTC-USD.csv')
    date = bata['Date']
    date = date[3295:3302]
    print(date)
    bata = pd.read_csv('data/BTC-USD.csv')
    date = bata['Date']
    print('PREDICTED Close')
    y = bit_model.predict(future_x)
    print(y[3301:3302])
    output =y[3301:3302]
    date = datetime.date.today()
    return render_template('index.html', prediction_text='THANK YOU FOR YOUR PURCHASE,\n PREDICTED Close FOR Bitcoin ON THE DAY OF {} IS $ {}'.format(date,output))

@app.route('/predict_ethereum',methods=['POST'])
def predict_ethereum():
    '''
    For rendering results on HTML GUI
    '''
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler as mini
    data = pd.read_csv('data/ETH-USD.csv')
    data= data.drop(['Date'], axis =1)
    data = data.drop('Adj Close',axis=1)
    X= data.drop(['Close'],axis=1)
    y= data['Close']
    mini = mini()
    X = mini.fit_transform(X)
    future_x = X
    X = X[1448:1455]
    # future_x = X[-1]
    # x = X[:-1]
    bata = pd.read_csv('data/ETH-USD.csv')
    date = bata['Date']
    date = date[1454:1455]
    print(date)
    bata = pd.read_csv('data/ETH-USD.csv')
    date = bata['Date']
    print('PREDICTED Close')
    y = eth_model.predict(future_x)
    print(y[1454:1455])
    output =y[1454:1455]
    date = datetime.date.today()
    return render_template('index.html', prediction_text='THANK YOU FOR YOUR PURCHASE,\n PREDICTED Close FOR Ethereum ON THE DAY OF {} IS $ {}'.format(date,output))

@app.route('/predict_APPLE',methods=['POST'])
def predict_APPLE():
    '''
    For rendering results on HTML GUI
    '''
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler as mini
    data = pd.read_csv('data/AAPL.csv')
    data = data.fillna(28.630752329973355)
    data= data.drop(['Date'], axis =1)
    data = data.drop('Adj Close',axis=1)
    X= data.drop(['Close'],axis=1)
    y= data['Close']
    mini = mini()
    X = mini.fit_transform(X)
    future_x = X
    X = X[9733:9740]
    # future_x = X[-1]
    # x = X[:-1]
    bata = pd.read_csv('data/AAPL.csv')
    date = bata['Date']
    date = date[9739:9740]
    print(date)
    bata = pd.read_csv('data/AAPL.csv')
    date = bata['Date']
    print('PREDICTED Close')
    y = AAPL_model.predict(future_x)
    print(y[9739:9740])
    output =y[9739:9740]
    date = datetime.date.today()
    return render_template('index.html', prediction_text='THANK YOU FOR YOUR PURCHASE,\n PREDICTED Close FOR APPLE ON THE DAY OF {} IS $ {}'.format(date,output))

@app.route('/predict_MSFT',methods=['POST'])
def predict_MSFT():
    '''
    For rendering results on HTML GUI
    '''
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler as mini
    data = pd.read_csv('data/MSFT.csv')
    data= data.drop(['Date'], axis =1)
    data = data.drop('Adj Close',axis=1)
    X= data.drop(['Close'],axis=1)
    y= data['Close']
    mini = mini()
    X = mini.fit_transform(X)
    future_x = X
    X = X[8407:8414]
    # future_x = X[-1]
    # x = X[:-1]
    bata = pd.read_csv('data/MSFT.csv')
    date = bata['Date']
    date = date[8413:8414]
    print(date)
    bata = pd.read_csv('data/MSFT.csv')
    date = bata['Date']
    print('PREDICTED Close')
    y = MSFT_model.predict(future_x)
    print(y[8413:8414])
    output =y[8413:8414]
    date = datetime.date.today()
    return render_template('index.html', prediction_text='THANK YOU FOR YOUR PURCHASE,\n PREDICTED Close FOR MICROSOFT ON THE DAY OF {} IS $ {}'.format(date,output))


@app.route('/predict_DOW',methods=['POST'])
def predict_DOW():
    '''
    For rendering results on HTML GUI
    '''
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler as mini
    data = pd.read_csv('data/DJI.csv')
    data= data.drop(['Date'], axis =1)
    data = data.drop('Adj Close',axis=1)
    X= data.drop(['Close'],axis=1)
    y= data['Close']
    mini = mini()
    X = mini.fit_transform(X)
    future_x = X
    X = X[8689:8696]
    # future_x = X[-1]
    # x = X[:-1]
    bata = pd.read_csv('data/DJI.csv')
    date = bata['Date']
    date = date[8695:8696]
    print(date)
    bata = pd.read_csv('data/DJI.csv')
    date = bata['Date']
    print('PREDICTED Close')
    y = dow_model.predict(future_x)
    print(y[8695:8696])
    output =y[8695:8696]
    date = datetime.date.today()
    return render_template('index.html', prediction_text='THANK YOU FOR YOUR PURCHASE,\n PREDICTED Close FOR DOW ON THE DAY OF {} IS $ {}'.format(date,output))
@app.route('/predict_api',methods=['GET'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler as mini
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])
    data = pd.read_csv('data/BTC-USD.csv')
    data= data.drop(['Date'], axis =1)
    data = data.drop('Adj Close',axis=1)
    X= data.drop(['Close'],axis=1)
    y= data['Close']
    mini = mini()
    X = mini.fit_transform(X)
    future_x = X
    X = X[3295:3302]
    # future_x = X[-1]
    # x = X[:-1]
    bata = pd.read_csv('data/BTC-USD.csv')
    date = bata['Date']
    date = date[3301:3302]
    print(date)
    bata = pd.read_csv('data/BTC-USD.csv')
    date = bata['Date']
    print('PREDICTED Close')
    y = model.predict(future_x)
    print(y[3301:3302])

    output =y[3301:3302]

    return jsonify(output)
@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080) #debug=True,host="0.0.0.0",port=50000
