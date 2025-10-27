from typing import List, Dict
import pandas as pd
import os
import time
from pathlib import Path
import logging

class Writer:
    def __init__(self):
        pass

    @staticmethod
    def merge_dict(data: List[Dict[str, float]]) -> Dict[str, float]:
        """
        Метод для формирования одного словаря из списка словарей
        """
        merged = {}

        for elem in data:
            for key, value in elem.items():
                merged.setdefault(key, []).append(value)
        
        return merged


    @staticmethod
    def write_csv(data: Dict[str, float]):
        """
        Метод, который записывает промежуточный csv файл
        """
        dir_path = Path(__file__).resolve().parents[2]

        data_dir = dir_path / 'data'
        data_dir.mkdir(exist_ok=True)

        df = pd.DataFrame(data)
        current_time = time.time()
        df.to_csv(rf'{data_dir}/{current_time}.csv', index=False)

        logging.info(f'Файл {current_time}.csv записан')

        