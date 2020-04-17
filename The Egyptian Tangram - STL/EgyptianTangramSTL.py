#!/usr/bin/env python
# -*- coding: utf-8 -*-

### MODULE INFO ################################################################

"""A set of functions for writing tangram-like objects in STL files."""

__all__     = ["preview", "prism", "read_stl", "write_stl"]
__author__  = "Carlos Luna-Mota"
__license__ = "The Unlicense"
__version__ = "20200417"

################################################################################



### AUXILIARY FUNCTIONS ########################################################

def inside(P, A, B, C, eps=0.000001):
    """
    Projects A, B, C and P into the XY plane and then checks if P is inside the
    (A,B,C) triangle (including the edges).

    Parameter "eps" determines sensibility of the algorithm when determining if
    P is so close to (A,B,C) triangle that must be considered as part of it.
    Don't override its default value (10^-6) unless you have a good reason.

    """

    # Project the points into the XY Plane:
    P = tuple(list(P[:2]) + [0.0]*(2-len(P)))
    A = tuple(list(A[:2]) + [0.0]*(2-len(A)))
    B = tuple(list(B[:2]) + [0.0]*(2-len(B)))
    C = tuple(list(C[:2]) + [0.0]*(2-len(C)))

    # Compute U, V & W vectors:
    U = (P[0]-C[0], P[1]-C[1])
    V = (A[0]-C[0], A[1]-C[1])
    W = (B[0]-C[0], B[1]-C[1])

    # Compute the barycentric coordinates of P:
    d = float(W[1]*V[0] - W[0]*V[1])
    a = float(W[1]*U[0] - W[0]*U[1])
    b = float(U[1]*V[0] - U[0]*V[1])
    c = d-a-b

    # Check check if the barycentric coordinates definition holds:
    if abs(d) > eps:
        assert(P[0]-eps <= (a/d)*A[0] + (b/d)*B[0] + (c/d)*C[0] <= P[0]+eps)
        assert(P[1]-eps <= (a/d)*A[1] + (b/d)*B[1] + (c/d)*C[1] <= P[1]+eps)

    # Determine if the point is inside the triangle
    if d >= 0.0: return (0.0-eps)*d <= min(a,b,c) and max(a,b,c) <= (1.0+eps)*d
    else:        return (1.0+eps)*d <= min(a,b,c) and max(a,b,c) <= (0.0-eps)*d

def triangulation(polygon):
    """
    Returns a triangulation of the polygon based on a projection of the polygon
    into the XY plane.

    All the returned triangles are in counterclockwise order when projected
    into the XY plane.

    """

    # See if there is a polygon at all
    assert(len(polygon) > 2)

    # Normalize the dimensions of the polygon vertices:
    P = [tuple(list(point[:3]) + [0.0]*(3-len(point))) for point in polygon]

    # Compute the oriented area to ensure counterclockwise orientation of P:
    area = sum(P[i-1][0]*Q[1]-P[i-1][1]*Q[0] for i,Q in enumerate(P))
    if area < 0.0: P.reverse()

    # Keep clipping ears until done:
    N, T, i = len(P), [], 0
    while i < N and N > 2:

        # Generate a candidate facet and compute its oriented area:
        A    = P[i-2][:]
        B    = P[i-1][:]
        C    = P[i  ][:]
        area = C[0]*A[1]-C[1]*A[0] + A[0]*B[1]-A[1]*B[0] + B[0]*C[1]-B[1]*C[0]

        # Determine if the facet is valid and we can clip it:
        if   area <= 0.000001:                                     i+=1
        elif any(inside(P[j], A, B, C) for j in range(i+1-N,i-2)): i+=1
        else:
            T.append((A,B,C))
            P.pop(i-1)
            i  = max(0, i-1)
            N -= 1

    # Return triangulation
    return T

