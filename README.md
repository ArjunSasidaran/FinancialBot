# Financial Bot
## Overview
Financial Bot is an advanced chatbot designed to assist users in retrieving and analyzing financial data. Leveraging cutting-edge technologies like Streamlit, LangChain, Neo4j, and the OpenAI API, this bot provides real-time financial insights with an interactive interface. It is specifically tailored to extract data from companies' 10K forms, offering users detailed financial metrics and insights.

## Features
- Query Financial Information: Retrieve detailed financial metrics, such as net income, gross margin, and more, extracted directly from companies' 10K forms.
- Real-Time Data Retrieval: Access up-to-date financial data from trusted sources.
- Interactive Interface: Easy-to-use chat interface built with Streamlit.
- Secure Configuration: Utilizes a secrets.toml file to securely store API keys and other sensitive information.

## Technologies Used
- Streamlit: For building the interactive user interface.
- LangChain: For managing complex chains of user inputs and responses.
- Neo4j: As the graph database to store and retrieve financial data.
- OpenAI API: For natural language processing.

## Setup
Clone the repository:

```bash
git clone https://github.com/yourusername/financial-bot.git
```
Navigate to the project directory:

```bash
cd llm-chatbot-python
```
Install the required dependencies:

```bash
pip install -r requirements.txt
```

Set up the secrets.toml file in the .streamlit/ directory with your API keys and database credentials:

```
[api_keys]
openai_api_key = "your-openai-api-key"

[database]
neo4j_uri = "your-neo4j-uri"
neo4j_username = "your-username"
neo4j_password = "your-password"
```
Run the Streamlit app:

```bash
streamlit run bot.py
```
Usage
Once the application is running, interact with the chatbot to query financial information about various companies, such as their net income, gross margin, and other key metrics derived from their 10K forms.

