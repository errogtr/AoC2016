import re


def abba(sequence):
    if m := re.search(r"(\w)(\w)\2\1", sequence):
        return len(set(m.group())) > 1
    return False


with open("data") as f:
    ips = f.read().splitlines()

tls = 0
for ip in ips:
    if any(abba(s) for s in re.findall(r"\[(\w+)]", ip)):
        continue
    tls += any(abba(s) for s in re.split(r"\[\w+]", ip))
print(tls)


aba = [
    re.compile(r"(?:^|])\w*(\w)(\w)\1.*\[\w*\2\1\2"),
    re.compile(r"\[\w*(\w)(\w)\1\w*].*\2\1\2\w*(?:\[|$)"),
]
print(sum(any(r.search(ip) for r in aba) for ip in ips))
