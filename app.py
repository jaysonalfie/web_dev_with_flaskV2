from flask import Flask, render_template, jsonify #using template
#creating a flask app
app = Flask(__name__)

#creating python list in which jobs will be stored
JOBS = [
     {
          'id': 1,
          'title': 'Data analyst',
          'location': 'Nairobi, Kenya',
          'salary': 'Ksh 100,000'
     },
     {
          'id': 2,
          'title': 'Data Scientist',
          'location': 'Nakuru, Kenya',
          'salary': 'Ksh 150,000'
     },
      {
          'id': 3,
          'title': 'Software Engineer',
          'location': 'Momabasa, Kenya',
          
     },
       {
          'id': 4,
          'title': 'Backend Engineer',
          'location': 'Remote',
          'salary': 'Ksh 180,000'
     }
]

#registering route to application
@app.route("/")
def hello_world():
     return  render_template('home.html',
                             jobs = JOBS) 
     
     
@app.route("/api/jobs")
def list_jobs():
     return jsonify(JOBS)


if __name__ == "__main__":
     #starting and running of the app
     app.run(host='0.0.0.0', debug=True)   
      