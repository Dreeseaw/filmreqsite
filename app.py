'''
william dreese
film launch source code
'''
from flask import Flask, request, render_template
from flask_mail import Mail
from datetime import datetime

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'wdreese123@gmail.com'
app.config['MAIL_PASSWORD'] = 'Dree1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    email = request.form["email"]
    try:
      msg = Message("New Sign Up", sender="wdreese123@gmail.com", recipients=["wdreese123@gmail.com"])
      msg.body = "New Sign Up: "+email+" @ "+str(datetime.now)
      mail.send(msg)
    except Error as e:
      print("error on db call: ", e)
  return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)
