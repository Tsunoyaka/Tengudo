""" Виды методов """

class MethodTypes:
    class_attr = 'class attr'

    def __init__(self) -> None:
        self.obj_attr = 'obj attr'


    def instance_method(self):
        return self.class_attr, self.obj_attr


    @classmethod
    def class_method(cls):
        print(cls.class_attr)
        # print(cls.obj_attr) # AttributeError


    @staticmethod
    def static_method(x, y):
        print('static method')
        # cls.class_attr # Error
        # self.obj_attr # Error
        return x + y

# obj = MethodTypes()
# print(obj.instance_method())
# obj.class_method()



class User:
    counter = 0

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = self.encrypt_password(password)
        self.counter += 1
        self.add_user()


    @staticmethod
    def encrypt_password(password):
        from hashlib import md5
        en_password = md5(password.encode()).hexdigest()
        return en_password

    @classmethod
    def add_user(cls):
        cls.counter += 1



user1 = User('Scheiber', 'Wolfgang')
print(user1.password)
print(user1.counter)


"""
1. instance method - обязательно принимает self, имеют доступ к атрибутом класса, методам класса, к атрибутам экземпляра

2. classmethod - принимает cls - ссылка на класс - не имеют доступа к атрибутам экземпляра,
   но имеют доступ к актрибутам и методам класса

3. staticmethod - отдельная функция, которая не имеет доступ ни к классу, ни к объекту класса.
   Используется для дополнения функционала класса
"""
