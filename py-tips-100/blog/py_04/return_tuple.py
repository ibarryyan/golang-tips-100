from dataclasses import dataclass


def parse_user():
    return "Tom", 18


name, age = parse_user()
print(name, age)

result = parse_user()
print(result)
print(type(result))


@dataclass
class User:
    name: str
    age: int


def parse_better_user() -> User:
    return User(name="Tom", age=18)


print(parse_better_user())
