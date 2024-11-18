AI Agent Dashboard
📜 Project Description
The AI Agent Dashboard is a streamlined web-based solution designed to simplify data processing, automate web searches, and derive actionable insights using artificial intelligence. Built with Streamlit, it enables users to process data from CSV files, perform dynamic web queries through SerpAPI, and extract meaningful insights using OpenAI models. Integration with Google Sheets enhances data synchronization and accessibility.

⚙️ Setup Instructions
Step 1: Clone or Download the Repository
Visit the project repository on GitHub.
Click Code → Download ZIP to get the files, or use Git to clone:
bash
Copy code
git clone <repository-url>
Step 2: Install Dependencies
Ensure Python 3.7+ is installed on your machine.
Open a terminal in the project directory.
Install the required libraries with:
bash
Copy code
pip install -r requirements.txt
Step 3: Run the Application
Start the Streamlit server with the following command:
bash
Copy code
streamlit run dashboard.py
Access the app in your web browser using the URL displayed in the terminal.
🧭 Usage Guide
1. Upload a CSV File
Navigate to the Upload Your CSV File section in the dashboard.
Upload a CSV file containing the data you want to process.
Preview the file and select the relevant column to process.
2. Connect to Google Sheets
Upload your Google API JSON key to connect the dashboard to Google Sheets.
Upon successful upload, the system synchronizes data dynamically.
3. Perform Web Search
Enter a search query template using {entity} as a placeholder (e.g., News about {entity}).
Click Search to retrieve search results for entities from the selected column.
4. Extract Insights
Extract relevant information from search results using OpenAI models.
Insights will be displayed for each entity in a structured format.
5. Download Results
Download the processed and extracted data as a CSV file for further use.
🔑 API Key Setup
Google Sheets API
Visit the Google Cloud Console.
Create a project and enable the Google Sheets API.
Generate Service Account credentials and download the JSON file.
Upload this file in the Google Sheets Integration section of the dashboard.
SerpAPI
Sign up at SerpAPI.
Locate your API key on the account dashboard.
Replace "your_serpapi_key" in the code with your actual SerpAPI key.
OpenAI API
Sign up at OpenAI.
Generate an API key from the dashboard.
Store it as an environment variable using:
bash
Copy code
export OPENAI_API_KEY="your_openai_key"
✨ Optional Features
Customizable Queries: Use {entity} placeholders for dynamic search queries.
Dynamic Styling: A sleek user interface with intuitive design and custom themes.
Google Sheets Sync: Effortlessly integrate and update data with Google Sheets.
