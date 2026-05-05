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
        self.spells: list[Spell] = []
        self.mana: float = 0

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

    def add_spell(self, spell: Spell) -> None:
        """Добавление заклинания персонажу"""
        self.spells.append(spell)

    def cast_spell(self, index: int) -> str:
        """Вызов заклинания"""
        if index >= len(self.spells) + 1:
            return "Заклинание не найдено!"

        if self.mana >= self.spells[index - 1].mana_cost:
            self.mana -= self.spells[index - 1].mana_cost
            return self.spells[index - 1].cast()
        else:
            return "Маны не хватает!"


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
        self.mana = self.calculate_max_mana()

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
        
    def calculate_max_mana(self) -> int:
        """Вычисление показателя максимальной маны"""
        if self.character_class == "warrior":
            return int(self.intelligence + self.strength / 2)
        elif self.character_class == "mage":
            return int(self.intelligence * 3 + self.wisdom)
        elif self.character_class == "hunter":
            return int(self.dexterity * 1.5 + self.wisdom / 2)
        else:
            return 0


class Spell(ABC):
    """Абстрактный класс заклинаний персонажа"""

    def __init__(self, name: str, damage: float, mana_cost: float) -> None:
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self) -> str:
        """Абстрактный метод эффекта заклинания"""
        pass


class Fireball(Spell):
    """Заклинание Fireball"""

    def __init__(self) -> None:
        super().__init__(name="Fireball", damage=35, mana_cost=15)

    def cast(self) -> str:
        """Эффект заклинания"""
        return f"-35HP"
    

class IceLance(Spell):
    """Заклинание IceLance"""

    def __init__(self) -> None:
        super().__init__(name="IceLance", damage=25, mana_cost=10) 

    def cast(self) -> str:
        """Эффект заклинания"""
        return f"-25HP"
    

class LightningBolt(Spell):
    """Заклинание LightningBolt"""

    def __init__(self) -> None:
        super().__init__(name="LightningBolt", damage=40, mana_cost=20)

    def cast(self) -> str:
        """Эффект заклинания"""
        return f"-40HP"