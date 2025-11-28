import streamlit as st
from supabase import create_client, Client

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
@st.cache_resource
def init_connection():
    url = st.secrets["connections"]["supabase"]["SUPABASE_URL"]
    key = st.secrets["connections"]["supabase"]["SUPABASE_KEY"]
    return create_client(url, key)


Signup, Login = st.tabs(["Sign Up", "Log In"])

supabase = init_connection()

def login(email, password):
    user = supabase.auth.sign_in_with_password({"email": email, "password": password})
    
