cache = {}
def routes(dim1, dim2):
    if (dim1 == 0 or dim2 == 0):
        return 1
    if (str(dim1) + "," + str(dim2) in cache):
        return cache[str(dim1) + "," + str(dim2)]
    cache[str(dim1) + "," + str(dim2)] = routes(dim1, dim2 - 1) + routes(dim1 - 1, dim2)
    return cache[str(dim1) + "," + str(dim2)]
print(routes(20, 20))