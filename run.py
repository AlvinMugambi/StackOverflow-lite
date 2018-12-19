import os
from app import create_app

config_name = os.getenv("Flask_ENV")
# version1 = Blueprint("apiv1", __name__, url_prefix="/api/v1")

app= create_app(config_name)




if __name__ == '__main__':
        app.run(debug=True)
