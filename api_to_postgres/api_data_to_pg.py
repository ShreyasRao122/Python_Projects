# import psycopg2
#
#
# p=psycopg2.connect(dbname="wovo_new",host="localhost",user="postgres",password="1234",port=5432)
#
# c=p.cursor()
# c.execute("select * from clients_clientinfo" )
# result = c.fetchall()
# for row in result:
#     print(row)
import requests


class ApiToPostgres:
    def __init__(self):
        self.name="wovo_new"
        self.host="localhost"
        self.user="postgres"
        self.passwd="123"
        self.port="5432"
        self.url="https://reqres.in/api/users/"

    def get_api_data(self):
        response = requests.get("https://reqres.in/api/users/")
        data=response.json()["data"]
        return data

    def process_data_to_postgres(self):
        data = self.get_api_data()
        for i in data:
            print(i)
a=ApiToPostgres()
a.process_data_to_postgres()










