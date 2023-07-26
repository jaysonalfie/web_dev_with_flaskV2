from flask import Flask, render_template#using template
#creating a flask app
app = Flask(__name__)

#registering route to application
@app.route("/")
def hello_world():
     return  render_template('home.html') 


if __name__ == "__main__":
     #starting and running of the app
     app.run(host='0.0.0.0', debug=True)   
      