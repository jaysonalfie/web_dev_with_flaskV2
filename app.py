from flask import Flask, render_template, jsonify,request #using template
from database import engine, load_job_from_db,add_application_to_db
from sqlalchemy import text

#creating a flask app
app = Flask(__name__)

#creating python list in which jobs will be stored
# JOBS = [
#      {
#           'id': 1,
#           'title': 'Data analyst',
#           'location': 'Nairobi, Kenya',
#           'salary': 'Ksh 100,000'
#      },
#      {
#           'id': 2,
#           'title': 'Data Scientist',
#           'location': 'Nakuru, Kenya',
#           'salary': 'Ksh 150,000'
#      },
#       {
#           'id': 3,
#           'title': 'Software Engineer',
#           'location': 'Momabasa, Kenya',
          
#      },
#        {
#           'id': 4,
#           'title': 'Backend Engineer',
#           'location': 'Remote',
#           'salary': 'Ksh 180,000'
#      }
# ]
#function that returns jobs from db
def load_jobs_from_db():
    with engine.connect() as connection:
        result = connection.execute(text("select * from jobs"))

        jobs = []
        # Converting a SQLAlchemy row object to a dictionary using _asdict()
        for row in result:
            jobs.append(row._asdict())

    return jobs

    


#registering route to application
@app.route("/")
def hello_world():
     jobs_list = load_jobs_from_db()
     return  render_template('home.html',
                             jobs = jobs_list) 
     
     
@app.route("/api/jobs")
def list_jobs():
     jobs_list = load_jobs_from_db()
     return jsonify(jobs_list)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template('jobpage.html',
                             job = job)

@app.route("/job/<id>/apply", methods=['GET', 'POST'])
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)

     #populating the app table in the db
    add_application_to_db(id,data)
    # Store this in the database
    # Display an acknowledgement
    # May send an email
    return render_template('application_submitted.html',
                           application=data,
                           job=job)







if __name__ == "__main__":
     #starting and running of the app
     app.run(host='0.0.0.0', debug=True)   
      