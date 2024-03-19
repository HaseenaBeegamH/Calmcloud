import sqlite3
from sqlite3 import Error
import streamlit as st

# Define a function to create a new connection to the SQLite database
def create_connection(db_file):
    """ create a new database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

# Fxn
def create_page_visited_table():
    conn = create_connection('data.db')  # Use create_connection instead of get_connection
    c = conn.cursor()
    try:
        c.execute('CREATE TABLE IF NOT EXISTS pageTrackTable(pagename TEXT,timeOfvisit TIMESTAMP)')
        conn.commit()
        
    except Exception as e:
        st.error(f"Error creating page visited table: {str(e)}")
    finally:
        if conn:
            conn.close()

def add_page_visited_details(pagename,timeOfvisit):
    conn = create_connection('data.db')  # Use create_connection instead of get_connection
    c = conn.cursor()
    try:
        c.execute('INSERT INTO pageTrackTable(pagename,timeOfvisit) VALUES(?,?)',(pagename,timeOfvisit))
        conn.commit()
    except Exception as e:
        st.error(f"Error adding page visited details: {str(e)}")
    finally:
        if conn:
            conn.close()

def view_all_page_visited_details():
    conn = create_connection('data.db')  # Use create_connection instead of get_connection
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM pageTrackTable')
        data = c.fetchall()
        return data
    except Exception as e:
        st.error(f"Error viewing page visited details: {str(e)}")
        return []
    finally:
        if conn:
            conn.close()

# Fxn To Track Input & Prediction
def create_emotionclf_table():
    conn = create_connection('data.db')  # Use create_connection instead of get_connection
    c = conn.cursor()
    try:
        c.execute('CREATE TABLE IF NOT EXISTS emotionclfTable(rawtext TEXT,prediction TEXT,probability NUMBER,timeOfvisit TIMESTAMP)')
        conn.commit()
        
    except Exception as e:
        st.error(f"Error creating emotion classifier table: {str(e)}")
    finally:
        if conn:
            conn.close()

def add_prediction_details(rawtext,prediction,probability,timeOfvisit):
    conn = create_connection('data.db')  # Use create_connection instead of get_connection
    c = conn.cursor()
    try:
        c.execute('INSERT INTO emotionclfTable(rawtext,prediction,probability,timeOfvisit) VALUES(?,?,?,?)',(rawtext,prediction,probability,timeOfvisit))
        conn.commit()
    except Exception as e:
        st.error(f"Error adding prediction details: {str(e)}")
    finally:
        if conn:
            conn.close()

def view_all_prediction_details():
    conn = create_connection('data.db')  # Use create_connection instead of get_connection
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM emotionclfTable')
        data = c.fetchall()
        return data
    except Exception as e:
        st.error(f"Error viewing prediction details: {str(e)}")
        return []
    finally:
        if conn:
            conn.close()







