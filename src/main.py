import logging
from connector.connector import Connector
from components.stream import Stream
from components.utilities import Utility

file_path = r'C:\Users\Rustam\Documents\python\hysys_observer\example.hsc'

# Настраиваем логирование
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


case = Connector.case(file_path=file_path)

stream = Stream(case=case)

# stream.playground()
comp_molar_frac = stream.get_components_molar_fraction('1', '1')

print(comp_molar_frac)