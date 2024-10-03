from abc import ABC, abstractmethod

from interfaces.antagonist import Antagonist


class Superhero(ABC):
  """Базовый класс супергероя"""

  @abstractmethod
  def attack(self, antagonist: Antagonist):
    """Атака супергероя"""
    pass

  @abstractmethod
  def get_name(self):
    """Получаем имя супергероя"""
    pass
