from flask import Flask,render_template,redirect,request,g
from utils.get_db import get_db
app = Flask(__name__)

@app.before_request
def set_db():
 g.db=get_db()

@app.route('/')
def home():
 return render_template('home.html')


if __name__ == '__main__':
 app.run(debug=True)