from pandas import DataFrame

from src.common_functions import couries_dataset_fun
from resources.config import *
import pandas as pd

class CouriersGenerator:
    def __init__(self, num: int = 10000):
        self.num = num

    def couriers(self):
        data = [couries_dataset_fun.generate_row() for _ in range(self.num)]
        couriers_df: DataFrame = pd.DataFrame(data, columns=couries_columns)

        return couriers_df


def generate_couriers(num: int):
    generator = CouriersGenerator(num=num)
    return generator.couriers
