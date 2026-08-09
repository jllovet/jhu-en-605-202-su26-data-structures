def get_hashed_value(key):
    return key * 2 + 3


def insert(a, k):
    i = 0
    hashed_value = get_hashed_value(k)
    index = hashed_value % len(a)
    print(f"Inserting {k} into {a}")
    print(
        f"get_hashed_value({k}) -> {get_hashed_value(k)} -> x mod {len(a)} -> {get_hashed_value(k) % len(a)}")
    while True:
        print(f"Attempting to insert {k} at index {index}")
        if a[index] == "_":
            print(f"Inserted {k} at index {index}")
            a[index] = k
            return a, i
        else:
            print(
                f"Collision at {index}, which contains the value: {a[index]}")
            print(
                f"Calculating new index: get_hashed_value({index}) -> {get_hashed_value(index)} -> x mod {len(a)} -> {get_hashed_value(index) % len(a)}")
            hashed_value = get_hashed_value(index)
            index = hashed_value % len(a)
            i += 1


n = 13
a = list()
for i in range(n):
    a.append("_")


keys = [5, 4, 25, 8, 10, 34, 18, 51, 17, 21]

for key in keys:
    collisions = 0
    a, collisions = insert(a, key)
    print(f"{collisions} collisions while inserting {key}")
    print(f"Current value of hash table: {a}")
    print()
