from app import api
from app.services import SalarySurveyService

salary_data_parameters = api.parser()

salary_data_parameters.add_argument(
    'limit',
    default=10,
    type=int
)

salary_data_parameters.add_argument(
    'fields', help=f'Which fields to show in output: \n {tuple(SalarySurveyService.SEARCH_FIELDS)}'
)

for key in SalarySurveyService.SEARCH_FIELDS:
    salary_data_parameters.add_argument(key, location='args',)

salary_data_parameters.add_argument(
    'orderBy',
    default='asc',
    choices=('asc', 'desc'),
)

salary_data_parameters.add_argument(
    'sortBy',
    default='timestamp',
    help=f'Which fields to sort: \n {tuple(SalarySurveyService.SEARCH_FIELDS)}'
)
