from abc import ABC, abstractmethod


class Antagonist(ABC):
    """Базовый класс антагониста"""

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def get_name(self):
        """Получаем Имя антагониста"""
        pass
