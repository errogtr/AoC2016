import re


def is_possible(a, b, c):
    return (a + b > c) and (b + c > a) and (a + c > b)


def all_possible(triangles):
    return sum(is_possible(*triangles[i : i + 3]) for i in range(0, len(triangles), 3))


with open("data") as f:
    triangles = [int(x) for x in re.findall(r"\d+", f.read())]

# ==== PART 1 ====
print(all_possible(triangles))

# ==== PART 2 ====
print(all_possible(triangles[::3] + triangles[1::3] + triangles[2::3]))