def normal(P, Q, R):
    """
    Returns the normal vector of the 3D facet (P,Q,R) using the right-hand rule.

    The function returns a unit-length normal vector unless P, Q and R are
    collinear. In that degenerate case it returns the null vector (0,0,0).

    """

    # Normalize dimensions:
    P = tuple(list(P[:3]) + [0.0]*(3-len(P)))
    Q = tuple(list(Q[:3]) + [0.0]*(3-len(Q)))
    R = tuple(list(R[:3]) + [0.0]*(3-len(R)))

    V = (Q[0]-P[0], Q[1]-P[1], Q[2]-P[2]) # P->Q
    W = (R[0]-P[0], R[1]-P[1], R[2]-P[2]) # P->R

    Nx = V[1] * W[2] - V[2] * W[1]
    Ny = V[2] * W[0] - V[0] * W[2]
    Nz = V[0] * W[1] - V[1] * W[0]

    length = (Nx*Nx + Ny*Ny + Nz*Nz)**0.5

    if length > 0.000001: return (Nx/length, Ny/length, Nz/length)
    else:
        print("WARNING: These points determine a null normal vector")
        print("         ({:8.2f}, {:8.2f}, {:8.2f})".format(*P))
        print("         ({:8.2f}, {:8.2f}, {:8.2f})".format(*Q))
        print("         ({:8.2f}, {:8.2f}, {:8.2f})".format(*R))
        return (0, 0, 0)

################################################################################



### STL FUNCTIONS ##############################################################

def prism(polygon, height):
    """
    Returns the facets of the 3D prism that has:

        lower base = polygon
        upper base = translation(polygon, (0,0,height))

    The polygon must project cleanly to the XY plane because it will be
    projected there for triangulation purposes.

    """

    # Sanity checks:
    assert(      height > 0)
    assert(len(polygon) > 2)

    # Normalize the dimensions of the polygon vertices:
    P = [tuple(list(point[:3]) + [0.0]*(3-len(point))) for point in polygon]

    # Compute the oriented area to ensure counterclockwise orientation of P:
    area = sum(P[i-1][0]*Q[1]-P[i-1][1]*Q[0] for i,Q in enumerate(P))
    if area < 0.0: P.reverse()

    # Triangulate the polygon on the XY plane:
    base = triangulation(P)

    # Generate a list of facets:
    facets = []

    # LOWER BASE FACETS:
    for A,B,C in base: facets.append((C,B,A))

    # LATERAL FACETS:
    for i in range(len(P)):
        A  = (P[i  ][0], P[i  ][1], P[i  ][2])
        B  = (P[i-1][0], P[i-1][1], P[i-1][2])
        AA = (P[i  ][0], P[i  ][1], P[i  ][2]+height)
        BB = (P[i-1][0], P[i-1][1], P[i-1][2]+height)
        facets.append((A,AA,B))
        facets.append((AA,BB,B))

    # UPPER BASE:
    for A,B,C in base:
        AA = (A[0], A[1], A[2]+height)
        BB = (B[0], B[1], B[2]+height)
        CC = (C[0], C[1], C[2]+height)
        facets.append((AA,BB,CC))

    return facets

def preview(P, name="Preview", alpha=0.7, axis=True, color='w'):
    """
    Shows a list of facets using matplotlib.

    * Parameter "name" determines the title of the preview window.
    * Parameter "alpha" controls the opacity of the facets (0 <= alpha <= 1)
    * Parameter "axis" determines if the axes are shown.
    * Parameter "color" determines the color of the facets.

    This function requires an additional 3rd party library called matplotlib.
    If you cannot install matplotlib you won't be able to use this function.

    """

    from matplotlib   import pyplot
    from mpl_toolkits import mplot3d

    # Compute the scale:
    scale  = [min(min(min(X,Y,Z) for X,Y,Z in facet) for facet in P),
              max(max(max(X,Y,Z) for X,Y,Z in facet) for facet in P)]

    # Create a new plot
    figure = pyplot.figure(num=name)
    axes   = mplot3d.Axes3D(figure)
    if not axis: axes.set_axis_off()
    else:        axes.auto_scale_xyz(scale, scale, scale)

    # Add the vectors to the plot
    collection = mplot3d.art3d.Poly3DCollection(P, linewidths=2)
    if 0.0 <= alpha < 1.0: collection.set_alpha(alpha)
    collection.set_facecolor(color)
    collection.set_edgecolor('black')
    axes.add_collection3d(collection)

    # Show the plot to the screen
    pyplot.show()

