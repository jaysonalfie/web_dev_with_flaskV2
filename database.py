from sqlalchemy import create_engine, text,Table, Column, Integer, String, MetaData, ForeignKey
from decouple import config # Import config from decouple
import random

# Load database configuration from .env file
DB_HOST = config('DB_HOST', default='127.0.0.1')
DB_PORT = config('DB_PORT', default='3306')
DB_USER = config('DB_USER', default='root')
DB_PASSWORD = config('DB_PASSWORD', default='')
DB_NAME = config('DB_NAME', default='eveman2_jobs')
DATABASE_URL = config('DATABASE_URL')  # Load DATABASE_URL from .env


engine = create_engine(DATABASE_URL)

metadata_obj = MetaData()
# with engine.connect() as connection:
#     result = connection.execute(text("select * from jobs"))
#     # print("type(result):",type(result))
#     # result_all =result.all()
#     # print("type(result.all()):", type(result_all))

#     result_dicts =[]
#     # converting a sqlalchemy row object to a dictionary using._asdict()
#     result_dicts = [row._asdict() for row in result]

    # print(result_dicts)

    # first_result = result_all[0]
    # print("type(first_result):",type(first_result))
    # first_result_dict = result_all[0]._asdict()
    # print("type(first_result_dict):",type(first_result_dict))
    # print(first_result_dict)
def load_jobs_from_db():
    with engine.connect() as connection:
        result = connection.execute(text("select * from jobs"))

        jobs = []
        # Converting a SQLAlchemy row object to a dictionary using _asdict()
        for row in result:
            jobs.append(row._asdict())

    return jobs


def load_job_from_db(id):
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT * FROM jobs WHERE id = :val"),
            {'val': id}  # Pass the parameter as a dictionary
        )
        row = result.fetchone()  # Use fetchone() to get a single row
        if row is None:
            return None
        else:
            return row._asdict()  # Convert the Row object to a dictionary

def add_application_to_db( id,data):
    with engine.connect() as connection:
        query = text(
"INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url)"
"VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
        )

        dataTobeInserted={
            "job_id":id,
            "full_name":data['full_name'],
            "email":data['email'],
            "linkedin_url":data['linkedin_url'],
            "education":data['education'],
            "work_experience":data['work_experience'],
            "resume_url":data['resume_url']
        }
        # print(dataTobeInserted)

        connection.execute(query,dataTobeInserted)
        
        connection.commit()

    # Add a return statement to indicate success
    return "Application added to the database successfully"



        
        