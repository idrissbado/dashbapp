# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 07:12:05 2024

@author: Idriss Olivier BADO
"""

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

class Dashboard:
    def __init__(self, df):
        self.df = df
        self.app = dash.Dash(__name__, external_stylesheets=["https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"])

        # Extract relevant filters (categorical columns only)
        self.filters = self.get_relevant_filters()

    def get_relevant_filters(self):
        """Extract relevant filters from categorical columns."""
        categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns
        filters = {}
        for col in categorical_cols:
            filters[col] = self.df[col].unique()
        return filters

    def calculate_indicators(self, filtered_df):
        """Calculate necessary business indicators."""
        total_transactions = filtered_df['transaction_id'].nunique()
        total_revenue = filtered_df['amount'].sum()
        unique_users = filtered_df['user_id'].nunique()
        avg_transaction_value = filtered_df['amount'].mean()

        return {
            'Total Transactions': total_transactions,
            'Total Revenue': total_revenue,
            'Unique Users': unique_users,
            'Average Transaction Value': avg_transaction_value
        }

    def layout(self):
        """Build the layout for the dashboard with a more professional HTML structure."""
        self.app.layout = html.Div([
            html.Nav([
                html.Div([
                    html.H1("Dashboard", className="navbar-brand")
                ], className="container-fluid")
            ], className="navbar navbar-dark bg-dark mb-4"),
            
            html.Div([
                html.Div([
                    html.Div([
                        html.H2("Filters"),
                        html.Div([
                            html.Div([
                                html.Label(f"Filter by {col}"),
                                dcc.Dropdown(
                                    id=f"{col}-filter",
                                    options=[{'label': val, 'value': val} for val in self.filters[col]],
                                    value=self.filters[col][0],
                                    clearable=False,
                                    className="form-control"
                                )
                            ], className="form-group")
                            for col in self.filters  # Dynamically create dropdowns for each filter
                        ])
                    ], className="card-body")
                ], className="card mb-4")
            ], className="container"),

            html.Div([
                html.Div([
                    html.Div([
                        html.H3("Total Transactions", id="total-transactions"),
                        html.H3("Total Revenue", id="total-revenue"),
                        html.H3("Unique Users", id="unique-users"),
                        html.H3("Average Transaction Value", id="avg-transaction-value")
                    ], className="card-body")
                ], className="card mb-4")
            ], className="container"),

            html.Div([
                dcc.Graph(id="transaction-volume-chart", className="card-body")
            ], className="card container mt-4")
        ], className="bg-light")

    def add_callbacks(self):
        """Define the dashboard's interactivity (callbacks)."""
        inputs = [Input(f"{col}-filter", 'value') for col in self.filters]

        @self.app.callback(
            [Output('total-transactions', 'children'),
             Output('total-revenue', 'children'),
             Output('unique-users', 'children'),
             Output('avg-transaction-value', 'children'),
             Output('transaction-volume-chart', 'figure')],
            inputs
        )
        def update_dashboard(*filter_values):
            # Filter data based on selected filter values
            filtered_df = self.df.copy()
            for i, col in enumerate(self.filters):
                filtered_df = filtered_df[filtered_df[col] == filter_values[i]]

            # Update indicators
            indicators = self.calculate_indicators(filtered_df)

            # Update transaction volume chart
            transaction_chart = px.histogram(
                filtered_df, 
                x='date', 
                y='amount', 
                title="Transaction Volume Over Time"
            )

            return (f"Total Transactions: {indicators['Total Transactions']}",
                    f"Total Revenue: {indicators['Total Revenue']}",
                    f"Unique Users: {indicators['Unique Users']}",
                    f"Average Transaction Value: {indicators['Average Transaction Value']}",
                    transaction_chart)

    def run(self):
        """Run the dashboard."""
        self.layout()
        self.add_callbacks()
        self.app.run_server(debug=True, use_reloader=False)

# Usage
# Load your dataset (replace with actual dataset)
df = pd.read_csv("wave_data.csv")

# Initialize and run the dashboard
dashboard = Dashboard(df)
dashboard.run()
