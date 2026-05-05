from abc import ABC, abstractmethod


class Unit(ABC):
    """Абстрактный класс юнита"""

    def __init__(self, strength: float, dexterity: float, constitution: float, wisdom: float,
                intelligence: float, charisma: float) -> None:
        
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

    @abstractmethod
    def calculate_max_health(self) -> int:
        """Абстрактный метод вычисления максимального здоровья"""
        pass

    @abstractmethod
    def calculate_damage(self) -> int:
        """Абстрактный метод вычисления базового урона"""
        pass

    @abstractmethod
    def calculate_defense(self) -> int:
        """Абстрактный метод вычисления защиты"""
        pass


class Character(Unit):
    """Класс персонажа"""

    def calculate_max_health(self) -> int:
        """Вычисление максимального здоровья персонажа - телосложение * 10 + сила / 2"""
        return int(self.constitution * 10 + (self.strength / 2))

    def calculate_damage(self) -> int:
        """Вычисление базового урона персонажа - сила * 1.5 + ловкость / 4"""
        return int((self.strength * 1.5) + (self.dexterity / 4))

    def calculate_defense(self) -> int:
        """Вычисление показателя защиты персонажа - телосложение * 1.5 + ловкость / 3"""
        return int((self.constitution * 1.5) + (self.dexterity / 3))


class Monster(Unit):
    """Класс монстра"""

    def calculate_max_health(self) -> int:
        """Вычисление максимального здоровья монстра - телсложение * 8 + сила / 3"""
        return int((self.constitution * 8) + (self.strength / 3)) 

    def calculate_damage(self) -> int:
        """Вычисление базового урона монстра - сила * 2 + телосложение / 5"""
        return int((self.strength * 2) + (self.constitution / 5))

    def calculate_defense(self) -> int:
        """Вычисление показателя защиты монстра - телосложение * 1.2 + сила / 5"""
        return int((self.constitution * 1.2) + (self.strength / 5))