from flask import Flask, jsonify
import pandas as pd
import json

app = Flask(__name__)

# Load dataset
df = pd.read_csv("../data/cleaned/final_engineered_jobs_dataset.csv")


# Home Route

@app.route('/')
def home():
    return "India IT Job Market Analytics API Running"


# KPI Summary API

@app.route('/kpi-summary', methods=['GET'])
def kpi_summary():

    total_jobs = int(df['job_title'].count())
    total_companies = int(df['company_name'].nunique())
    total_roles = int(df['standardized_role'].nunique())

    return jsonify({
        "total_job_postings": total_jobs,
        "total_companies": total_companies,
        "total_job_roles": total_roles
    })


# Top Skills API

@app.route('/top-skills', methods=['GET'])
def top_skills():

    skills = {
        "SQL": int(df['sql_flag'].sum()),
        "Python": int(df['python_flag'].sum()),
        "Excel": int(df['excel_flag'].sum()),
        "AWS": int(df['aws_flag'].sum()),
        "Azure": int(df['azure_flag'].sum()),
        "Power BI": int(df['power_bi_flag'].sum()),
        "GCP": int(df['gcp_flag'].sum()),
        "Tableau": int(df['tableau_flag'].sum())
    }

    return app.response_class(
    response=json.dumps(skills, indent=4),
    mimetype='application/json'
)


# Top Roles API

@app.route('/top-roles', methods=['GET'])
def top_roles():

    roles = (
        df['standardized_role']
        .value_counts()
        .head(10)
        .to_dict()
    )

    return jsonify(roles)


# Top Locations API

@app.route('/top-locations', methods=['GET'])
def top_locations():

    locations = (
        df['location']
        .value_counts()
        .head(10)
        .to_dict()
    )

    return jsonify(locations)


# Experience Distribution API

@app.route('/experience-distribution', methods=['GET'])
def experience_distribution():

    experience = (
        df['minimum_experience']
        .value_counts()
        .sort_index()
        .to_dict()
    )

    return jsonify(experience)


# Run Flask App

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)