import psycopg2


def connect_db():
    try:
        conn = psycopg2.connect("dbname='election' user='postgres' host='localhost' password='Vlad1309'")
        return conn
    except:
        print("I am unable to connect to the database")