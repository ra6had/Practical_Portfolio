
def distances(agents):
    """
    compute distances between agents
    
    arguments:
    agents -- a list of (a list of) coordinate pairs
    
    returns:
    distance_set -- a list of distances between all of coordinate pairs
    """

    distance_set = []
    i = 0
    for i in range(len(agents)):
        for j in range(len(agents)):
            if j > i:
                distance = (((agents[i][0] - agents[j][0])**2 + ((agents[i][1] - agents[j][1])**2))**0.5)
                distance_set.append(distance)
    return distance_set