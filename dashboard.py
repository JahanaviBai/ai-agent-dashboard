import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from serpapi import GoogleSearch
import openai
import tempfile

# Custom CSS Styling for Modern UI
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 45px;
        color: #4CAF50;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .section-title {
        font-size: 24px;
        color: #1976D2;
        font-weight: bold;
        margin-top: 30px;
        border-bottom: 2px solid #1976D2;
        padding-bottom: 5px;
    }
    .button {
        background-color: #03A9F4;
        color: white;
        font-size: 16px;
        font-weight: bold;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .button:hover {
        background-color: #0288D1;
    }
    .status {
        color: #4CAF50;
        font-weight: bold;
    }
    .footer {
        font-size: 14px;
        color: #999;
        text-align: center;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# Title of the Dashboard
st.markdown("<h1 class='title'>🔍 AI Agent Dashboard</h1>", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.header("📂 Dashboard Navigation")
    st.markdown("### 🚀 Quick Links")
    st.write("1️⃣ **Upload CSV**: Process your data.")
    st.write("2️⃣ **Google Sheets**: Connect your sheets.")
    st.write("3️⃣ **Search & Extract**: Extract insights.")
    st.write("4️⃣ **Download Results**: Save your results.")
    st.divider()

# File Upload Section
st.markdown("<div class='section-title'>📁 Upload Your CSV File</div>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"], label_visibility="visible")
data = None

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    st.write("### Preview of Uploaded Data:")
    st.dataframe(data, use_container_width=True)
    selected_column = st.selectbox("Select the column to process:", data.columns)
    st.write(f"You selected: **{selected_column}**")

# Google Sheets Integration
def connect_google_sheets(json_keyfile):
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(json_keyfile.getvalue())
    temp_file.close()

    # Use the temp file path
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(temp_file.name, scope)
    client = gspread.authorize(creds)
    return client

st.markdown("<div class='section-title'>🔗 Google Sheets Integration</div>", unsafe_allow_html=True)
if st.checkbox("Enable Google Sheets Integration"):
    json_keyfile = st.file_uploader("Upload Google API Key JSON", type=["json"])
    if json_keyfile:
        client = connect_google_sheets(json_keyfile)
        st.success("✅ Successfully connected to Google Sheets!")

# Search Feature using SerpAPI
st.markdown("<div class='section-title'>🔍 Perform Web Search</div>", unsafe_allow_html=True)

def search_entity(query):
    params = {
        "q": query,
        "api_key": "your_serpapi_key"  # Replace with your actual SerpAPI key
    }
    search = GoogleSearch(params)
    return search.get_dict()

custom_query = st.text_input("Enter your search query (use {entity} as a placeholder):", placeholder="Search with dynamic entities")
search_results = {}

if st.button("Search Entities"):
    if custom_query and data is not None:
        with st.spinner("Performing search..."):
            for entity in data[selected_column].unique():
                query = custom_query.replace("{entity}", entity)
                results = search_entity(query)
                search_results[entity] = results
                st.write(f"### Results for **{entity}**:")
                st.json(results)

# Extract Information using OpenAI
st.markdown("<div class='section-title'>🤖 Extract Information Using AI</div>", unsafe_allow_html=True)

def extract_info(results, entity):
    prompt = f"Extract relevant information for {entity} from the following results:\n\n{results}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an assistant."}, {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

extracted_info = []

if st.button("Extract Info"):
    if data is not None and custom_query:
        with st.spinner("Extracting information..."):
            for entity in data[selected_column].unique():
                results = search_results.get(entity, {})
                extracted = extract_info(results, entity)
                extracted_info.append({"Entity": entity, "Extracted Info": extracted})
                st.write(f"### Extracted Info for **{entity}**:")
                st.write(extracted)

# Download Results as CSV
st.markdown("<div class='section-title'>📥 Download Results</div>", unsafe_allow_html=True)

if data is not None:
    csv = pd.DataFrame(extracted_info).to_csv(index=False)
    st.download_button("Download Results as CSV", csv, "extracted_results.csv", "text/csv")

# Footer
st.markdown("<div class='footer'>🌟 Powered by OpenAI, SerpAPI, and Streamlit 🌟</div>", unsafe_allow_html=True)
