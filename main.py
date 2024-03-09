from flask import Flask,render_template,redirect,request,session,g
from utils.get_db import get_db
from model.drawing import Drawing
from model.user import User
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint
app = Flask(__name__)
app.secret_key='shop12'

def send_email(email,name):
 msg = MIMEMultipart()
 otp= randint(1000,9999)
 msg['From'] = 'techabissa@gmail.com'
 msg['To'] = email
 msg['Subject'] = 'Verify Your Email Address Shop Pantings'
 body = f'Hello {name},\n\nPlease verify your email address by inserting otp on Website\nOtp -:  **{otp}**\n\nIf you did not make this request, please ignore this email and your account will not be created.\n\nRegards,\n<NAME>'
 msg.attach(MIMEText(body, 'plain'))
 server = smtplib.SMTP('smtp.gmail.com', 587)
 server.starttls()
 server.login('techabissa@gmail.com', 'kzzk ekju htpx vicm')
 text = msg.as_string()
 server.sendmail('techabissa@gmail.com', email, text)
 session['otp']=otp

 server.quit()

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
 
@app.route('/sign',methods=['GET'])
def signup():
 return render_template('sign.html')

@app.route('/signup/',methods=['POST'])
def sign():
 name= request.form.get('name')
 email= request.form.get('email')
 passw=request.form.get('pass')
 session['name']=name
 session['email']=email
 session['password']=passw
 return redirect('/verify')

@app.route('/verify/',methods=['GET'])
def signl():
 send_email(session.get('email'),session.get('name'))
 return render_template('verify.html')

@app.route('/otpveri/',methods=['POST'])
def otpveri():
 db=g.db
 otp= request.form.get('otp')
 if int(session.get('otp')) == int(otp):
  user=User(name=session.get('name'),email=session.get('email'),password=session.get('password'))
  db.add(user)
  db.commit()
  db.refresh(user)
  db.close()
  session['is_login']=True
  return render_template('afterlogin.html')#user=user.name
 return render_template('verify.html')


if __name__ == '__main__':
 app.run(debug=True)