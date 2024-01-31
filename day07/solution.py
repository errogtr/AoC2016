import re


with open("data") as f:
    ips = f.read().splitlines()


# ==== PART 1 ====
supernet = re.compile(r"(?:^|])\w*(\w)((?!\1)\w)\2\1\w*(?:\[|$)")  # search for 'abba' outside '[]'
hypernet = re.compile(r"\[\w*(\w)((?!\1)\w)\2\1\w*]")  # search for 'abba' inside '[]'
print(sum(supernet.search(ip) is not None and not hypernet.search(ip) for ip in ips))

# ==== PART 2 ====
aba = [
    re.compile(r"(?:^|])\w*(\w)((?!\1)\w)\1.*\[\w*\2\1\2"),  # ...aba...[...bab...]
    re.compile(r"\[\w*(\w)((?!\1)\w)\1\w*].*\2\1\2\w*(?:\[|$)"),   # ...[...aba...]...bab...
]
print(sum(any(r.search(ip) for r in aba) for ip in ips))
