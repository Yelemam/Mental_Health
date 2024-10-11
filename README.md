# Mental_Health_Project3
# Mental Health Data Engineering Project

![mental_health_bg](https://github.com/user-attachments/assets/3be7e3c1-3890-4428-a655-3d48fe6a3262)

# Table of Contents

    1.    Project Overview
    2.    Folder Structure Explanation
    3.    Data Sources
    4.    Database Creation Process
    5.    ETL Workflow
    6.    Exploratory Data Analysis (EDA)
    7.    Flask Web Application
    8.    Tools and Technologies
    9.    Challenges and Solutions
    10.    Future Enhancements
    11.    Ethical Considerations
    12.    Contributors
    13.    Acknowledgments

# Project Overview

TThe Mental Health Data Engineering project focuses on using data engineering techniques to analyze mental health data with the goal of uncovering 
trends, correlations, and insights. While we work with the data to understand mental health patterns, our primary emphasis is on the data engineering process itself.

# Folder Structure Explanation

    •    data/: Contains raw and cleaned datasets used for analysis and visualization.
    •    database/: Includes the SQL schema and scripts for database creation and management.
    •    notebooks/: Jupyter Notebooks used for data cleaning, transformation, and exploratory data analysis.
    •    webapp/: Contains the Flask web application files, including app.py, HTML templates, and static files (CSS, images).
    •    static/: Sub-directory within webapp that holds static resources like stylesheets and images.
    •    templates/: Sub-directory within webapp that contains HTML templates for the Flask app.
    •    README.md: This document provides an overview of the project and its components.

# Data Sources

    •    Kaggle Dataset: Used for obtaining a variety of mental health data. https://www.kaggle.com/datasets/bhavikjikadara/mental-health-dataset?resource=download
    •    Data was pre-processed to ensure consistency and relevance for the analysis.

# Database Creation Process

    •    The database was initially created using direct imports from Jupyter Notebook 3. The transformed data was loaded directly into the database.
    •    Following the data import, the database tables were altered to include primary keys (PK) and foreign keys (FK) to establish relationships and enhance data integrity.
    •    The database design adheres to standard normalization principles, ensuring optimized storage and efficient querying.

# ETL Workflow

    •    Extraction: Data was extracted from CSV file from Kaggle. https://www.kaggle.com/datasets/bhavikjikadara/mental-health-dataset?resource=download
    •    Transformation: Data cleaning and transformation processes were conducted to handle missing values, normalize formats, and prepare the data for analysis.
    •    Load: The processed data was loaded into a PostgreSQL database, with tables linked by PKs and FKs to support robust data analysis.
    •    Visualization: An ERD (Entity-Relationship Diagram) was created to visually represent the database schema and table relationships.

![ERD](https://github.com/user-attachments/assets/6153ca25-bd94-45f6-9972-4b44cbe4e8df)


# Exploratory Data Analysis (EDA)

    •    Detailed analysis was performed using Jupyter Notebooks to explore the data and identify key trends.
    •    Visualizations were created to highlight correlations between different variables, such as gender, treatment, and self-employment status.
    •    The EDA provided insights into the factors influencing mental health, guiding the development of targeted visualizations in the web app.

![gender_distribution](https://github.com/user-attachments/assets/1e4d7809-0429-434a-b12c-8d8be800ff81)

![treatment_by_country](https://github.com/user-attachments/assets/fc1e6b8b-d079-4531-b189-762a5f711475)


# Flask Web Application

    •    The Flask web application serves as an interactive interface for users to engage with the data.
    •    Features:
         •    Data Table: Allows users to filter and explore data dynamically.
         •    Interactive Charts: Displays visualizations of mental health trends, with filtering options for deeper insights.
         •    Responsive Design: Ensures that the app is accessible across different devices.
         •    Integration: The web app integrates seamlessly with the database, enabling real-time data interaction and visualization.


# Tools and Technologies

    •    Python & Jupyter Notebooks: Used for data analysis, ETL, and exploratory data analysis.
    •    PostgreSQL: The database platform used to store and manage the data.
    •    Flask: Web framework used to create the interactive web application.
    •    Plotly: Library used for creating dynamic charts and visualizations.
    •    SQLAlchemy: For database operations and handling queries in the web app.

# Challenges and Solutions

    •    Static File Serving: Encountered issues with serving static files in Flask, which were resolved by explicitly setting the static file path.
    •    Data Cleaning: Addressed challenges related to inconsistent data formats and missing values during the transformation phase.
    •    Database Optimization: Implemented table normalization and indexing to improve query performance and data retrieval speed.

# Future Enhancements

    •    Machine Learning Integration: Plan to include predictive models to identify trends in mental health conditions.
    •    Extended Data Sources: Explore additional datasets to enrich the analysis and provide more comprehensive insights.
    •    Enhanced Visualizations: Add more interactive charts and filters to enable deeper exploration of the data.

# Ethical Considerations

    •    Data Privacy: Care was taken to ensure that any sensitive information was anonymized to protect individual privacy.
    •    Transparency: All data sources and analysis methods are documented to maintain transparency and reproducibility.
    •    Ethical guidelines were followed to ensure that data is used responsibly and respectfully in understanding mental health.

# Contributors

    •    Yara El-Emam
    •    Michael Rhee
    •    Abigail Serpa
    •    Muad Rashid

# Acknowledgments

    •    Instructors and Mentors: Special thanks to our instructors and mentors who provided guidance and valuable feedback throughout the project.
    •    Kaggle: For providing access to the dataset used in this analysis, which formed the foundation of our project.
    •    AI Tools and Assistance: We utilized AI tools to assist with debugging, integrating new libraries, and setting up connections between Jupyter Notebook and PostgreSQL, which greatly enhanced our productivity and problem-solving capabilities.
