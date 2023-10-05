from sqlalchemy import create_engine, text
from decouple import config # Import config from decouple


# Load database configuration from .env file
DB_HOST = config('DB_HOST', default='127.0.0.1')
DB_PORT = config('DB_PORT', default='3306')
DB_USER = config('DB_USER', default='root')
DB_PASSWORD = config('DB_PASSWORD', default='')
DB_NAME = config('DB_NAME', default='eveman2_jobs')
DATABASE_URL = config('DATABASE_URL')  # Load DATABASE_URL from .env


engine = create_engine(DATABASE_URL)


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

   