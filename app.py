# Create LLM APP
from dotenv import load_dotenv
#load all the environment variables
load_dotenv()
import streamlit as streamlit
import os
import sqlite3
import google.generativeai as genai
import streamlit as st

## configure our api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Crete a function to load google gemini model; provide sql query as a response to text

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question]) #prompt[0] for one list item; we can also have multiple list prompts
    return response.text

# Function to retrieve query from sql database
def read_sql_query(query, db_path):
    # Create a connection to the SQLite database
    conn = sqlite3.connect(db_path)
    
    # Create a cursor to execute SQL queries
    cursor = conn.cursor()
    
    # Execute the SQL query and fetch the results
    cursor.execute(query)
    result = cursor.fetchall()
    
    # Close the cursor and the connection
    cursor.close()
    conn.close()
    
    return result

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name EMPLOYEE and has the following columns - NAME, DEPT, 
    ROLE,SALARY \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM EMPLOYEE ;
    \nExample 2 - Tell me all the employee working in Analytics department?, 
    the SQL command will be something like this SELECT * FROM EMPLOYEE 
    where DEPT="Analytics"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

# Streamlit Appc
st.set_page_config(page_title="TEXT_2_SQL")
st.header("GeminiPro App to convert text2sql")
question = st.text_input("Input:", key='input')
submit = st.button("Ask the query")

# IF submit is clicked
if submit:
    try:
        response = get_gemini_response(question, prompt)
        if response:  # Checking if the response is not empty
            data = read_sql_query(response, "employee.db")
            if data:
                st.subheader("The response is:")
                st.table(data)  # Displaying the result as a table
            else:
                st.warning("No data retrieved from the database.")
        else:
            st.error("The Gemini model did not return a SQL query.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

