import numpy as np
from math import sqrt
from stl import mesh
from matplotlib import pyplot
from mpl_toolkits import mplot3d

### CONFIGURATION ##############################################################

# Basic Parameters:
name  = "EgyptianTangram"   # File Name
S     = 100.0               # Square Side         (in mm)
H     =   5.0               # Piece Height        (in mm)
slack =   2.0               # Box Slack           (in mm)

# Derived Sizes:
X   = S/(2.0*sqrt(5.0))     # Rational   Unit     (in mm) 
Y   = S/ 2.0                # Irrational Unit     (in mm)
B   = 5.75*X                # 3D Printer Bed Size (in mm)
b_S = H+S+H+slack           # Box Side            (in mm)
b_H = H+H+slack             # Box Height          (in mm)

# Print Basic Info:
print("EGYPTIAN TANGRAM STL:\n")
print("Unit Length:   {:8.2f} mm".format(X))
print("Square Side:   {:8.2f} mm".format(S))
print("Piece Height:  {:8.2f} mm".format(H))
print("Total Surface: {:8.2f} mm^2".format(H*(S*4 + X*15) + 2*S*S))
print("Total Volume:  {:8.2f} mm^3".format(S*S*H))
print("Printer Bed:   {:8.2f} mm x {:6.2f} mm".format(B, B))

################################################################################



### AUXILIARY FUNCTIONS ########################################################

def normal(X, Y, Z):
    """
    Requirements:
    
    * No zero-area facet is allowed.
        
    """

    A = [Y[0]-X[0],Y[1]-X[1],Y[2]-X[2]] # Y-X
    B = [Z[0]-X[0],Z[1]-X[1],Z[2]-X[2]] # Z-X

    Nx = A[1] * B[2] - A[2] * B[1]
    Ny = A[2] * B[0] - A[0] * B[2]
    Nz = A[0] * B[1] - A[1] * B[0]

    length = sqrt(Nx*Nx + Ny*Ny + Nz*Nz)

    if length < 0.000001:
        print("ERROR: Found a facet with area 0.")
        print("       ({:8.2f}, {:8.2f}, {:8.2f})".format(*X))
        print("       ({:8.2f}, {:8.2f}, {:8.2f})".format(*Y))
        print("       ({:8.2f}, {:8.2f}, {:8.2f})".format(*Z))

    return [Nx/length, Ny/length, Nz/length]

def facet(X, Y, Z):
    """
    Requirements:
    
    * The vertices must be given in anticlockwise order.
    
    """
    
    output = []
    N = normal(X, Y, Z)
    output.append("    facet normal {:e} {:e} {:e}\n".format(*N))
    output.append("        outer loop\n")
    output.append("            vertex {:e} {:e} {:e}\n".format(*X))
    output.append("            vertex {:e} {:e} {:e}\n".format(*Y))
    output.append("            vertex {:e} {:e} {:e}\n".format(*Z))
    output.append("        endloop\n")
    output.append("    endfacet\n")
    return output

def prism(vertices, H):
    """
    Requirements:
    
    * The vertices must be given in clockwise order.
    * Diagonals from vertices[0] must be 'interior'.
    
    """

    output = []

    # Print Sides:
    for i in range(-1, len(vertices)-1):
        
        A = vertices[i]
        B = vertices[i+1]
        
        output += facet([A[0],A[1],0.0], [A[0],A[1],H], [B[0],B[1],0.0])
        output += facet([A[0],A[1],H],   [B[0],B[1],H], [B[0],B[1],0.0])

    # Print Base:
    for i in range(1, len(vertices)-1):

        A = vertices[0]
        B = vertices[i]
        C = vertices[i+1]
                
        output += facet([A[0],A[1],0.0], [B[0],B[1],0.0], [C[0],C[1],0.0])

    # Print Top:
    for i in range(1, len(vertices)-1):

        A = vertices[0]
        B = vertices[i]
        C = vertices[i+1]

        output += facet([C[0],C[1],H], [B[0],B[1],H], [A[0],A[1],H])
    
    return output
    
