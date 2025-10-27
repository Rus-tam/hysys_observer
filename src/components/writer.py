from typing import List, Dict

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
    def write_csv(data: dict):
        pass