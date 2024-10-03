from interfaces.antagonist import Antagonist
from interfaces.city import City
from interfaces.media import Media
from interfaces.superhero import Superhero


class Godzilla(Antagonist):
  """Годзилла"""

  def attack(self):
    return "Godzilla stands near a skyscraper"

  def get_name(self):
    return "Godzilla"


class Alien(Antagonist):
  """Инопланетяне"""

  def attack(self):
    return "Aliens abduct cows in the meadow"

  def get_name(self):
    return "Aliens"


class Tokyo(City):
  """Токио"""

  def get_antagonist(self):
    return Godzilla()

  def get_name(self):
    return "Tokyo"


class Kostroma(City):
  """Кострома"""

  def get_antagonist(self):
    return Alien()

  def get_name(self):
    return "Kostroma"


class ChuckNorris(Superhero):
  """Чак Норрис"""

  def attack(self, antagonist: Antagonist):
    return "PIU PIU"

  def get_name(self):
    return "Chuck Norris"


class Newspaper(Media):
  """Газета"""

  def announce(self, superhero: Superhero, city: City, antagonist: Antagonist):
    return f"Today in newspapers: {superhero.get_name()} saved {city.get_name()}!"


class TV(Media):
  """ТВ"""

  def announce(self, superhero: Superhero, city: City, antagonist: Antagonist):
    return f"Watch on the first channel: {superhero.get_name()} saved {city.get_name()}!"

def save_city(superhero: Superhero, city: City, media: Media):
  antagonist = city.get_antagonist()
  print(antagonist.attack())
  print(superhero.attack(antagonist))
  print(media.announce(superhero, city, antagonist))


save_city(ChuckNorris(), Tokyo(), Newspaper())

save_city(ChuckNorris(), Kostroma(), TV())
