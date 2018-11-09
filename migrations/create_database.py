import os
from sqlalchemy import create_engine


mysql_user = os.getenv('MYSQL_USER', '')
mysql_host = os.getenv('MYSQL_HOST', '')
mysql_password = os.getenv('MYSQL_PASSWORD', '')
mysql_engine = create_engine(f'mysql://{mysql_user}:{mysql_password}@{mysql_host}:3306')

# Create Database for development if it did not exist
db_name_for_development = 'ci_cd_flask_development'
existing_databases = mysql_engine.execute("SHOW DATABASES;")
if db_name_for_development not in [d[0] for d in existing_databases]:
    mysql_engine.execute(
        f'''CREATE DATABASE {db_name_for_development}
            DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;''')
    print("Created database : {0}".format(db_name_for_development))


# Create Database for test if it did not exist
db_name_for_test = 'ci_cd_flask_test'
existing_databases = mysql_engine.execute("SHOW DATABASES;")
if db_name_for_test not in [d[0] for d in existing_databases]:
    mysql_engine.execute(
        f'''CREATE DATABASE {db_name_for_test}
            DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;''')
    print("Created database : {0}".format(db_name_for_test))
