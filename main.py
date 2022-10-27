"""Документация модуля. Основной модуль в проекте.
Выводит все действия и их результаты,
связанные с манипуляциями персонажем игры.
"""

from graphic_arts.start_game_banner import run_screensaver

from random import randint

DEFAULT_ATTACK = 5
DEFAULT_STAMINA = 80
DEFAULT_DEFENCE = 10


class Character:
    # Константа для диапазона очков урона.
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15
    BREIF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, name):
        self.name = name

    # Объявляем метод атаки
    def attack(self):
        # Вместо диапазона записана переменная класса.
        # Оператор * распаковывает передаваемый кортеж.
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный '
                f'{value_attack}')

    # Объявляем метод защиты.
    def defence(self):
        """
        Принимает на вход имя и класс персонажа.
        Возвращает строку сообщения о блокированном персонажем уроне
        в зависимости от его класса.
        """
        value_deffense = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_deffense} ед. урона')

    # Объявляем метод специального умения.
    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        return (f'{self.__class__.__name__} - {self.BREIF_DESC_CHAR_CLASS}')


class Warrior(Character):
    BREIF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'

    def train_desc(self):
        print(f'{self.name}, ты Воитель — отличный боец ближнего боя.')

class Mage(Character):
    BREIF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'

    def train_desc(self):
        print(f'{self.name}, ты Маг — превосходный укротитель стихий.')

class Healer(Character):
    BREIF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'

    def train_desc(self):
        print(f'{self.name}, ты Лекарь — чародей, способный исцелять раны.')

def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

    approve_choice: str = None

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ').lower()
        char_class: Character = game_classes[selected_class](char_name)
        class_brief: str = char_class.__str__()
        print(class_brief)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class

def start_training(character) -> str:
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    commands: dict = {
        'attack': char_class.attack(),
        'defence': char_class.defence(),
        'special': char_class.special()
        }

    char_class.train_desc()
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника '
          'или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ').lower()
        if cmd == 'skip':
            return 'Тренировка окончена.'
        cmd_result = commands[cmd]
        print(cmd_result)
    return 'Тренировка окончена.'

if __name__ == '__main__':
    run_screensaver()
    """Включает внешний модуль оформления начальной заставки."""
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class(char_name)
    print(start_training(char_class))
