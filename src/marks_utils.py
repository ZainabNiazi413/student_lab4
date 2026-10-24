
import numpy as np

def standardise_loop(data):
    rows = len(data)
    cols = len(data[0])

    means = []
    stds = []

    for j in range(cols):
        column = [data[i][j] for i in range(rows)]
        means.append(sum(column) / rows)
        stds.append((sum((x - means[j]) ** 2 for x in column) / rows) ** 0.5)

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            if stds[j] == 0:
                row.append(0.0)
            else:
                row.append((data[i][j] - means[j]) / stds[j])
        result.append(row)

    return np.array(result)


def standardise_np(data):
    means = data.mean(axis=0)
    stds = data.std(axis=0)
    stds = np.where(stds == 0, 1, stds)
    return (data - means) / stds
