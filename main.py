from app import app
from app.app_config.config import SERVER_PORT

if __name__ == "__main__":
	app.run(host = '127.0.0.1', debug = True, port=SERVER_PORT)