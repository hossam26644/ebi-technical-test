from flask import Flask, request
from flask_restplus import Resource, Api, reqparse, fields

from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__) #the main app object
db = SQLAlchemy(app) #the database object
ma = Marshmallow(app) #marshmallow serialization object

app = Flask(__name__)                  #  Create a Flask WSGI application
app.config['RESTPLUS_MASK_SWAGGER'] = False
api = Api(app, doc='/documentation/')                       #  Create a Flask-RESTPlus API
#app.register_blueprint(api, url_prefix='/api/1')
db = SQLAlchemy(app)
#ma = Marshmallow(app)


engine = db.create_engine("mysql://anonymous@ensembldb.ensembl.org:3306/ensembl_website_90",echo = True)
metadata = db.MetaData()
census = db.Table('gene_autocomplete', metadata, autoload=True, autoload_with=engine)

ns_conf = api.namespace('bla', description='Conference operations')


@ns_conf.route('/gene_suggest') 
@api.doc(params={'id': 'An ID'})       #  Create a URL route to this resource
class HelloWorld(Resource):            #  Create a RESTful resource
    def get(self):                     #  Create GET endpoint
        return {'hello': 'HossamWorld'}

pagination = reqparse.RequestParser()
pagination.add_argument('query', type=str, help='Query',default="")
pagination.add_argument('species', type=str, help='Species',required=True)
pagination.add_argument('limit', type=int, help='Limit',required=True)

ResponceBodyModel = api.model('suggestions',{'SuggestedGeneNames':fields.String})

@ns_conf.route('/') 
class Connection(Resource):            #  Create a RESTful resource
	@api.expect(pagination)
	@api.marshal_with(ResponceBodyModel)
	def get(self):
		args = pagination.parse_args()
		query = args.get('query')
		species = args.get('species')
		limit = args.get('limit')
		

		sqlquery = db.select([census.c.stable_id]).where(db.and_(census.c.stable_id.like('ENSAMEG%'),
															  census.c.species == 'ailuropoda_melanoleuca')).limit(10).order_by(census.c.stable_id)
		connection = engine.connect()
		ResultProxy = connection.execute(sqlquery)
		ResultSet = ResultProxy.fetchall()
		print("************")
		print((ResultSet))
		output = []
		
		for x in ResultSet:
		  output.append(x[0]) 

		return {'SuggestedGeneNames':output}


def initialize_app(app):
    ''' initialize app object'''
    app.logger.addHandler(FILE_HANDLER)
    configure_app(app, configuration)
    api.init_app(app)
    api.add_namespace(ns_conf)
				
		


if __name__ == '__main__':
	initialize_app(app)
    app.run(debug=True) 