from app import create_app
# from config import config


# version1 = Blueprint("apiv1", __name__, url_prefix="/api/v1")

app= create_app()


if __name__ == '__main__':
        app.run(debug=True)
