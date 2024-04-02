# code for creating database and table ::

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

# Function to create a database connection
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

# Creating database (should run only once)
create_database_query = "CREATE DATABASE IF NOT EXISTS Ecommerce"
execute_query(connection, create_database_query)

# Connecting to the database
connection = create_db_connection("localhost", "root", pw, db)

#SQL queries to create tables
create_product_table = """
 CREATE TABLE IF NOT EXISTS Product (
     ProductID INT PRIMARY KEY,
     Name VARCHAR(255),
     SKU VARCHAR(50),
     Description TEXT,
     Price DECIMAL(10, 2),
     SupplierID INT
 );
 """

create_supplier_table = """
 CREATE TABLE IF NOT EXISTS Supplier (
     SupplierID INT PRIMARY KEY,
     Name VARCHAR(255),
     Contact VARCHAR(50),
     Email VARCHAR(255),
     Address VARCHAR(255)
 );
 """
create_order_table = """
 CREATE TABLE IF NOT EXISTS `Orders` (
     OrderID INT PRIMARY KEY,
     CustomerID INT,
     OrderDate DATE,
     Status VARCHAR(20)
 );
 """
create_orderitem_table = """
 CREATE TABLE IF NOT EXISTS OrderItem (
     OrderItemID INT PRIMARY KEY,
     OrderID INT,
     ProductID INT,
     Quantity INT,
     UnitPrice DECIMAL(10, 2)
 );
 """

create_shipment_table = """
 CREATE TABLE IF NOT EXISTS Shipment (
     ShipmentID INT PRIMARY KEY,
     OrderID INT,
     ShipmentDate DATE,
     TrackingNumber VARCHAR(50)
 );
 """

create_inventory_table = """
 CREATE TABLE IF NOT EXISTS Inventory (
     InventoryID INT PRIMARY KEY,
     ProductID INT,
     Quantity INT,
     Location VARCHAR(100)
 );
 """