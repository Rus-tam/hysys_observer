import win32com.client as win32
import logging

class Connector:
       """
       Класс для подключения к Aspen HYSYS
       """
       def case(file_path):
              file_name = file_path.split('\\')[-1]

              logging.info(f'Инициализирую подключение к расчетному файлу {file_name}')

              try:
                     app = win32.DispatchEx('HYSYS.Application.V14.0')
                     case = app.SimulationCases.Open(file_path)
                     case.Visible = 1
                     logging.info(f'Успешное подключение к расчетному файлу {file_name}')
                     return case
              except:
                     logging.error(f'Все пошло не по плану. Подключение к расчетному файлу {file_name} провалилось')
