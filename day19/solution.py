# solved first with pen and paper

# ==== PART 1 ====
# write any number N as 2^n + k, where n is the largest number s.t. 2^n < N, and 0 <= k < 2^n.
# Then: f(2^n + k) = 2k + 1


# ==== PART 2 ====
# write any number N as 3^n + k, where n is the largest number s.t. 3^n < N, and 1 <= k < 2 * 3^n.
# Then:
#               |- k,          if 1 <= k < 3^n
# f(2^n + k) = -|
#               |- 2k - 3^n,   if 3^n <= k < 2*3^n

