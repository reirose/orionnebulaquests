import psycopg2

host = 'ec2-63-34-97-163.eu-west-1.compute.amazonaws.com'
user = 'embmbunftgkamj'
password = 'b64bec5b40a806f84f32d3ea98c79e72caeff029882d56882f9d9abe026d42a8'
db_name = "d5lmfb255cr73a"

conn = psycopg2.connect(host=host, user=user, password=password, dbname=db_name)
conn.set_session(autocommit=True)

cur = conn.cursor()
query = cur.execute
