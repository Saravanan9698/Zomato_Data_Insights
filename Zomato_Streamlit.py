import nbimporter
import streamlit as st
import pymysql
from Zomato_SQL import DatabaseOperator

print("Streamlit app is running...")

# Page Title
st.set_page_config(page_title="Zomato_Data_Insights",
                   page_icon="🍕",
                   layout="wide",
                   initial_sidebar_state="expanded")

# Initialize the DatabaseOperator class

db = DatabaseOperator(user="root", password="123456789", db_name="zomato_db")

# Sidebar navigation for pages

st.sidebar.title("NAVIGATION")
page = st.sidebar.selectbox("Select Page", ["CRUD Operations", "SQL Insights"])


### CRUD Operations PAGE

if page == "CRUD Operations":
    st.title("🍕 Zomato CRUD Operations")

    operation = st.sidebar.radio("Select Table", ["Customers", "Restaurants", "Orders", "Deliveries"])

    crud_action = st.sidebar.radio("Select Operation", ["Create", "Read", "Update", "Delete", "Alter"])

## Customers CRUD and Alter
    if operation == "Customers":
        st.header("Customer Management")

        if crud_action == "Create":
            st.subheader("Add New Customer")
            name = st.text_input("Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
            address = st.text_input("Address")

            if st.button("Add Customer"):
                db.create_customer(name, email, phone, address)
                st.success(f"Customer '{name}' added successfully!")

        elif crud_action == "Read":
            st.subheader("All Customers")
            customers = db.read_customers()
            st.table(customers)

        elif crud_action == "Update":
            st.subheader("Update Customer Details")
            customers = db.read_customers()
            customer_ids = [cust['customer_id'] for cust in customers]
            selected_id = st.selectbox("Select Customer ID", customer_ids)

            new_name = st.text_input("New Name")
            new_email = st.text_input("New Email")

            if st.button("Update Customer"):
                db.update_customer(selected_id, new_name, new_email)
                st.success(f"Customer ID {selected_id} updated successfully!")

        elif crud_action == "Delete":
            st.subheader("Delete Customer")
            customers = db.read_customers()
            customer_ids = [cust['customer_id'] for cust in customers]
            selected_id = st.selectbox("Select Customer ID to Delete", customer_ids)

            if st.button("Delete Customer"):
                db.delete_customer(selected_id)
                st.success(f"Customer ID {selected_id} deleted successfully!")
                
        elif crud_action == "Alter":
            st.subheader("Alter Customer Table")
            new_column = st.text_input("New Column Name")
            data_type = st.text_input("Data Type (e.g., VARCHAR(255), INT)")

            if st.button("Add Column"):
                db.alter_customer_table(new_column, data_type)
                st.success(f"Column '{new_column}' added to Customers table!")

## Restaurants CRUD and Alter
    elif operation == "Restaurants":
        st.header("Restaurant Management")

        if crud_action == "Create":
            st.subheader("Add New Restaurant")
            name = st.text_input("Restaurant Name")
            location = st.text_input("Location")

            if st.button("Add Restaurant"):
                db.create_restaurant(name, location)
                st.success(f"Restaurant '{name}' added successfully!")

        elif crud_action == "Read":
            st.subheader("All Restaurants")
            restaurants = db.read_restaurants()
            st.table(restaurants)

        elif crud_action == "Update":
            st.subheader("Update Restaurant Details")
            restaurants = db.read_restaurants()
            restaurant_ids = [rest['restaurant_id'] for rest in restaurants]
            selected_id = st.selectbox("Select Restaurant ID", restaurant_ids)

            new_name = st.text_input("New Name")
            new_location = st.text_input("New Location")

            if st.button("Update Restaurant"):
                db.update_restaurant(selected_id, new_name, new_location)
                st.success(f"Restaurant ID {selected_id} updated successfully!")

        elif crud_action == "Delete":
            st.subheader("Delete Restaurant")
            restaurants = db.read_restaurants()
            restaurant_ids = [rest['restaurant_id'] for rest in restaurants]
            selected_id = st.selectbox("Select Restaurant ID to Delete", restaurant_ids)

            if st.button("Delete Restaurant"):
                db.delete_restaurant(selected_id)
                st.success(f"Restaurant ID {selected_id} deleted successfully!")
                
        elif crud_action == "Alter":
            st.subheader("Alter Restaurant Table")
            new_column = st.text_input("New Column Name")
            data_type = st.text_input("Data Type (e.g., VARCHAR(255), INT)")

            if st.button("Add Column"):
                db.alter_restaurant_table(new_column, data_type)
                st.success(f"Column '{new_column}' added to Restaurants table!")

## Orders CRUD and Alter
    elif operation == "Orders":
        st.title("Order Management")

        if crud_action == "Create":
            st.subheader("Create New Order")
            customer_id = st.number_input("Customer ID", min_value=1)
            restaurant_id = st.number_input("Restaurant ID", min_value=1)
            items = st.text_input("Items")
            quantity = st.number_input("Quantity", min_value=1)

            if st.button("Place Order"):
                db.create_order(customer_id, restaurant_id, items, quantity)
                st.success("Order placed successfully!")

        elif crud_action == "Read":
            st.subheader("All Orders")
            orders = db.read_orders()
            st.table(orders)

        elif crud_action == "Update":
            st.subheader("Update Order Details")
            orders = db.read_orders()
            order_ids = [order['order_id'] for order in orders]
            selected_id = st.selectbox("Select Order ID", order_ids)

            new_item = st.text_input("New Item")
            new_quantity = st.number_input("New Quantity", min_value=1)

            if st.button("Update Order"):
                db.update_order(selected_id, new_item, new_quantity)
                st.success(f"Order ID {selected_id} updated successfully!")

        elif crud_action == "Delete":
            st.subheader("Delete Order")
            orders = db.read_orders()
            order_ids = [order['order_id'] for order in orders]
            selected_id = st.selectbox("Select Order ID to Delete", order_ids)

            if st.button("Delete Order"):
                db.delete_order(selected_id)
                st.success(f"Order ID {selected_id} deleted successfully!")
                
        elif crud_action == "Alter":
            st.subheader("Alter Orders Table")
            new_column = st.text_input("New Column Name")
            data_type = st.text_input("Data Type (e.g., VARCHAR(255), INT)")

            if st.button("Add Column"):
                db.alter_order_table(new_column, data_type)
                st.success(f"Column '{new_column}' added to Orders table!")

## Deliveries CRUD and Alter
    elif operation == "Deliveries":
        st.header("Delivery Management")

        if crud_action == "Create":
            st.subheader("Create New Delivery")
            order_id = st.number_input("Order ID", min_value=1)
            delivery_status = st.selectbox("Delivery Status", ["Pending", "Delivered", "Cancelled"])

            if st.button("Add Delivery"):
                db.create_delivery(order_id, delivery_status)
                st.success("Delivery created successfully!")

        elif crud_action == "Read":
            st.subheader("All Deliveries")
            deliveries = db.read_deliveries()
            st.table(deliveries)

        elif crud_action == "Update":
            st.subheader("Update Delivery Status")
            deliveries = db.read_deliveries()
            delivery_ids = [delivery['delivery_id'] for delivery in deliveries]
            selected_id = st.selectbox("Select Delivery ID", delivery_ids)

            new_status = st.selectbox("New Status", ["Pending", "Delivered", "Cancelled"])

            if st.button("Update Delivery"):
                db.update_delivery(selected_id, new_status)
                st.success(f"Delivery ID {selected_id} updated successfully!")

        elif crud_action == "Delete":
            st.subheader("Delete Delivery")
            deliveries = db.read_deliveries()
            delivery_ids = [delivery['delivery_id'] for delivery in deliveries]
            selected_id = st.selectbox("Select Delivery ID to Delete", delivery_ids)

            if st.button("Delete Delivery"):
                db.delete_delivery(selected_id)
                st.success(f"Delivery ID {selected_id} deleted successfully!")
                
        elif crud_action == "Alter":
            st.subheader("Alter Deliveries Table")
            new_column = st.text_input("New Column Name")
            data_type = st.text_input("Data Type (e.g., VARCHAR(255), INT)")

            if st.button("Add Column"):
                db.alter_delivery_table(new_column, data_type)
                st.success(f"Column '{new_column}' added to Deliveries table!")
            
### SQL INSIGHTS PAGE 
elif page == "SQL Insights":
    st.title("📊 SQL Data Insights")

    sql_queries = {
        "1. Retrieve all customers": "SELECT * FROM customers;",
        "2. Retrieve all restaurants": "SELECT * FROM restaurants;",
        "3. Retrieve all orders": "SELECT * FROM orders;",
        "4. Retrieve all deliveries": "SELECT * FROM deliveries;",
        "5. Count total number of customers": "SELECT COUNT(*) FROM customers;",
        "6. Top 5 Premium Customers": "SELECT name, total_orders FROM customers WHERE is_premium = 1 ORDER BY total_orders DESC LIMIT 5",
        "7. Top Rated Restaurants": "SELECT name, rating FROM restaurants ORDER BY rating DESC LIMIT 5",
        "8. Active Customers": "SELECT COUNT(*) FROM customers WHERE signup_date >= CURDATE() - INTERVAL 1 YEAR",
        "9. Most Popular Cuisine": "SELECT preferred_cuisine, COUNT(*) FROM customers GROUP BY preferred_cuisine ORDER BY COUNT(*) DESC LIMIT 1",
        "10. Delivery Efficiency": "SELECT delivery_status, COUNT(*) FROM deliveries GROUP BY delivery_status",
        "11. Top 5 customers with most orders": "SELECT customer_id, COUNT(*) AS total_orders FROM orders GROUP BY customer_id ORDER BY total_orders DESC LIMIT 5;",
        "12. Pending deliveries": "SELECT * FROM deliveries WHERE delivery_status = 'Pending';",
        "13. Orders in the last 7 days": "SELECT * FROM orders WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 7 DAY);",
        "14. Total revenue for each restaurant": "SELECT restaurant_id, SUM(total_amount) AS total_revenue FROM orders GROUP BY restaurant_id;",
        "15. Customers without any orders": "SELECT * FROM customers WHERE customer_id NOT IN (SELECT DISTINCT customer_id FROM orders);",
        "16. Restaurants with zero orders": "SELECT * FROM restaurants WHERE restaurant_id NOT IN (SELECT DISTINCT restaurant_id FROM orders);",
        "17. Delivery status breakdown": "SELECT delivery_status, COUNT(*) AS count FROM deliveries GROUP BY delivery_status;",
        "18. Highest earning restaurant": "SELECT restaurant_id, SUM(total_amount) AS total_revenue FROM orders GROUP BY restaurant_id ORDER BY total_revenue DESC LIMIT 1;",
        "19. Monthly revenue trend": "SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, SUM(total_amount) AS monthly_revenue FROM orders GROUP BY month ORDER BY month;",
        "20. Average order value": "SELECT AVG(total_amount) FROM orders;",
        "21. Total orders today": "SELECT COUNT(*) FROM orders WHERE order_date = CURDATE();",
        "22. Total orders this month": "SELECT COUNT(*) FROM orders WHERE MONTH(order_date) = MONTH(CURDATE());",
        "23. Customers with highest spending": "SELECT customer_id, SUM(total_amount) AS total_spent FROM orders GROUP BY customer_id ORDER BY total_spent DESC LIMIT 5;",
        "24. Number of repeat customers": "SELECT COUNT(customer_id) FROM (SELECT customer_id FROM orders GROUP BY customer_id HAVING COUNT(*) > 1) AS repeat_customers;",
        "25. Restaurants with the most orders this month": "SELECT restaurant_id, COUNT(*) AS order_count FROM orders WHERE MONTH(order_date) = MONTH(CURDATE()) GROUP BY restaurant_id ORDER BY order_count DESC LIMIT 5;",
    }
    selected_query = st.selectbox("Select Query", list(sql_queries.keys()))

    if st.button("Execute Query"):
        query = sql_queries[selected_query]
        result = db.execute_query(query)
        st.table(result)

    if st.button("Show All Queries"):
        for title, query in sql_queries.items():
            st.subheader(title)
            result = db.execute_query(query)
            st.table(result)
            
            
# # Close the connection

# db.close_connection()
# print("Streamlit app is closed...")
