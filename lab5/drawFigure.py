def draw3dPyramid(size):
    for i in range(size):
        for j in range(size - i):
            print(" ", end=" ")
        for k in range(2 * i + 1):
            print("x", end=" ")
        for l in range(i+1):
            print(":", end=" ")
        print()

# Draw the 3D pyramid
#draw3dPyramid(10)

def draw2dPyramid(size):
    for i in range(size):
        for j in range(size - i):
            print(" ", end=" ")
        for k in range(2 * i + 1):
            print("x", end=" ")
        print()

# Draw the 3D pyramid
#draw2dPyramid(10)


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

# Set the size of the 3D cube
cube_size = 50

# Draw the 3D printed ASCII art cube
draw3dCube(cube_size)
