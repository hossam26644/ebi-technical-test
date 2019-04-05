''' Main file, run to start service '''
from logging import FileHandler, WARNING

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from apis.api import api
from configurations import DeploymentConfigurations as configuration

#main elements
app = Flask(__name__) #the main app object
db = SQLAlchemy(app) #the database object
ma = Marshmallow(app) #marshmallow serialization object
FILE_HANDLER = FileHandler('errorlogs.txt') #file handler for logging
FILE_HANDLER.setLevel(WARNING)


def configure_app(app, configuration):
    ''' config app from confiuration file '''
    app.config['SQLALCHEMY_DATABASE_URI'] = configuration.SQLALCHEMY_DATABASE_URI
    app.config['RESTPLUS_VALIDATE'] = configuration.RESTPLUS_VALIDATE
    app.config['RESTPLUS_MASK_SWAGGER'] = configuration.RESTPLUS_MASK_SWAGGER
    app.config['ERROR_404_HELP'] = configuration.RESTPLUS_ERROR_404_HELP
    app.config['TESTING'] = configuration.FLASK_TESTING
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = configuration.SQLALCHEMY_TRACK_MODIFICATIONS

def initialize_app(app, configuration):
    ''' initialize app object'''
    #get name space, TODO// relocate to import list
    from namespaces.gene_operations import gene_operations_namespace
    app.logger.addHandler(FILE_HANDLER)
    configure_app(app, configuration)
    api.init_app(app)
    api.add_namespace(gene_operations_namespace)

if __name__ == '__main__':
    initialize_app(app, configuration)
    app.run(host='0.0.0.0',debug=configuration.FLASK_DEBUG)

