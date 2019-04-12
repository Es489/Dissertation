import numpy as np
import random


def create_grid(n, m):
    l = []
    for i in range(n):
        l.append([' ' for _ in range(m)])
    return l


def choose_points(nu, gr, radius, distance):
    count = 0



    cells = [i for i in np.argwhere(gr == ' ').tolist()]
    reference = [i for i in cells]


    while count < nu and cells!=[]:


            cell = random.choice(cells)

            row = cell[0]
            column = cell[1]

            check = check_point(radius,row,column,gr)

            if check & (gr[row][column]==' '):

                                cells.remove(cell)
                                reference.remove(cell)
                                count+=1

                                cells = map_point(gr,row,column,radius,distance,reference,cells,count)

            else:
                 cells.remove(cell)


"""Check if chosen point allows to have given radius, if not modifies it """
def boundaries(radius,row,column,gr):
    up_radius = radius
    down_radius = radius
    left_radius = radius
    right_radius = radius
    x, y = gr.shape

    if row - radius < 0:
        up_radius = row
    elif row + radius > x:
        down_radius = x - row

    if column - radius < 0:
        left_radius = column
    elif column + radius > y:
        right_radius = y - column

    return up_radius, down_radius, right_radius, left_radius

"""Checks if the chosen point is leagal"""
def check_point(radius,row,column, gr):
    u,d,r,l = boundaries(radius,row,column,gr)

    boundries = gr[row - u:row + d + 1, column - l:column + r + 1].tolist()
    diameter = ['*' not in i for i in boundries]

    return sum(diameter) == len(boundries)

"""Mapps point onto a given grig g and returns legal cells for other point to find"""
def map_point(g,row,column,radius, distance, reference,cells,count):
    g[row][column] = 1
    u, d, r, l = boundaries(radius, row, column, g)
    rows = range(row - u, row + d + 1)
    columns = range(column - l, column + r + 1)
    r,c = g.shape
    #check if we can go up,down left or right dor the given distance
    #get cells corresponding to rows and columns for distance boundary and put them inrto ex_d
    perimeter = [i for i in reference if (i[0] in rows) & (i[1] in columns)]
    excluded = [i for i in cells if (i[0] in rows) & (i[1] in columns)]
    ex_d = []
    cells = [i for i in cells if i not in excluded] + ex_d
    for i in perimeter:
        g[i[0]][i[1]] = "*"

    return cells









#
# g = np.array(create_grid(15, 15))
# choose_points(3,g,2,0)
# for j in g:
#     print(j)


