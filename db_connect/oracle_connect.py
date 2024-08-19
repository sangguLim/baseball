import logging
import cx_Oracle

username = 'system'
password = 'system'
dsn = '10.10.10.10/xe'
port = 1521
encoding = 'UTF-8'

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    connection = cx_Oracle.connect(username, password, dsn, encoding=encoding)
except Exception as ex:
    logger.error("ERROR: Could not connect to database.")
    logger.error(ex)
    print('Could not connect to database:', ex)

logger.info("SUCCESS: Connecting database succeeded")

try:
    cursor = connection.cursor()
    sql = "select * from emp"
    cursor.execute(sql)
except Exception as ex:
    logger.error("ERROR: Could not fetch data.")
    logger.error(ex)
    print('Could not fetch data:', ex)

logger.info("SUCCESS: Fetching data succeeded")

rows = cursor.fetchall()
print(rows)

cursor.close()

connection.close()