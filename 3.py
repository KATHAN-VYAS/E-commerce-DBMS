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

# Function to fetch table schema
def fetch_table_schema(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"DESCRIBE {table_name}")
    return cursor.fetchall()

# Function to fetch all data from a table
def fetch_table_data(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    return cursor.fetchall()

# Function to insert data
def insert_data(connection, query):
    execute_query(connection, query)

# Function to delete data
def delete_data(connection, query):
    execute_query(connection, query)

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

# Streamlit UI
st.title("MySQL Database Management")

# Dropdown to select table
selected_table = st.sidebar.selectbox("Select Table", ["Product", "Supplier", "Orders", "OrderItem", "Shipment", "Inventory"])

# Display table schema
st.subheader("Table Schema")
if selected_table:
    table_schema = fetch_table_schema(connection, selected_table)
    st.table(table_schema)

# Display available values in the selected table
st.subheader("Available Values")
if selected_table:
    table_data = fetch_table_data(connection, selected_table)
    st.table(table_data)

# Inserting data
st.subheader("Insert Data")
if selected_table:
    st.write(f"Inserting into {selected_table}")
    if selected_table == "Product":
        for i in range(st.sidebar.slider("Number of Entries to Insert", 1, 10)):
            # Assuming a simple input for now, you can expand this with appropriate input fields
            product_ID = st.number_input(f"ProductID {i+1}",step = 1)
            product_name = st.text_input(f"Product Name {i+1}")
            sku = st.text_input(f"SKU {i+1}")
            description = st.text_area(f"Description {i+1}")
            price = st.number_input(f"Price {i+1}", step=0.01)
            supplier_id = st.number_input(f"Supplier ID {i+1}", min_value=1, step=1)
            
            if st.button(f"Insert {i+1}"):
                try:
                    insert_query = f"INSERT INTO {selected_table} (ProductID, Name, SKU, Description, Price, SupplierID) VALUES ('{product_ID}','{product_name}', '{sku}', '{description}', {price}, {supplier_id})"
                    insert_data(connection, insert_query)
                    #refreshing
                    st.success("Data inserted successfully!")
                    st.subheader("Updated Table")
                    table_data = fetch_table_data(connection, selected_table)
                    st.table(table_data)
                except Exception as e:
                    st.error(f"Error inserting data: {str(e)}")
    if selected_table == "Supplier":
        for i in range(st.sidebar.slider("Number of Entries to Insert", 1, 10)):
            # Assuming a simple input for now, you can expand this with appropriate input fields
            supplier_id = st.number_input(f"SupplierID {i+1}")
            supplier_name = st.text_input(f"Supplier Name {i+1}")
            supplier_contact = st.text_input(f"Supplier contact {i+1}")
            supplier_email = st.text_area(f"Email {i+1}")
            address = st.text_input(f"address {i+1}")
            
            if st.button(f"Insert {i+1}"):
                try:
                    insert_query = f"INSERT INTO {selected_table} (SupplierID,Name,Contact,Email,Address) VALUES ('{supplier_id}','{supplier_name}', '{supplier_contact}', '{supplier_email}', '{address}')"
                    insert_data(connection, insert_query)
                    st.success("Data inserted successfully!")
                    #refreshing
                    st.subheader("Updated Table") 
                    table_data = fetch_table_data(connection, selected_table)
                    st.table(table_data)
                except Exception as e:
                    st.error(f"Error inserting data: {str(e)}")
    if selected_table == "Orders":
        for i in range(st.sidebar.slider("Number of Entries to Insert", 1, 10)):
            # Assuming a simple input for now, you can expand this with appropriate input fields
            order_id = st.number_input(f"OrderID {i+1}, step=1")
            customer_ID = st.number_input(f"Customer ID {i+1}, step=1")
            order_date = st.date_input(f"Order date {i+1}")
            status = st.text_area(f"Status {i+1}")
    
            if st.button(f"Insert {i+1}"):
                try:
                    insert_query = f"INSERT INTO {selected_table} (OrderID,CustomerID,OrderDate,Status) VALUES ('{order_id}','{customer_ID}', '{order_date}', '{status}')"
                    insert_data(connection, insert_query)
                    st.success("Data inserted successfully!")
                    #refreshing 
                    st.subheader("Updated Table")
                    table_data = fetch_table_data(connection, selected_table)
                    st.table(table_data)
                except Exception as e:
                    st.error(f"Error inserting data: {str(e)}")
    if selected_table == "OrderItem":
        for i in range(st.sidebar.slider("Number of Entries to Insert", 1, 10)):
            # Assuming a simple input for now, you can expand this with appropriate input fields
            order_item_id = st.number_input(f"OrderItemID {i+1}, step=1")
            order_id = st.number_input(f"OrderID {i+1}, step=1")
            product_ID = st.number_input(f"ProductID {i+1}")
            quantity = st.number_area(f"Quantity {i+1}")
            unitprice = st.number_input(f"UnitPrice {i+1}")
    
            if st.button(f"Insert {i+1}"):
                try:
                    insert_query = f"INSERT INTO {selected_table} (OrderItemID,OrderID,ProductID,Quantity,UnitPrice) VALUES ('{order_item_id}','{order_id}', '{product_ID}', '{quantity}', '{unitprice}')"
                    insert_data(connection, insert_query)
                    st.success("Data inserted successfully!")
                    #refreshing 
                    st.subheader("Updated Table")
                    table_data = fetch_table_data(connection, selected_table)
                    st.table(table_data)
                except Exception as e:
                    st.error(f"Error inserting data: {str(e)}")
    if selected_table == "Shipment":
        for i in range(st.sidebar.slider("Number of Entries to Insert", 1, 10)):
            # Assuming a simple input for now, you can expand this with appropriate input fields
            shipment_id = st.number_input(f" ShipmentID {i+1}, step=1")
            order_id = st.number_input(f"OrderID {i+1}, step=1")
            product_ID = st.number_input(f"ProductID {i+1}")
            shipment_date = st.date_input(f"ShipmentDate {i+1}")
            tracking_number = st.number_input(f"TrackingNumber {i+1}")
    
            if st.button(f"Insert {i+1}"):
                try:
                    insert_query = f"INSERT INTO {selected_table} (ShipmentID,OrderID,ShipmentDate,TrackingNumber) VALUES ('{shipment_id}','{order_id}', '{shipment_date}', '{tracking_number}')"
                    insert_data(connection, insert_query)
                    st.success("Data inserted successfully!")
                    #refreshing 
                    st.subheader("Updated Table")
                    table_data = fetch_table_data(connection, selected_table)
                    st.table(table_data)
                except Exception as e:
                    st.error(f"Error inserting data: {str(e)}")
    if selected_table == "Inventory":
        for i in range(st.sidebar.slider("Number of Entries to Insert", 1, 10)):
            # Assuming a simple input for now, you can expand this with appropriate input fields
            inventory_id = st.number_input(f" InventoryID {i+1}, step=1")
            product_ID = st.number_input(f"ProductID {i+1}")
            quantity = st.date_input(f"Quantity {i+1}")
            location = st.number_input(f"Location {i+1}")
    
            if st.button(f"Insert {i+1}"):
                try:
                    insert_query = f"INSERT INTO {selected_table} (InventoryID,productID,Quantity,Location) VALUES ('{inventory_id}','{product_ID}', '{quantity}', '{location}')"
                    insert_data(connection, insert_query)
                    st.success("Data inserted successfully!")
                    #refreshing 
                    st.subheader("Updated Table")
                    table_data = fetch_table_data(connection, selected_table)
                    st.table(table_data)
                except Exception as e:
                    st.error(f"Error inserting data: {str(e)}")


# Deleting data
st.subheader("Delete Data")
if selected_table:
    st.write(f"Deleting from {selected_table}")
    for i in range(st.sidebar.slider("Number of Entries to Delete", 1, 10)):
        # Assuming a simple input for now, you can expand this with appropriate input fields
        entry_id = st.number_input(f"Entry ID to Delete {i+1}", min_value=1, step=1)
        
        if st.button("Delete"):
            try:
                delete_query = f"DELETE FROM {selected_table} WHERE ProductID = {entry_id}"  # Assuming ProductID for simplicity
                delete_data(connection, delete_query)
                st.success("Data deleted successfully!")
                #refreshing
                st.subheader("Updated Table")
                table_data = fetch_table_data(connection, selected_table)
                st.table(table_data)
            except Exception as e:
                st.error(f"Error deleting data: {str(e)}")