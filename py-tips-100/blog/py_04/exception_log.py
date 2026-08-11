import logging

logging.basicConfig(level=logging.INFO)

try:
    int("abc")
except ValueError:
    logging.exception("parse int failed")


def parse_age(text: str) -> int:
    return int(text)


print(parse_age("18"))
