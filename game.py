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
    """Класс персонажа с игровым классом"""

    def __init__(self, strength: float, dexterity: float, constitution: float, wisdom: float,
                intelligence: float, charisma: float, character_class: str) -> None:
        
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)
        self.character_class = character_class

        if self.character_class not in ("warrior", "hunter", "mage"):
            raise ValueError(f"Класс персонажа {character_class} неверный!")
        
        self.max_health = self.calculate_max_health()
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()

    def calculate_max_health(self) -> int:
        """Вычисление максимального здоровья персонажа - телосложение * 10 + сила / 2"""
        return int(self.constitution * 10 + (self.strength / 2))

    def calculate_damage(self) -> int:
        """Вычисление базового урона персонажа в зависимости от класса"""
        if self.character_class == "warrior":
            return int(self.strength * 2.2 + self.constitution / 3)
        elif self.character_class == "mage":
            return int(self.intelligence * 2.5 + self.wisdom / 2)
        elif self.character_class == "hunter":
            return int(self.dexterity * 1.9 + self.strength / 3)
        else:
            return 0

    def calculate_defense(self) -> int:
        """Вычисление показателя защиты персонажа в зависимости от класса"""
        if self.character_class == "warrior":
            return int(self.constitution * 1.8 + self.strength / 4)
        elif self.character_class == "mage":
            return int(self.wisdom * 1.3 + self.intelligence / 6)
        elif self.character_class == "hunter":
            return int(self.dexterity * 1.6 + self.constitution / 5)
        else:
            return 0