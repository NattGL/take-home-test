from flask_restx import Resource

from app import api
from app.services import SalarySurveyService
from app.swagger import salary_data_parameters


@api.route('/salary_data')
class SalaryData(Resource):

    @api.response(200, 'Success')
    @api.response(400, 'Bad request')
    @api.response(404, 'Not found')
    @api.response(500, 'Internal Server Error')
    @api.expect(salary_data_parameters)
    def get(self) -> dict:
        return SalarySurveyService.get_data_by_filter(salary_data_parameters.parse_args())
