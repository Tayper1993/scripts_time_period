from abc import ABC, abstractmethod

from interfaces.antagonist import Antagonist
from interfaces.city import City
from interfaces.superhero import Superhero


class Media(ABC):
    """Базовый класс СМИ"""

    @abstractmethod
    def announce(self, superhero: Superhero, city: City, antagonist: Antagonist):
      """Получаем анонс победы"""
      pass
