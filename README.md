# dashbapp
Dashboard for Business Indicators
This Python project uses the Dash framework to create an interactive and visually appealing dashboard for analyzing business transactions. The dashboard allows for real-time data filtering, indicator calculation, and data visualization.

Overview
The Dashboard class provides a professional and intuitive interface for business users to gain insights into transaction data. It dynamically extracts relevant filters from categorical columns, computes business indicators, and displays them in a structured layout. Users can interactively filter data and view changes in metrics such as:

Total Transactions: The count of unique transactions.
Total Revenue: The sum of all transaction amounts.
Unique Users: The number of distinct users involved in transactions.
Average Transaction Value: The mean value of transactions.
Additionally, the dashboard includes a transaction volume chart that visually represents the data over time.

Features
Dynamic Filtering: Automatically generates dropdown filters for categorical columns.
Indicator Calculation: Computes key metrics like revenue, user count, and transaction averages.
Interactive Visualization: Uses Plotly for an engaging graphical representation of data.
Bootstrap Styling: Incorporates a clean and responsive layout using Bootstrap.
Installation
Clone the repository:


Copier le code
git clone https://github.com/idrissbado/dashbapp.git
Install the necessary packages:


pip install -r requirements.txt
Make sure you have your data file (e.g., wave_data.csv) in the project directory.

Usage
Load your dataset and initialize the dashboard:

python

import pandas as pd
from dashboard import Dashboard

df = pd.read_csv("wave_data.csv")
dashboard = Dashboard(df)
dashboard.run()
Open your browser to view the dashboard at http://127.0.0.1:8050/.

Requirements
Python 3.7+
Dash
Plotly
Pandas
Author
Idriss Olivier BADO
Data Evangelist at Bizao
License
This project is licensed under the MIT License.
