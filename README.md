# Job Posting Analytics and Recruitment Market Analysis

## Project Overview

This project focuses on collecting, cleaning, analyzing, and visualizing real-time job posting data from multiple job portals to understand current recruitment trends, in-demand skills, hiring locations, salary patterns, and market behavior across the IT industry.

The project combines web scraping, data preprocessing, SQL analysis, exploratory data analysis (EDA), and dashboard visualization to generate actionable insights from recruitment data.

---

## Objectives

- Collect job posting data from multiple job portals
- Analyze hiring trends across roles and locations
- Identify high-demand technical skills
- Study salary and experience requirements
- Compare recruitment patterns between portals
- Build a structured analytics workflow using Python and SQL

---

## Data Sources

Data was collected from multiple job portals including:

- LinkedIn
- Naukri
- Indeed
- Glassdoor
- VCS Job Portal

> Note: VCS Job Portal contributed a limited number of records during the data collection window due to lower active listings compared to other portals.

---

## Technologies Used

### Programming & Analysis
- Python
- SQL (MySQL)

### Python Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Selenium
- BeautifulSoup
- Requests

### Database
- MySQL

### Visualization
- Power BI

### Development Environment
- Jupyter Notebook
- VS Code

---

## Project Workflow

### 1. Data Collection
- Collected real-time job posting data from multiple portals
- Used Selenium and BeautifulSoup for scraping dynamic and static content
- Extracted job title, company, location, skills, salary, experience, and posting details

### 2. Data Cleaning
- Removed duplicates
- Standardized columns and formats
- Handled missing values
- Normalized skill and location names

### 3. Database Integration
- Imported cleaned data into MySQL
- Performed SQL-based transformations and analysis

### 4. Exploratory Data Analysis
- Skill demand analysis
- Location-wise hiring trends
- Experience-level distribution
- Salary trend analysis
- Company hiring patterns

### 5. Dashboard & Visualization
- Created interactive Power BI dashboards
- Built charts for recruitment trends and skill demand analysis

---

## Key Insights

- Python, SQL, Selenium, Power BI, and Java are among the most demanded skills
- Bengaluru, Hyderabad, Chennai, and Pune showed high recruitment activity
- Mid-level experience roles dominated the hiring market
- Different portals showed varying concentrations of job categories and salary visibility
- Data Analyst, Automation Testing, and Software Development roles showed consistent demand

---

## Folder Structure

```bash
project/
│
├── data/
│   └── cleaned/
│
├── notebooks/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Future Enhancements

- Real-time automated data pipelines
- Advanced NLP-based skill extraction
- Predictive hiring trend analysis
- Streamlit-based deployment
- AI-driven job recommendation system

---

## Author

Monisha M