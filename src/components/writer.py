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
        result = {}
        for elem in data:
            result |= elem
        
        return result


    @staticmethod
    def write_csv(data: Dict[str, float]):
        dir_path = Path(__file__).resolve().parents[2]

        data_dir = dir_path / 'data'
        data_dir.mkdir(exist_ok=True)

        df = pd.DataFrame(data, index=[0])
        current_time = time.time()
        df.to_csv(rf'{data_dir}/{current_time}.csv', index=False)

        logging.info(f'Файл {current_time}.csv записан')

        