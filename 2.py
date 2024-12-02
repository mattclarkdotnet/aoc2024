# Define the logic
def safe1(l: list) -> bool:
    diffs = [a-b for a, b in zip(l, l[1:])]
    return all(d>=1 and d<=3 for d in diffs) or all(d>=-3 and d<=-1 for d in diffs)

def safe2(l: list) -> bool:
    if safe1(l):
        return True
    else:
        # Try removing each level and see if that makes things safe
        for i in range(len(l)):
            newlist = list(l)
            del newlist[i]
            if safe1(newlist):
                return True
    return False

# Read the input
with open("2.input") as f:
    reports = [list(map(int, line.strip().split())) for line in f]

# Calculate the results
count = 0
for r in reports:
    if safe1(r):
        count += 1
print(f"Safe reports 1: {count}")

count = 0
for r in reports:
    if safe2(r):
        count += 1
print(f"Safe reports 2: {count}")
