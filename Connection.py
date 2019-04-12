import random


def rand_gen_connections(points):

    connections = dict([(i,[]) for i in range(points)])

    for i in range(points):
        for j in range(points):
            connected = random.choice([True,False])
            if connected and j!=i:
                connections[i].append(j)
    return connections



