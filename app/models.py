from app import db, ma


class SalarySurvey(db.Model):
    __tablename__ = "salary_survey"
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    employment_type = db.Column(db.String)
    company_name = db.Column(db.String)
    company_size = db.Column(db.String)
    primary_location_country = db.Column(db.String)
    primary_location_city = db.Column(db.String)
    industry = db.Column(db.String)
    company_type = db.Column(db.String)
    years_experience_industry = db.Column(db.String)
    years_experience_company = db.Column(db.String)
    job_title = db.Column(db.String)
    job_ladder = db.Column(db.String)
    job_level = db.Column(db.String)
    required_hours_per_week = db.Column(db.String)
    actual_hours_per_week = db.Column(db.String)
    education_level = db.Column(db.String)
    tota_base_salary = db.Column(db.Integer)
    total_bonus = db.Column(db.Integer)
    total_stock_options_equity = db.Column(db.Integer)
    health_insurance_offered = db.Column(db.String)
    annual_vacation_weeks = db.Column(db.String)
    is_happy_at_current_position = db.Column(db.String)
    has_plan_to_resign = db.Column(db.String)
    thoughts_about_industry_direction = db.Column(db.String)
    gender = db.Column(db.String)
    necessary_top_skills = db.Column(db.String)
    has_done_bootcamp = db.Column(db.String)


class SalarySurveySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SalarySurvey
        load_instance = True
        sqla_session = db.session


salary_survey_schema = SalarySurveySchema()
salary_surveys_schema = SalarySurveySchema(many=True)
