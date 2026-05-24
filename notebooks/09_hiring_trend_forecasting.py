# Import Required Libraries

import pandas as pd


# Load Final Engineered Dataset

df = pd.read_csv("../data/cleaned/final_engineered_jobs_dataset.csv", low_memory=False)

print(df.head())


# Convert Posted Date Column

df["posted_date"] = pd.to_datetime(
    df["posted_date"],
    errors="coerce"
)


# Remove Null Dates

df = df.dropna(subset=["posted_date"])


# Use Only Real-Time Portal Data For Trend Analysis

# Kaggle dataset is retained for ML training purposes.
# It is excluded from trend analysis because it contains
# large historical/synthetic records that may distort
# current real-time hiring market trends.

real_time_portals = [
    "Naukri",
    "Foundit",
    "LinkedIn",
    "Indeed"
]

df = df[df["portal_name"].isin(real_time_portals)]

print(df["portal_name"].value_counts())


# Filter Last 3 Months Data

latest_date = df["posted_date"].max()

three_months_back = latest_date - pd.DateOffset(months=3)

df_recent = df[df["posted_date"] >= three_months_back]

print(df_recent.shape)


# Create Monthly Hiring Trend

monthly_jobs = df_recent.groupby(
    df_recent["posted_date"].dt.to_period("M")
).size().reset_index(name="job_count")

monthly_jobs["posted_date"] = monthly_jobs["posted_date"].astype(str)

print(monthly_jobs)


# Find Most Demanded Roles

top_roles = df_recent["standardized_role"].value_counts().reset_index()

top_roles.columns = ["job_role", "job_count"]

print(top_roles.head(10))


# Find Most Demanded Skills

skills = [
    "python_flag",
    "sql_flag",
    "power_bi_flag",
    "tableau_flag",
    "excel_flag",
    "selenium_flag"
]

skill_demand = df_recent[skills].sum().reset_index()

skill_demand.columns = ["skill", "demand_count"]

skill_demand = skill_demand.sort_values(
    by="demand_count",
    ascending=False
)

print(skill_demand)


# Portal Wise Hiring Analysis

portal_trend = df_recent["portal_name"].value_counts().reset_index()

portal_trend.columns = ["portal_name", "job_count"]

print(portal_trend)


# Save Trend Analysis Results

monthly_jobs.to_csv(
    "../data/cleaned/monthly_hiring_trend.csv",
    index=False
)

top_roles.to_csv(
    "../data/cleaned/top_job_roles.csv",
    index=False
)

skill_demand.to_csv(
    "../data/cleaned/skill_demand_analysis.csv",
    index=False
)

portal_trend.to_csv(
    "../data/cleaned/portal_hiring_analysis.csv",
    index=False
)

print("Hiring Trend Analysis Completed Successfully")