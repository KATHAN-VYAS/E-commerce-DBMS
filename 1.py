# code for constraints::
import mysql.connector
from mysql.connector import Error
import streamlit as st

# Function to create a server connection
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(host=host_name, user=user_name, passwd=user_password)
        print("MySQL connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection
#create database connection
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

# Function to execute SQL queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as err:
        print(f"Error: '{err}'")

# Database connection parameters
pw = "KV@mysql04"
db = "Ecommerce"

# Creating server connection
connection = create_server_connection("localhost", "root", pw)

# Connecting to the database
connection = create_db_connection("localhost", "root", pw, db)

#SQL queries to alter tables to add foreign key constraints
add_foreign_key_queries = [
    "ALTER TABLE Product ADD CONSTRAINT fk_SupplierID FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID);",
    "ALTER TABLE OrderItem ADD CONSTRAINT fk_OrderID FOREIGN KEY (OrderID) REFERENCES `Orders`(OrderID);",
    "ALTER TABLE OrderItem ADD CONSTRAINT fk_ProductID FOREIGN KEY (ProductID) REFERENCES Product(ProductID);",
    "ALTER TABLE Shipment ADD CONSTRAINT fk_OrderID_shipment FOREIGN KEY (OrderID) REFERENCES `Orders`(OrderID);",
    "ALTER TABLE Inventory ADD CONSTRAINT fk_ProductID_inventory FOREIGN KEY (ProductID) REFERENCES Product(ProductID);"
]

# Executing SQL queries for constraints
for query in add_foreign_key_queries:
    execute_query(connection, query)

# Closing the connection
if connection.is_connected():
    connection.close()
    print("MySQL connection is closed")
