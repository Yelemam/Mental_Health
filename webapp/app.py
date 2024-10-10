# Import necessary libraries
from flask import Flask, render_template, request, send_from_directory
import pandas as pd
import plotly.express as px
import os

# Initialize Flask application
app = Flask(__name__)

# Load the dataset from the data folder
# This section reads the CSV file and loads it into a DataFrame
data_file_path = os.path.join(os.path.dirname(__file__), 'data', 'cleaned_mental_health_data.csv')
data = pd.read_csv(data_file_path)

# --------------------------------------
# Landing Page Route
# Displays the welcome page with navigation buttons to other sections
# --------------------------------------
@app.route('/')
def landing_page():
    return render_template('index.html')

# --------------------------------------
# Data Table Route
# Displays the data table and allows filtering by Gender
# --------------------------------------
@app.route('/data', methods=['GET', 'POST'])
def data_table():
    # Retrieve filter values from the form and apply them to the data table
    gender_filter = request.form.get('gender_filter', 'all')
    self_employed_filter = request.form.get('self_employed_filter', 'all')
    treatment_filter = request.form.get('treatment_filter', 'all')

    # Start with the full dataset and filter down based on the criteria
    filtered_data = data
    if gender_filter != 'all':
        filtered_data = filtered_data[filtered_data['Gender'] == gender_filter]
    if self_employed_filter != 'all':
        filtered_data = filtered_data[filtered_data['self_employed'] == self_employed_filter]
    if treatment_filter != 'all':
        filtered_data = filtered_data[filtered_data['treatment'] == treatment_filter]

    data_sample = filtered_data.head(10).to_html(classes='data', header="true")
    return render_template('data_table.html', data=data_sample)
# --------------------------------------
# Gender Analysis Route
# Displays the gender analysis visualization with a filter for Gender
# --------------------------------------
@app.route('/gender-analysis', methods=['GET', 'POST'])
def gender_analysis():
    # Retrieve filter value from the form and apply it to the gender data
    gender_filter = request.form.get('gender_filter', 'all')
    filtered_data_gender = data if gender_filter == 'all' else data[data['Gender'] == gender_filter]
    
    # Create gender analysis chart using Plotly
    gender_counts = filtered_data_gender['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']
    gender_chart = px.bar(gender_counts, 
                          x='Gender', y='Count',
                          labels={'Gender': 'Gender', 'Count': 'Number of Respondents'},
                          title='Respondents by Gender')
    gender_chart_html = gender_chart.to_html(full_html=False)
    
    return render_template('gender_analysis.html', gender_chart=gender_chart_html)

# --------------------------------------
# Self-Employment Analysis Route
# Displays the self-employment analysis visualization with a filter for Self-Employment Status
# --------------------------------------
@app.route('/self-employment-analysis', methods=['GET', 'POST'])
def self_employment_analysis():
    # Retrieve filter value from the form and apply it to the self-employment data
    employment_filter = request.form.get('employment_filter', 'all')
    filtered_data_employment = data if employment_filter == 'all' else data[data['self_employed'] == employment_filter]
    
    # Create self-employment analysis chart using Plotly
    self_employment_counts = filtered_data_employment.groupby(['self_employed', 'treatment']).size().reset_index(name='Count')
    self_employment_chart = px.bar(self_employment_counts, 
                                   x='self_employed', y='Count', color='treatment',
                                   labels={'self_employed': 'Self-Employed', 'Count': 'Number of Respondents'},
                                   title='Mental Health Treatment among Self-Employed Individuals')
    self_employment_chart_html = self_employment_chart.to_html(full_html=False)
    
    return render_template('self_employment_analysis.html', self_employment_chart=self_employment_chart_html)
# --------------------------------------
# Run the Flask Application
# Starts the Flask web server with debug mode enabled
# --------------------------------------
if __name__ == '__main__':
    app.run(debug=True)