import os
from app.config import BaseConfig

password = os.getenv('MYSQL_PASSWORD', '')


class Config(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f'mysql://root:{password}@db:3306/ci_cd_flask_development?charset=utf8mb4'
