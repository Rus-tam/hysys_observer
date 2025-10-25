import logging
from connector.connector import Connector
file_path = r'C:\Users\Rustam\Documents\python\hysys_observer\example.hsc'

# Настраиваем логирование
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


case = Connector.case(file_path=file_path)