class Tree:
    def __init__(self, height, age, species):
        """
        >>> Tree(5, 10, "Oak")
        >>> Tree(-1, 10, "Oak")
        Traceback (most recent call last):
        ValueError: Высота дерева должна быть положительной.
        """
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительной.")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")
        if not species:
            raise ValueError("Название породы дерева не может быть пустым.")

        self.height = height
        self.age = age
        self.species = species

    def photosynthesize(self):
        return f"{self.species} производит кислород."

    def grow(self, years):
        if years <= 0:
            raise ValueError("Количество лет должно быть положительным.")
        self.age += years
        self.height += years * 0.5
        return f"Дерево выросло на {years * 0.5} метров."


class Vehicle:
    def __init__(self, brand, model, year):
        """
        >>> Vehicle("Toyota", "Corolla", 2020)
        >>> Vehicle("", "Corolla", 2020)
        Traceback (most recent call last):
        ValueError: Марка не может быть пустой.
        """
        if not brand:
            raise ValueError("Марка не может быть пустой.")
        if not model:
            raise ValueError("Модель не может быть пустой.")
        if year <= 0:
            raise ValueError("Год выпуска должен быть положительным.")

        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return f"Двигатель {self.brand} {self.model} запущен."

    def stop_engine(self):
        return f"Двигатель {self.brand} {self.model} заглушен."


class SocialNetwork:
    def __init__(self, name, users):
        """
        >>> SocialNetwork("Facebook", 1000000)
        >>> SocialNetwork("", 1000000)
        Traceback (most recent call last):
        ValueError: Название соцсети не может быть пустым.
        """
        if not name:
            raise ValueError("Название соцсети не может быть пустым.")
        if users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")

        self.name = name
        self.users = users

    def register_user(self, username):
        if not username:
            raise ValueError("Имя пользователя не может быть пустым.")
        self.users += 1
        return f"Пользователь {username} зарегистрирован в {self.name}."

    def post_message(self, username, message):
        if not username or not message:
            raise ValueError("Имя пользователя и сообщение не могут быть пустыми.")
        return f"{username} опубликовал сообщение: {message}"

    def delete_account(self, username):
        if not username:
            raise ValueError("Имя пользователя не может быть пустым.")
        self.users -= 1
        return f"Аккаунт {username} удален из {self.name}."
