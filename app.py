from flask import Flask
from routes.user import main as routes_user
from models import db
from models.user import User
from flask_script import Manager
from flask import render_template
from routes.image import main as routes_image

app = Flask(__name__)
manager = Manager(app)



def configure_app():
    db_name = "user_test"
    app.config["SECRET_KEY"] = "secret_key"
    app.config['MONGODB_SETTINGS'] = {
        'db': db_name,
    }
    db.init_app(app)
    register_routes(app)


def configured_app():
    configure_app()
    return app


def register_routes(app):
    app.register_blueprint(routes_user)
    app.register_blueprint(routes_image)

@app.errorhandler(404)
def error404(e):
    return render_template('404.html')


@manager.command
def server():
    print('server run')
    # app = configured_app()
    config = dict(
        debug=True,
        host='',
        port=3000,
    )
    app.run(**config)


if __name__ == "__main__":
    configure_app()
    manager.run()
