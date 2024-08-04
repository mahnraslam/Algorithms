#Generic in python
#First install mypy
#Run the program by : mypy fileName.py:mypy Day4_Generic.py
def  greeting(name:str) -> str :
    return "Hello" + name

#print(greeting(123))

print(greeting("Sara"))

def greet_all(names: list[str]) -> None:
    for name in names:
        print('Hello ' + name)
    return None

names = ["Alice", "Bob", "Charlie"]
ages = [10, 20, 30]

greet_all(names)   # Ok!
#greet_all(ages)    # Error due to incompatible types

from typing import Union

def normalize_id(user_id: Union[int, str]) -> str:
    if isinstance(user_id, int):
        return f'user-{100_000 + user_id}'
    else:
        return user_id
print(normalize_id(3434))