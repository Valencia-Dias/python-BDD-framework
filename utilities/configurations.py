import configparser
import mysql.connector
from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config


connect_config = {
    'user': getConfig()['SQl']['user'],
    'password': getConfig()['SQl']['password'],
    'host': getConfig()['SQl']['host'],
    'database': getConfig()['SQl']['database']
}


def getPassword():
    return "Romans@0808"


def getConnection():
    # conn = mysql.connector.connect(host="localhost", database="APIDevelop", user="root", password="password")
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Successful connection")
            return conn
    except Error as e:
        print(e)


def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row_or_tuple = cursor.fetchone()
    conn.close()
    return  row_or_tuple