def view(filename, edges=True, axis=True):
    """
    Opens the STL file and shows the 3D figure using mathplotlib

    Requirements:

    * filename must include the extension

    """

    # Create a new plot
    figure = pyplot.figure()
    axes   = mplot3d.Axes3D(figure)

    if not axis: axes.set_axis_off()

    # Load the STL files and add the vectors to the plot
    MESH = mesh.Mesh.from_file(filename)
    collection = mplot3d.art3d.Poly3DCollection(MESH.vectors, linewidths=2)
    collection.set_alpha(0.7)
    collection.set_facecolor('w')
    if edges: collection.set_edgecolor('k')
    axes.add_collection3d(collection)
    
    # Auto scale to the mesh size
    scale = MESH.points.flatten(-1)
    axes.auto_scale_xyz(scale, scale, scale)

    # Show the plot to the screen
    pyplot.show()

################################################################################



### MAIN FUNCTION ##############################################################

if __name__ == "__main__":

    ### EGYPTIAN TANGRAM'S PIECES ##############################################

    T6 = [[5.75*X, 5.75*X],
          [5.75*X, 2.75*X],
          [1.75*X, 5.75*X]]

    T5 = [[0.00,   3.15*X  ],
          [0.00,   3.15*X+Y],
          [2.00*Y, 3.15*X  ]]

    T4 = [[0.00  , 2.50*X],
          [4.00*X, 2.50*X],
          [0.00  , 0.50*X]]

    T1 = [[0.25*X, 0.00  ],
          [2.25*X, 1.00*X],
          [2.25*X, 0.00  ]]

    Q4 = [[2.75*X, 1.00*X],
          [4.75*X, 2.00*X],
          [5.75*X, 0.00  ],
          [2.75*X, 0.00  ]]

    ### T6 #####################################################################

    with open("{}-{:.0f}x{:.0f}x{:.0f}.stl".format("T6",S,S,H), "w") as output:

        output.write("solid T6\n")
        output.writelines(prism(T6, H))
        output.write("endsolid T6\n")

    ### T5 #####################################################################

    with open("{}-{:.0f}x{:.0f}x{:.0f}.stl".format("T5",S,S,H), "w") as output:

        output.write("solid T5\n")
        output.writelines(prism(T5, H))
        output.write("endsolid T5\n")

    ### T4 #####################################################################

    with open("{}-{:.0f}x{:.0f}x{:.0f}.stl".format("T4",S,S,H), "w") as output:

        output.write("solid T4\n")
        output.writelines(prism(T4, H))
        output.write("endsolid T4\n")

    ### T1 #####################################################################

    with open("{}-{:.0f}x{:.0f}x{:.0f}.stl".format("T1",S,S,H), "w") as output:

        output.write("solid T1\n")
        output.writelines(prism(T1, H))
        output.write("endsolid T1\n")

    ### Q4 #####################################################################

    with open("{}-{:.0f}x{:.0f}x{:.0f}.stl".format("Q4",S,S,H), "w") as output:

        output.write("solid Q4\n")
        output.writelines(prism(Q4, H))
        output.write("endsolid Q4\n")

    ### EGYPTIAN TANGRAM #######################################################
    
    with open("{}-{:.0f}x{:.0f}x{:.0f}.stl".format(name,S,S,H), "w") as output:

        output.write("solid EgyptianTangram\n")
        output.writelines(prism(T6, H))
        output.writelines(prism(T5, H))
        output.writelines(prism(T4, H))
        output.writelines(prism(T1, H))
        output.writelines(prism(Q4, H))
        output.write("endsolid EgyptianTangram\n")

    ### STL VIEWER #############################################################

    # Show the Egyptian Tangram:
    view("{}-{:.0f}x{:.0f}x{:.0f}.stl".format(name,S,S,H))
    
################################################################################
