my_list= [1, 3.0 ["a", "b", ["A", "B", "C"], "d"], "John"]
for member in my_list:
    if isinstance(member, list):
        for m in member:
            print(m, end= " ")