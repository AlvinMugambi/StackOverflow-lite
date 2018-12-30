import os
from app import create_app


# version1 = Blueprint("apiv1", __name__, url_prefix="/api/v1")
config_name = os.getenv('APP_SETTINGS') # config_name = "development"

app = create_app(config_name)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:password@localhost:5432/flask_api"


if __name__ == '__main__':
        app.run()
