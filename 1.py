from itertools import groupby

with open("1.input") as f:
    pairs = [(int(x), int(y)) for (x, y) in [line.strip().split() for line in f]]
(list1, list2) = zip(*pairs)

distance = 0
for (a, b) in zip(sorted(list1), sorted(list2)):
    distance += abs(int(b) - int(a))

print(f"Distance:   {distance}")

# counts = {}
# for k, g in groupby(sorted(list2)):
#     counts[k] = len(list(g))

counts = dict((k, len(list(g))) for k, g in groupby(sorted(list2)))
similarity = 0
for k, g in groupby(sorted(list1)):
    similarity += k * counts.get(k, 0)

print(f"Similarity: {similarity}")
