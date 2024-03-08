from flask import Flask,render_template,redirect,request,g
from utils.get_db import get_db
from model.drawing import Drawing
app = Flask(__name__)

@app.before_request
def set_db():
 g.db=get_db()

@app.route('/')
def home():
 query=g.db.query(Drawing).all()
 if query == [] or query is None:
  return render_template('home.html',pant="<h2 style=text-align:center;font-family:Truculenta;margin-top:62px>No Drawing Available</h2>")

@app.route('/',methods=['POST'])
def search():
 if request.method == 'POST':
  name=request.form['name']
  query=g.db.query(Drawing).filter(name.lower() in Drawing.name.lower() or Drawing.name.lower() in name.lower())
  return render_template('store.html',query=query)  ## To Modified Later
 


if __name__ == '__main__':
 app.run(debug=True)