import logging
from connector.connector import Connector
from components.stream import Stream
from components.writer import Writer
from components.utilities import Utility
import pandas as pd

file_path = r'C:\Users\Rustam\Documents\python\hysys_observer\example.hsc'

# Настраиваем логирование
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s\n"
)


# case = Connector.case(file_path=file_path)

# stream = Stream(case=case)

data = {}
a = [
    {'1': 1.0, '2': 2.0, '3': 3.0, '4': 4.0},
    {'1': 5.0, '2': 6.0, '3': 7.0, '4': 8.0},
    {'1': 9.0, '2': 10.0, '3': 11.0, '4': 12.0},
    {'1': 13.0, '2': 14.0, '3': 15.0, '4': 16.0}
]


