''' configuration file, contains configuration parameters for
	debugging, testing and deployment
'''
class DebugConfigurations():
    ''' debuging app configuration parameters'''
    FLASK_DEBUG = True
    RESTPLUS_VALIDATE = False
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False
    SQLALCHEMY_DATABASE_URI = "mysql://anonymous@ensembldb.ensembl.org:3306/ensembl_website_90"
    FLASK_TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfigurations():
    ''' testing app configuration parameters'''
    FLASK_DEBUG = False
    RESTPLUS_VALIDATE = False
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False
    SQLALCHEMY_DATABASE_URI = "mysql://anonymous@ensembldb.ensembl.org:3306/ensembl_website_90"
    FLASK_TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DeploymentConfigurations():
    ''' deployment app configuration parameters'''
    FLASK_DEBUG = False
    RESTPLUS_MASK_SWAGGER = True
    RESTPLUS_VALIDATE = True
    RESTPLUS_ERROR_404_HELP = False
    SQLALCHEMY_DATABASE_URI = "mysql://anonymous@ensembldb.ensembl.org:3306/ensembl_website_90"
    FLASK_TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
