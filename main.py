import streamlit as st
import pandas as pd
import zipfile
import os

# Title
st.title("Dataset Exploration App")

# Sidebar for uploading ZIP file
st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload a ZIP file containing datasets", type=["zip"])

# Function to extract ZIP file
def extract_zip(zip_file, extract_to="extracted_files"):
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(extract_to)
    return extract_to

if uploaded_file:
    # Extract the uploaded ZIP file
    st.sidebar.success("File uploaded successfully!")
    extract_path = extract_zip(uploaded_file)

    # List extracted files
    files = [f for f in os.listdir(extract_path) if f.endswith(".csv")]
    if files:
        st.sidebar.header("Select a File")
        selected_file = st.sidebar.selectbox("Choose a CSV file", files)

        # Load selected CSV
        file_path = os.path.join(extract_path, selected_file)
        data = pd.read_csv(file_path)

        # Display DataFrame
        st.header(f"Exploring `{selected_file}`")
        st.subheader("Dataset Preview")
        st.write(data.head())

        # Dataset Info
        st.subheader("Basic Information")
        st.write(data.info())

        # Dataset Statistics
        st.subheader("Dataset Statistics")
        st.write(data.describe())

        # Visualization Options
        st.subheader("Visualizations")
        if st.checkbox("Show Column Names"):
            st.write(data.columns.tolist())

        if st.checkbox("Show Missing Values"):
            st.write(data.isnull().sum())
    else:
        st.error("No CSV files found in the ZIP.")
else:
    st.info("Please upload a ZIP file containing datasets.")

