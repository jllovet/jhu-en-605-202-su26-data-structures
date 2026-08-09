def get_hashed_value(key):
    return key * 2 + 3


def insert(a, k):
    i = 0
    print(f"Inserting {k} into {a}")
    print(
        f"get_hashed_value({k}) -> {get_hashed_value(k)} -> x mod {len(a)} -> {get_hashed_value(k) % len(a)}")
    while True:
        print(f"Attempting to insert {k} at index {get_hashed_value(k) % len(a) + i}")
        if a[get_hashed_value(k) % len(a) + i] == "_":
            print(f"Inserted {k} at index {get_hashed_value(k) % len(a) + i}")
            a[get_hashed_value(k) % len(a) + i] = k
            return a, i
        else:
            print(
                f"Collision at {get_hashed_value(k) % len(a) + i}, which contains the value: {a[get_hashed_value(k) % len(a) + i]}")
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
