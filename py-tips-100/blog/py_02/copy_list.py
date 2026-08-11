from copy import deepcopy

old_users = ["Tom", "Jerry"]
new_users = old_users
new_users.append("Alice")
print(old_users)

users = [{"name": "Tom", "tags": ["admin"]}]
copied_users = deepcopy(users)
copied_users[0]["tags"].append("vip")

print(users)
print(copied_users)
