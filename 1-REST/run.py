import main.application as main
from configurations import DeploymentConfigurations as configuration

app = main.app

if __name__ == '__main__':
    main.initialize_app(main.app, configuration)
    main.app.run(host='0.0.0.0',debug=configuration.FLASK_DEBUG)

