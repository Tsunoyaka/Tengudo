"""

CRUD - Cread Read Update Delete

DataBase

Terminal View

UX - add Email and Message (CRUD)

"""

from email import message
import email
from multiprocessing.connection import answer_challenge


DataBase: dict = dict()

_id = 0


def get_data_or_error(DataBase: dict, id: int) -> dict:
    try:
        object_ = DataBase[id]
    except KeyError as e:
        raise ValueError("Такого индекса не существует!!!")
    else:
        print(object_)

def create_data(email: str, message: str):
    """
    add object in DataBase
    """

    global _id

    obj = {
        "email": email,
        "message": message
    }
    DataBase[_id] = obj
    
    
    _id += 1

def show_database(flag:bool=False, *args, **kwargs) -> None:
    """
    show all data in DataBase
    """
    if args:
        for obj in args:
            print(obj)
        return None
    
    if kwargs:
        for k, v in kwargs.items():
            print(k, v)
        return None

    if flag:
        for k, v in DataBase.items():
            print(k, v, "\n")
    else:
        print(DataBase)

def read_to_database(id:int, *args, **kwargs) -> dict:
    """
    it's function return DataBase ---> Object
    """

    object_ = get_data_or_error(DataBase=DataBase, id=id)

    return object_


def update_data(id: int, **kwargs):
    """
    it's function update in DataBase on ID
    """

    email = kwargs.get('email')
    message = kwargs.get('message')

    global DataBase

    object_ = DataBase[id]

    object_['email'] = email if email else object_['email']
    object_['message'] = message if message else object_['message']

    return object_


for i in range(10):
    create_data(f"test{i}@test.com", "hello it is SPAMMMM")


def delete_data(id: int) -> dict:
    """
    It's function delete object on ID in DataBase
    """

    global DataBase
    get_data_or_error(DataBase=DataBase, id=id)
    object_ = DataBase.pop(id)

    return object_

# show_database(flag=True)
# answer = read_to_database(id=3)
# show_database(flag=False, args=answer)
# update_data(3, email='Zhan@gmail.com', message='Haha lol')
# delete_data(id=3)
# object_ = DataBase[id]

try:
    object_ = read_to_database(id=4)
except Exception as e:
    print(e)
else:
    print(object_)
    print("Вот твои данные")
# TODO Delete dor data
# TODO ShowData dor


