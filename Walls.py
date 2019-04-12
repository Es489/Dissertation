import numpy as np


def get_avaliable_cells(grid):
    return [i for i in np.argwhere(grid == ' ').tolist()]

