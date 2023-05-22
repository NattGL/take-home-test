import csv
import sqlite3

import dateutil.parser

from config import BaseConfig


def load_data():
    with open('datasets/salary_survey.csv', 'r', encoding="utf-8") as f:
        dr = csv.DictReader(f, delimiter=",")
        to_db = [
            (
                dateutil.parser.parse(i['Timestamp']).strftime("%Y-%m-%d %H:%M:%S") if i['Timestamp'] else None,
                i['Employment Type'],
                i['Company Name'],
                i['Company Size - # Employees'],
                i['Primary Location (Country)'],
                i['Primary Location (City)'],
                i['Industry in Company'],
                i['Public or Private Company'],
                i['Years Experience in Industry'],
                i['Years of Experience in Current Company  '],
                i['Job Title In Company'],
                i['Job Ladder'],
                i['Job Level'],
                i['Required Hours Per Week'],
                i['Actual Hours Per Week'],
                i['Highest Level of Formal Education Completed'],
                i['Total Base Salary in 2018 (in USD)'] if i['Total Base Salary in 2018 (in USD)'] else None,
                i['Total Bonus in 2018 (cumulative annual value in USD)'] if i['Total Bonus in 2018 (cumulative annual value in USD)'] else None,
                i['Total Stock Options/Equity in 2018 (cumulative annual value in USD)'] if i['Total Stock Options/Equity in 2018 (cumulative annual value in USD)'] else None,
                i['Health Insurance Offered'],
                i['Annual Vacation (in Weeks)'],
                i['Are you happy at your current position?'],
                i['Do you plan to resign in the next 12 months?'],
                i['What are your thoughts about the direction of your industry?'],
                i['Gender'],
                i['Final Question: What are the top skills (you define what that means) that you believe will be necessary for job growth in your industry over the next 10 years?'],
                i['Have you ever done a bootcamp? If so was it worth it?'],
            ) for i in dr]

    conn = sqlite3.connect(BaseConfig.DATABASE_NAME)
    cur = conn.cursor()
    cur.executemany("INSERT INTO salary_survey (timestamp, "
                    "employment_type, "
                    "company_name,"
                    "company_size,"
                    "primary_location_country,"
                    "primary_location_city,"
                    "industry,"
                    "company_type,"
                    "years_experience_industry,"
                    "years_experience_company,"
                    "job_title,"
                    "job_ladder,"
                    "job_level,"
                    "required_hours_per_week,"
                    "actual_hours_per_week,"
                    "education_level,"
                    "tota_base_salary,"
                    "total_bonus,"
                    "total_stock_options_equity,"
                    "health_insurance_offered,"
                    "annual_vacation_weeks,"
                    "is_happy_at_current_position,"
                    "has_plan_to_resign,"
                    "thoughts_about_industry_direction,"
                    "gender,"
                    "necessary_top_skills,"
                    "has_done_bootcamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()
    conn.close()
