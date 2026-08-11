from collections import defaultdict

user = {"name": "Tom"}
print(user.get("age", 0))

groups = {}
groups.setdefault("python", []).append("Tom")
groups.setdefault("python", []).append("Alice")
print(groups)

better_groups = defaultdict(list)
better_groups["python"].append("Tom")
better_groups["python"].append("Alice")
print(dict(better_groups))
