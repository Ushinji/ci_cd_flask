import os
from app.config import BaseConfig

user = os.getenv('MYSQL_USER', '')
host = os.getenv('MYSQL_HOST', '')
password = os.getenv('MYSQL_PASSWORD', '')


class Config(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f'mysql://{user}:{password}@{host}:3306/ci_cd_flask_test?charset=utf8mb4'
