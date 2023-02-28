from sqlalchemy import create_engine,text

engine = create_engine("mysql+pymysql://34wlyt739b1vr8j3gghpr:pscale_pw_9zjZQFpR7BZhnUNGRtX7lqm9N2YpGQ74SQRXwBr3JJ8@ap-south.connect.psdb.cloud/variants?charset=utf8mb4")

with engine.connect() as conn:
  result = conn.execute(text('select * from sem'))
  print(result.all())