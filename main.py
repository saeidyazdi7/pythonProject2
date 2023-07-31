dictionaries = [{"weight": 50, "apple": "red"}, {"weight": 40, "banana": "yellow"}, {"weight": 60, "orange": "orange"},
                {"weight": 30, "lime": "green"}]
new = sorted(dictionaries, key=lambda x: list(x.values())[1])
print(new)