from abc import ABC
import json


class WorkToFile(ABC):
    """Абстрактный класс для работы с файлами"""

    @staticmethod
    def read():
        pass

    @staticmethod
    def write():
        pass
