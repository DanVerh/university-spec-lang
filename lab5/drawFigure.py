def draw3dPyramid(size):
    for i in range(size):
        for j in range(size - i):
            print(" ", end=" ")
        for k in range(2 * i + 1):
            print("x", end=" ")
        for l in range(i+1):
            print(":", end=" ")
        print()

def draw2dPyramid(size):
    for i in range(size):
        for j in range(size - i):
            print(" ", end=" ")
        for k in range(2 * i + 1):
            print("x", end=" ")
        print()

def draw3dCube(size):

    for i in range(size):
        print("/", end=" ")
        if i == size - 1:
            print(" |")

    for i in range(size-1):
        for j in range(size):
            print("|", end=" ")
            if j == size - 1 and i != size-2:
                print(" |", end=" ")
            elif j == size - 1 and i == size-2:
                print("/", end=" ")
        print()

def draw2dCube(size):
    for i in range(size-1):
        for j in range(size):
            print("|", end=" ")
        print()