def build_message(name: str, age: int) -> str:
    return f"{name} is {age} years old"


name = "Tom"
print(type(name))

name = 18
print(type(name))

user_name = "Tom"
user_age = 18
print(build_message(user_name, user_age))
