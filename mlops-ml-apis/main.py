from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import pickle

columns = ['size', 'year', 'parking']
model = pickle.load(open('model.sav', 'rb'))

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'example'
app.config['BASIC_AUTH_PASSWORD'] = 'example'

basic_auth = BasicAuth(app)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/sentiment/<phrase>')
@basic_auth.required
def sentiment(phrase):
    tb = TextBlob(phrase)
    tb_en = tb.translate(from_lang='pt', to='en')
    polarity = tb_en.sentiment.polarity
    return "polarity: {}".format(polarity)

@app.route('/quotation/', methods=['POST'])
@basic_auth.required
def quotation():
    req = request.get_json()
    req_input = [req[col] for col in columns]
    price = model.predict([req_input])
    return jsonify(price=price[0])

app.run(debug=True)
