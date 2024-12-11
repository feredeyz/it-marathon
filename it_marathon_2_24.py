class Blum:
    '''
        Познакомтесь с феечкой Блум!
        Она - душа компании. Дополняет любую компанию и делает её лучше.
        Её задача - добавить первую цифру введённого числа в его конец.
    '''
    def __init__(self, name: str, number: int):
        self.name: str = name
        self.number: int = number

    def __str__(self):
        return f"Привет! Я феечка Винкс! Моё имя {self.name}!"

    def to_end(self):
        return str(self.number) + str(self.number)[0]

class Stella:
    '''
        Познакомтесь с феечкой Стэлла!
        Она - главный персонаж в своей жизни. Она может разом перевернуть ход событий.
        Её задача - развернуть ваше число.
    '''
    def __init__(self, name: str, number: int):
        self.name: str = name
        self.number: int = number

    def __str__(self):
        return f"Привет! Я феечка Винкс! Моё имя {self.name}!"

    def reverse_number(self):
        return str(self.number)[::-1]

class Leyla:
    '''
        Познакомтесь с феечкой Лэйла!
        Она очень суетливая, поэтому часто не может определиться с порядком вещей.
        Её задача - заменить цифры в введёном числе на соответствующие им символы.
    '''
    def __init__(self, name: str, number: int):
        self.name: str = name
        self.number: int = number
        self.replacements: dict = {
            "0": "0",
            "1": "I",
            "2": "Z",
            "3": "E",
            "4": "!",
            "5": "S",
            "6": "b",
            "7": "J",
            "8": "#",
            "9": "P",
        }

    def __str__(self):
        return f"Привет! Я феечка Винкс! Моё имя {self.name}!"

    def replace(self):
        self.number = str(self.number)
        result = ''
        for number in self.number:
            result += self.replacements[number]
        return result

class Flora:
    '''
        Познакомтесь с феечкой Флора!
        Она очень строгая и любит порядок во всём!
        Её задача - проверять введёное число.
    '''
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number

    def __str__(self):
        return f"Привет! Я феечка Винкс! Моё имя {self.name}!"

    def check(self):
        return False if len(str(self.number)) != 7 else True


def lol():
    number: int = int(input())

    flora: Flora = Flora("Флора", number)
    if not flora.check():
        return "WRONG"
    
    blum: Blum = Blum('Блум', number)
    number: int = int(blum.to_end())

    stella: Stella = Stella("Стелла", number)
    number: int = int(stella.reverse_number())

    leyla: Leyla = Leyla("Лэйла", number)
    number: str = leyla.replace()
    return number

def main():
    joke = False
    if joke:
        print(lol())
    else:
        print(normal())

def normal():
    n = str(int(input()))
    if len(n) != 7:
        return "WRONG"
    n = (n + n[0])[::-1]
    replacements: dict = {
            "0": "0",
            "1": "I",
            "2": "Z",
            "3": "E",
            "4": "!",
            "5": "S",
            "6": "b",
            "7": "J",
            "8": "#",
            "9": "P",
        }
    return ''.join([replacements[i] for i in n])
    

if __name__ == "__main__":
    main()

