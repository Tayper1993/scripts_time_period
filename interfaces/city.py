from abc import ABC, abstractmethod


class City(ABC):
    """Базовый класс города"""

    @abstractmethod
    def get_antagonist(self):
        """Получаем антагониста"""
        pass

    @abstractmethod
    def get_name(self):
        """Получаем имя города"""
        pass
