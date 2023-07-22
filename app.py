from flask import Flask
#creating a flask app
app = Flask(__name__)

#registering route to application
@app.route("/")
def hello_world():
     return "Hello, world" 


if __name__ == "__main__":
     #starting and running of the app
     app.run(host='0.0.0.0', debug=True)  
      