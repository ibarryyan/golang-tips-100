def add_bad_tag(tag, tags=[]):
    tags.append(tag)
    return tags


def add_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags


print(add_bad_tag("python"))
print(add_bad_tag("ai"))

print(add_tag("python"))
print(add_tag("ai"))
