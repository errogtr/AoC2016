import re
from itertools import product
from copy import copy


with open("data") as f:
    instructions = f.read().splitlines()

Lx, Ly = 50, 6
display = [["."] * Lx for _ in range(Ly)]

# ==== PART 1 ====
for instruction in instructions:
    if instruction.startswith("rect"):
        max_x, max_y = map(int, instruction[5:].split("x"))
        for x, y in product(range(max_x), range(max_y)):
            display[y][x] = "#"
    else:  # rotate
        direction, idx, shift = re.search(r"(x|y)=(\d+) by (\d+)", instruction).groups()
        if direction == "x":
            transposed = list(zip(*display))
            transposed[int(idx)] = [p for _, p in sorted(((j + int(shift)) % Ly, pixel) for j, pixel in enumerate(transposed[int(idx)]))]
            display = [list(row) for row in zip(*transposed)]
        else:
            display[int(idx)] = [p for _, p in sorted(((j + int(shift)) % Lx, pixel) for j, pixel in enumerate(display[int(idx)]))]
print(sum(sum(v == "#" for v in row) for row in display))

# ==== PART 2 ====
print("\n".join("".join(row) for row in display))
