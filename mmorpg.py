class Character:
    def __init__(self, level: int):
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

    def attack(self, *, target: "Character") -> None:
        target.got_damage(damage = self.attack_power)
        print(f"{self.character_name} attacks {target.character_name} with attack {self.attack_power} power!")
        print(f"{self.character_name} hp: {self.health_points}  \'{self.health_points_percent()}%\'")
        print(f"{target.character_name} hp: {target.health_points}  \'{target.health_points_percent()}%\'")


    def got_damage(self, *, damage: int) -> None:
        damage = damage * (100 - self.defence) / 100
        damage = round(damage)
        self.health_points -= damage

    @property
    def defence(self) -> int:
        defence = self.base_defence * self.level
        return defence

    @property
    def max_health_points(self) -> int:
        return self.base_health_points * self.level

    def health_points_percent(self) -> float:
        return  round(self.health_points / self.max_health_points * 100, 1)


    def __str__(self):
        return f"Тип: {self.character_name}, очки жизни {self.health_points}, урон: {self.attack_power}"

    def is_alive(self) -> bool:
        return self.health_points > 0

class Ork(Character):
    base_health_points= 300
    base_attack_power = 20
    character_name = "Ork"
    base_defence = 15

    @property
    def defence(self) -> int:
        defence = super().defence
        if self.health_points <= 50:
            defence *= 3
        return defence

class Elf(Character):
    base_health_points = 200
    base_attack_power= 30
    character_name = "Elf"
    base_defence = 10

    def attack(self, *, target: "Character") -> None:
        if target.health_points_percent() <= 30:
            attack_power = self.attack_power * 3
            print(f"Elf attack_power: {attack_power}")
        else:
            attack_power = self.attack_power

        target.got_damage(damage=attack_power)
        print(f"{self.character_name} attacks {target.character_name} with attack {attack_power} power!")
        print(f"{self.character_name} hp: {self.health_points}  '{self.health_points_percent()}%'")
        print(f"{target.character_name} hp: {target.health_points}  '{target.health_points_percent()}%'")

def fight(character_1: Character, character_2: Character) -> None:
    while character_1.is_alive() and character_2.is_alive():
        character_1.attack(target = character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)

ork1 = Ork(level=1)
elf1 = Elf(level=1)

fight(character_1=ork1, character_2=elf1)

#fight(character_1=ork1, character_2=elf1)