def read_stl(filename):
    """
    Reads the STL file and returns a list of facets (being each facet a list
    of three 3D points).

    * *arameter "filename" must include the ".stl" extension

    Adapted from: https://stackoverflow.com/questions/54006078/

    """

    # Determine if the STL file is in ASCII or binary format:
    is_ASCII = True
    try:
        with open(filename, 'r') as f: line = f.readline()
    except UnicodeDecodeError: is_ASCII = False
    if is_ASCII:
        if len(line) < 5 or line[0:5].lower() != 'solid': is_ASCII = False

    # READ ASCII:
    if is_ASCII:
        facets = []
        with open(filename, 'r') as f: L = [l.split() for l in f.readlines()]
        facet = []
        for line in L:
            if line[0].lower() == 'vertex':
                facet.append(tuple([float(x) for x in line[1:]]))
                if len(facet) == 3: facets.append(tuple(facet)); facet = []

    # READ BINARY:
    else:
        facets = []
        with open(filename, 'rb') as f:
            f.seek(80)                              # skip header
            N = struct.unpack('I', f.read(4))[0]    # number of facets
            for i in range(N):
                  f.seek(12, 1)                     # skip normal
                  facet = []                        # read three 3D points
                  facet.append(struct.unpack('fff', f.read(12))) # read point
                  facet.append(struct.unpack('fff', f.read(12))) # read point
                  facet.append(struct.unpack('fff', f.read(12))) # read point
                  facets.append(tuple(facet))       # store the facet
                  f.seek(2, 1)                      # skip attribute

    # Return facets:
    return facets

def write_stl(filename, facets, header=None, attributes=None, ASCII=False):
    """
    Writes a list of facets into a STL file.

    * Parameter "filename" must include the ".stl" extension.
    * Only the first 80 characters of "header" are used.
    * Parameter "attributes" must be a list of integers as long as "facets".
    * The normal of each facet must point outwards.

    Adapted from: https://stackoverflow.com/questions/54006078/

    """

    # Normalize point dimension:
    facets = [(tuple(list(P[:3]) + [0.0]*(3-len(P))),
               tuple(list(Q[:3]) + [0.0]*(3-len(Q))),
               tuple(list(R[:3]) + [0.0]*(3-len(R)))) for (P,Q,R) in facets]

    # Normalize header
    if header: header = header[:80] + '\0'*(80-len(header))
    else:      header = '\0' * 80

    # Normalize attributes
    if attributes: assert(len(attributes) == len(facets))
    else:          attributes = [0] * len(facets)

    # Write ASCII STL file:
    if ASCII:
        with open(filename, 'w') as f:
            name = filename[:filename.rfind('.')]
            f.write("solid {}\n".format(name))
            for (P,Q,R) in facets:
                N = normal(P,Q,R)
                f.write("    facet normal {:e} {:e} {:e}\n".format(*N))
                f.write("        outer loop\n")
                f.write("            vertex {:e} {:e} {:e}\n".format(*P))
                f.write("            vertex {:e} {:e} {:e}\n".format(*Q))
                f.write("            vertex {:e} {:e} {:e}\n".format(*R))
                f.write("        endloop\n")
                f.write("    endfacet\n")
            f.write("endsolid {}\n".format(name))

    # Write binary STL file:
    else:
        import struct
        with open(filename, 'wb') as f:
            f.write(struct.pack('80s', header.encode('utf-8')))
            f.write(struct.pack('I', len(facets)))
            for i, (P,Q,R) in enumerate(facets):
                N = normal(P,Q,R)
                f.write(struct.pack('fff', N[0], N[1], N[2]))
                f.write(struct.pack('fff', P[0], P[1], P[2]))
                f.write(struct.pack('fff', Q[0], Q[1], Q[2]))
                f.write(struct.pack('fff', R[0], R[1], R[2]))
                f.write(struct.pack('H', attributes[i]))

