import streamlit as st
from deta import Deta

st.write("# Welcome to our pendulum experiment")

# Data to be written to Deta Base
with st.form("form"):
    T = st.number_input("Enter the time period")
    submitted = st.form_submit_button("save")


# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])

# Create a new database "example-db"
# If you need a new database, just use another name.
db = deta.Base("example-db")

# If the user clicked the submit button,
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    db.put({"time period": T})

"---"
"Here's everything stored in the database:"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch().items
st.write(db_content)