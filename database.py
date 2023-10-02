from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:@127.0.0.1/eveman2_jobs?charset=utf8mb4")
with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))
    # print("type(result):",type(result))
    # result_all =result.all()
    # print("type(result.all()):", type(result_all))

    result_dicts =[]
    # converting a sqlalchemy row object to a dictionary using._asdict()
    result_dicts = [row._asdict() for row in result]

    print(result_dicts)

    # first_result = result_all[0]
    # print("type(first_result):",type(first_result))
    # first_result_dict = result_all[0]._asdict()
    # print("type(first_result_dict):",type(first_result_dict))
    # print(first_result_dict)