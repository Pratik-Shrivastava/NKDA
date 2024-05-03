import urllib.parse
import logging
import os
from datetime import date

SERVER_PORT: str = os.environ.get('SERVER_PORT', '5000')

POSTGRES: dict = {
    'user': os.environ.get('POSTGRES_USER', 'postgres'),
    'db': os.environ.get('POSTGRES_DB', 'nkda-db'),
    'host': os.environ.get('POSTGRES_HOST', '127.0.0.1'),
    'password': urllib.parse.quote(os.environ.get('POSTGRES_PASSWORD', '2580')),
    'port': os.environ.get('POSTGRES_PORT', '5432')
}
DB_URI: str = 'postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(db)s' % POSTGRES
POSTGRES_DATE_FORMAT: str = '%Y-%m-%d'
POSTGRES_DT_FORMAT: str = '%Y-%m-%dT%H:%M:%S'

JWT_SECRET_KEY: str = os.environ.get('JWT_SECRET_KEY', 'f3bca1544d308741c9240f3b6ced1067513ce1351c9fd3971fdafbfe68fffc82')

LOGGER_PATH: str = os.environ.get('LOGGER_PATH', 'D:/WEBSOFTTECHS/nkda-backend/logs/')


def get_logger(__name__: str) -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    file_handler = logging.FileHandler(f'{LOGGER_PATH}log-{date.today()}.log')
    
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
