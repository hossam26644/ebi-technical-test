''' Api module '''
from flask_restplus import Api

#create api
api = Api(title='gene_suggest service', version='1.0',
          description='Responds with a list of suggested \
          gene names for the given query and target species.')

@api.errorhandler
def internal_server_error_exception(error):
    ''' internal server error exeption '''
    message = 'An unhandled exception occurred.'
    return {'message': message}, 500
    