################################################################################



### MAIN FUNCTION ##############################################################

if __name__ == "__main__":


    ### Basic parameters #######################################################

    #size   = 100.0                  # Tangram size   (in mm)
    #height =   5.0                  # Tangram height (in mm)

    size   = 25.0*2.0*(5.0**0.5)    # Tangram size   (in mm)
    height =  5.0                   # Tangram height (in mm)

    #size   = 35.0*2.0*(5.0**0.5)    # Tangram size   (in mm)
    #height = 10.0                   # Tangram height (in mm)


    ### Print basic information on the screen ##################################

    s = size / 10.0                 # Tangram size      (in cm)
    h = height / 10.0               # Tangram height    (in cm)
    l = size / (2.0*(5.0**0.5))     # Shortest length   (in mm)
    a = 26.57                       # Acutest angle     (atan(1/2) in degrees)

    surface = h * (4.0*s + 1.5*l) + 2.0*s*s     # Total surface     (in cm²)
    volume  = s*s*h                             # Total volume      (in cm³)
    bed     = 0.575*l                           # Printer bed size  (in cm)

    print(" ╔═════════════════════════════════════════╗")
    print(" ║          EGYPTIAN TANGRAM STL           ║")
    print(" ╠═════════════════════════════════════════╣")
    print(" ║                                         ║")
    print(" ║  Tangram size: {:5.2f} × {:5.2f} × {:4.2f} cm  ║".format(s,s,h))
    print(" ║                                         ║")
    print(" ║  Shortest length:  {:6.2f} mm            ║".format(l))
    print(" ║  Longest length:   {:6.2f} mm            ║".format(5.0*l))
    print(" ║  Acutest angle:    {:6.2f} º             ║".format(a))
    print(" ║                                         ║")
    print(" ║  Total surface:    {:6.2f} cm²           ║".format(surface))
    print(" ║  Total volume:     {:6.2f} cm³           ║".format(volume))
    print(" ║  Printer bed size: {:6.2f} × {:5.2f} cm    ║".format(bed, bed))
    print(" ║                                         ║")
    print(" ╚═════════════════════════════════════════╝")


    ### Piece definitions ######################################################

    x = size /(2.0*(5.0**0.5))  # Rational length   (in mm)
    y = size / 2.0              # Irrational length (in mm)

    T1 = prism([(0.25*x,0.00*x), (2.25*x,1.00*x),   (2.25*x,0.00*x)], height)
    T4 = prism([(0.00*x,2.50*x), (4.00*x,2.50*x),   (0.00*x,0.50*x)], height)
    T5 = prism([(0.00*y,3.15*x), (0.00*y,3.15*x+y), (2.00*y,3.15*x)], height)
    T6 = prism([(5.75*x,5.75*x), (5.75*x,2.75*x),   (1.75*x,5.75*x)], height)
    Q4 = prism([(2.75*x,0), (2.75*x,x), (4.75*x,2.0*x), (5.75*x,0)],  height)


    ### Write and preview the STL files ########################################

    write_stl("Egyptian Tangram - T1.stl", T1, ASCII=True)
    write_stl("Egyptian Tangram - T4.stl", T4, ASCII=True)
    write_stl("Egyptian Tangram - T5.stl", T5, ASCII=True)
    write_stl("Egyptian Tangram - T6.stl", T6, ASCII=True)
    write_stl("Egyptian Tangram - Q4.stl", Q4, ASCII=True)

    write_stl("Egyptian Tangram.stl", T1+T4+T5+T6+Q4, ASCII=True)

    preview(read_stl("Egyptian Tangram.stl"))

################################################################################
