import json
from collections import defaultdict


data = json.load(open('./ingredients.json'))

data = {
    k: v
    for k, v in data.items()
    if not k.endswith('(V)')
}

stats = defaultdict(lambda: 0)
for I in data.values():
    for i in I:
        stats[i] += 1

count = list(sorted(([n, i] for i, n in stats.items()), reverse=True))
ingredients = [i for _, i in count]

data = dict(sorted(data.items(), key=lambda d: sorted(((stats[i], i) for i in d[1]), reverse=True)))

# print('\n'.join(f'{n} {i}' for n, i in count))
# print()
# print(f'{len(data)} foods')
# print(f'{len(ingredients)} ingredients')

import matplotlib.pyplot as plt
import numpy as np

grid = np.array([
    [1 if i in recipe else 0 for i in ingredients]
    for recipe in data.values()
])

fig, ax = plt.subplots()
im = ax.imshow(grid, aspect=len(ingredients)/len(data))
ax.set_yticks(np.arange(len(data)), labels=[food for food in data.keys()], fontsize=6)
ax.set_xticks(np.arange(len(ingredients)), labels=ingredients, fontsize=6)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
# fig.tight_layout()
plt.show()
