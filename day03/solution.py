import re


def is_possible(a, b, c):
    return (a + b > c) and (b + c > a) and (a + c > b)


with open("data") as f:
    triangles = [int(x) for x in re.findall(r"\d+", f.read())]

# ==== PART 1 ====
print(sum(is_possible(*triangles[i:i+3]) for i in range(0, len(triangles), 3)))

# ==== PART 2 ====
triangles = triangles[::3] + triangles[1::3] + triangles[2::3]
print(sum(is_possible(*triangles[i:i+3]) for i in range(0, len(triangles), 3)))
