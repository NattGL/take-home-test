from flask_restx import abort
from sqlalchemy import and_

from app.models import salary_surveys_schema, SalarySurvey, SalarySurveySchema


class SalarySurveyService:
    SEARCH_FIELDS = {
        'timestamp': SalarySurvey.timestamp,
        'employment_type': SalarySurvey.employment_type,
        'company_name': SalarySurvey.company_name,
        'company_size': SalarySurvey.company_size,
        'primary_location_country': SalarySurvey.primary_location_country,
        'primary_location_city': SalarySurvey.primary_location_city,
        'industry': SalarySurvey.industry,
        'company_type': SalarySurvey.company_type,
        'years_experience_industry': SalarySurvey.years_experience_industry,
        'years_experience_company': SalarySurvey.years_experience_company,
        'job_title': SalarySurvey.job_title,
        'job_ladder': SalarySurvey.job_ladder,
        'job_level': SalarySurvey.job_level,
        'required_hours_per_week': SalarySurvey.required_hours_per_week,
        'actual_hours_per_week': SalarySurvey.actual_hours_per_week,
        'education_level': SalarySurvey.education_level,
        'tota_base_salary': SalarySurvey.tota_base_salary,
        'total_bonus': SalarySurvey.total_bonus,
        'total_stock_options_equity': SalarySurvey.total_stock_options_equity,
        'health_insurance_offered': SalarySurvey.health_insurance_offered,
        'annual_vacation_weeks': SalarySurvey.annual_vacation_weeks,
        'is_happy_at_current_position': SalarySurvey.is_happy_at_current_position,
        'has_plan_to_resign': SalarySurvey.has_plan_to_resign,
        'thoughts_about_industry_direction': SalarySurvey.thoughts_about_industry_direction,
        'gender': SalarySurvey.gender,
        'necessary_top_skills': SalarySurvey.necessary_top_skills,
        'has_done_bootcamp': SalarySurvey.has_done_bootcamp,

    }

    @classmethod
    def get_data_by_filter(cls, args: dict):
        query = SalarySurvey.query

        order_by = args.pop('orderBy')
        sort_by = args.pop('sortBy')
        limit = args.pop('limit')
        fields = args.pop('fields')

        query = query.filter(and_(
            *[(cls.SEARCH_FIELDS[field] == search) for field, search in args.items() if search is not None]
        ))

        if sort_by:
            sort_column_list = []
            for column in sort_by.split(','):
                sort_column = cls.SEARCH_FIELDS[column]
                if order_by == 'desc':
                    sort_column = sort_column.desc()
                sort_column_list.append(sort_column)

            query = query.order_by(*sort_column_list)

        data = query.limit(limit).all()

        if data is not None or data != []:
            if fields:
                try:
                    salary_surveys_filtered_schema = SalarySurveySchema(many=True, only=(fields.split(',')))
                except ValueError:
                    abort(400, f"Wrong fields")
                else:
                    return salary_surveys_filtered_schema.dump(data)
            return salary_surveys_schema.dump(data)
        else:
            abort(404, f"Data not found")
