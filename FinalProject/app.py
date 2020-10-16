from flask import Flask, request, render_template
import yfinance as yf
from pymongo import MongoClient

# instantiate the Flask app.
app = Flask(__name__)

# requests stock info from yahoo finance and prints it on the webpage
@app.route("/quote")
def display_quote():
	symbol = request.args.get('symbol', default="")
	quote = yf.Ticker(symbol)
	client = MongoClient("mongodb+srv://domo0804:Zucchini007@fe520-h0yvv.mongodb.net/test?retryWrites=true&w=majority")
	entry = {}
	for key in quote.info:
		entry[key]=quote.info[key]
	client.fe520.stocks.insert_one(entry)
	unentry = client.fe520.stocks.find_one({'symbol':symbol},projection={'_id': False})
	return unentry

@app.route("/")
def home():
    return render_template("homepage.html")
# run the flask app.
if __name__ == "__main__":
	app.run(debug=True)

