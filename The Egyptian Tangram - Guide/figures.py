#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
#
# Figure generator for: "The Egyptian Tangram Guide"
#
# By: Carlos Luna Mota
#
################################################################################

# LIBRARIES
from pyx import *
from math import *
from itertools import product

# CONSTANTS
BETA = 180*atan2(1,2)/pi
R2  = sqrt(2.0)
R3  = sqrt(3.0)
R5  = sqrt(5.0)
R10 = sqrt(10.0)

# COLOR PALETTE
WHITE    = color.grey.white
BLACK    = color.grey(0.10)
D_GREY   = color.grey(0.30)
GREY     = color.grey(0.50)
L_GREY   = color.grey(0.70)
CHALK    = color.grey(0.90)

RED      = color.cmyk.Mahogany
BLUE     = color.cmyk.NavyBlue
GREEN    = color.cmyk.ForestGreen
ORANGE   = color.cmyk.Orange
YELLOW   = color.cmyk.Dandelion

L_RED    = color.cmyk.Red
L_BLUE   = color.cmyk.SkyBlue
L_GREEN  = color.cmyk.LimeGreen
L_ORANGE = color.cmyk.YellowOrange
L_YELLOW = color.cmyk.Goldenrod

D_GREEN  = color.cmyk.OliveGreen
PLUM     = color.cmyk.Orchid
PINK     = color.cmyk.Lavender
BROWN    = color.cmyk.RawSienna

# LINE STYLES
BASE       = [style.linewidth.THick, style.linestyle.solid, style.linecap.round, style.linejoin.round, WHITE]
ULTRATHICK = [style.linewidth.THICK]
VERYTHICK  = [style.linewidth.THICk]
THICK      = [style.linewidth.THIck]
NORMAL     = [style.linewidth.THick]
THIN       = [style.linewidth.Thick]
VERYTHIN   = [style.linewidth.normal]
ULTRATHIN  = [style.linewidth.thin]
SOLID      = [style.linestyle.solid]
DASHED     = [style.linestyle.dashed]
DOTTED     = [style.linestyle.dotted]
DASHDOTTED = [style.linestyle.dashdotted]

def FILLED(color):
    return [deco.filled([color])]
def COLOR(color):
    return [color]

# AUXILIARY FUNCTIONS
def w_point((x1,x2), (y1,y2), Wx, Wy): return ((Wx*x1+Wy*y1)/(Wx+Wy), (Wx*x2+Wy*y2)/(Wx+Wy))
def s_point((x1,x2), (y1,y2), W): return ((W*(y1-x1))+y1, (W*(y2-x2))+y2)
def r_point((p1,p2), (c1,c2), A): return (c1+(p1-c1)*cos(A)-(p2-c2)*sin(A), c2+(p1-c1)*sin(A)+(p2-c2)*cos(A))
def flip(P, A, B):
    M = ((A[0]+B[0])/2.0, (A[1]+B[1])/2.0)  # Midpoint of the A--B segment
    V = (A[1]-B[1], B[0]-A[0])              # Perpendicular to the A--B line
    W = (P[0]-M[0], P[1]-M[1])              # Vector M->P
    k = (V[0]*W[0] + V[1]*W[1]) / (V[0]*V[0] + V[1]*V[1])
    PPP = (M[0] + k*V[0], M[1] + k*V[1])  # Perpendicular Projection of P
    return (P[0] + 2*(PPP[0]-P[0]), P[1] + 2*(PPP[1]-P[1]))

################################################################################

# FIGURES
def figure000a():
    '''Tangram dels Cinc Triangles'''

    name = "figures/figure000a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(B, C, 1,1)
    F = w_point(A, C, 1,1)

    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*F),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*D),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure000b():
    '''Tangram de la Creu'''

    name = "figures/figure000b"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(C, E, 3,2)
    H = w_point(C, E, 1,4)
    I = w_point(A, F, 3,2)
    J = w_point(A, F, 1,4)

    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*F),
                              path.lineto(*J),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*J),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.lineto(*B),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure000c():
    '''Tangram de la Creu - Retícula'''

    name = "figures/figure000c"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(C, D, 1,1)
    H = w_point(D, A, 1,1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.moveto(*H),
                              path.lineto(*C),
                              path.moveto(*B),
                              path.lineto(*G),
                              path.moveto(*E),
                              path.lineto(*D)), BASE+THICK+COLOR(color.rgb.blue)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure000d():
    '''Tangram dels cinc triangles - Retícula'''

    name = "figures/figure000d"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    drawing = []
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*G),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D)), BASE+THICK+COLOR(color.rgb.blue)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*B),
                              path.moveto(*D),
                              path.lineto(*G),
                              path.moveto(*A),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*C)), BASE+THICK+COLOR(color.rgb.blue)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*C),
                              path.moveto(*B),
                              path.lineto(*D)), BASE+THICK+COLOR(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*G),
                              path.moveto(*F),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure000e():
    '''El Puzzle Egipci'''

    name = "figures/figure000e"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(C, E, 3,2)
    H = w_point(C, E, 1,4)
    I = w_point(A, F, 3,2)
    J = w_point(A, F, 1,4)
    K = w_point(A, B, 1,1)
    L = w_point(D, C, 1,1)
    M = w_point(J, B, 1,1)
    N = w_point(G, C, 1,1)
    O = w_point(I, J, 1,1)
    P = w_point(G, H, 1,1)
    Q = w_point(A, I, 1,1)
    R = w_point(H, D, 1,1)


    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*F),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*G),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*I),
                              path.lineto(*A),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*H),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*J),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*J),
                              path.lineto(*I),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*H),
                              path.lineto(*G),
                              path.lineto(*L),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*L),
                              path.moveto(*K),
                              path.lineto(*D),
                              path.moveto(*A),
                              path.lineto(*F),
                              path.moveto(*E),
                              path.lineto(*C),
                              path.moveto(*O),
                              path.lineto(*G)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure000f():
    '''El Puzzle Egipci'''

    name = "figures/figure000f"

    X = 2.0*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(E, D, 4,1)

    drawing = []
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*F),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(WHITE)))
    N   = 20
    eps = 0.02
    dX  = (1.0/N , -1.0/N)
    dY  = (1.0/N ,  1.0/N)
    for i in range(1,N*20):
        for j in range(1,N*20):
            P = (-2*X + i*dX[0] + j*dY[0], 0 + i*dX[1] + j*dY[1])
            if (2*P[0]+P[1] < (2-eps)*X and
                P[0]+2*P[1] > (1+eps)*X and
               -2*P[0]+P[1] < -eps*X):
                drawing.append((path.path(
                    path.moveto(*P),
                    path.closepath()), BASE+THIN+COLOR(BLACK)))

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*D),
                              path.lineto(*E)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure001a():
    '''The Egyptian Tangram'''

    name = "figures/figure001a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    drawing = []


    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C)), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E)), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F)), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.lineto(*D)), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I)), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure001b():
    '''Egyptian Tangram outline'''

    name = "figures/figure001b"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure001c():
    '''Egyptian Tangram outline minus one line'''

    name = "figures/figure001c"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure001d():
    '''Egyptian Tangram outline minus two lines'''

    name = "figures/figure001d"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    drawing = []

    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure001e():
    '''Egyptian Tangram outline minus three lines'''

    name = "figures/figure001e"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    drawing = []

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure001f():
    '''Egyptian Tangram outline plus 5x5 grid'''

    name = "figures/figure001f"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*w_point(A, D, 1,4)),
                              path.lineto(*w_point(B, C, 1,4)),
                              path.moveto(*w_point(A, D, 2,3)),
                              path.lineto(*w_point(B, C, 2,3)),
                              path.moveto(*w_point(A, D, 3,2)),
                              path.lineto(*w_point(B, C, 3,2)),
                              path.moveto(*w_point(A, D, 4,1)),
                              path.lineto(*w_point(B, C, 4,1)),
                              path.moveto(*w_point(A, B, 1,4)),
                              path.lineto(*w_point(D, C, 1,4)),
                              path.moveto(*w_point(A, B, 2,3)),
                              path.lineto(*w_point(D, C, 2,3)),
                              path.moveto(*w_point(A, B, 3,2)),
                              path.lineto(*w_point(D, C, 3,2)),
                              path.moveto(*w_point(A, B, 4,1)),
                              path.lineto(*w_point(D, C, 4,1))), BASE+DOTTED+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure001g():
    '''The Egyptian Tangram'''

    name = "figures/figure001g"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    drawing = []


    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E)), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*I),
                              path.lineto(*C)), BASE+THICK+FILLED(color.cmyk.SpringGreen)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure001h():
    '''The Egyptian Tangram'''

    name = "figures/figure001h"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    drawing = []


    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E)), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F)), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*I),
                              path.lineto(*C)), BASE+THICK+FILLED(color.cmyk.SpringGreen)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002a():
    '''Egyptian Tangram grid'''

    name = "figures/figure002a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK+COLOR(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002b():
    '''Egyptian Tangram grid outline'''

    name = "figures/figure002b"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002c():
    '''Egyptian Tangram grid outline'''

    name = "figures/figure002c"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    I = w_point(E, B, 2,3)
    J = w_point(G, D, 1,1)
    K = w_point(H, A, 2,3)
    L = w_point(A, G, 1,2)
    M = w_point(I, C, 1,1)
    N = w_point(B, E, 1,1)
    O = w_point(A, H, 1,4)
    P = w_point(A, H, 1,2)


    drawing = []

    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*N),
                              path.lineto(*K),
                              path.lineto(*A),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*O),
                              path.lineto(*P),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*L),
                              path.lineto(*M),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002d():
    '''Egyptian Tangram grid outline'''

    name = "figures/figure002d"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    I = w_point(B, E, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E)), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*C)), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F)), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002e():
    '''Egyptian Tangram grid outline plus 2x2 grid'''

    name = "figures/figure002e"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*w_point(A, D, 1,1)),
                              path.lineto(*w_point(B, C, 1,1)),
                              path.moveto(*w_point(A, B, 1,1)),
                              path.lineto(*w_point(D, C, 1,1))), BASE+DOTTED+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002f():
    '''Egyptian Tangram grid outline plus 3x3 grid'''

    name = "figures/figure002f"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*w_point(A, D, 1,2)),
                              path.lineto(*w_point(B, C, 1,2)),
                              path.moveto(*w_point(A, D, 2,1)),
                              path.lineto(*w_point(B, C, 2,1)),
                              path.moveto(*w_point(A, B, 1,2)),
                              path.lineto(*w_point(D, C, 1,2)),
                              path.moveto(*w_point(A, B, 2,1)),
                              path.lineto(*w_point(D, C, 2,1))), BASE+DOTTED+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002g():
    '''Egyptian Tangram grid outline plus 4x4 grid'''

    name = "figures/figure002g"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*w_point(A, D, 1,3)),
                              path.lineto(*w_point(B, C, 1,3)),
                              path.moveto(*w_point(A, D, 2,2)),
                              path.lineto(*w_point(B, C, 2,2)),
                              path.moveto(*w_point(A, D, 3,1)),
                              path.lineto(*w_point(B, C, 3,1)),
                              path.moveto(*w_point(A, B, 1,3)),
                              path.lineto(*w_point(D, C, 1,3)),
                              path.moveto(*w_point(A, B, 2,2)),
                              path.lineto(*w_point(D, C, 2,2)),
                              path.moveto(*w_point(A, B, 3,1)),
                              path.lineto(*w_point(D, C, 3,1))), BASE+DOTTED+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002h():
    '''Egyptian Tangram grid outline plus 5x5 grid'''

    name = "figures/figure002h"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*w_point(A, D, 1,4)),
                              path.lineto(*w_point(B, C, 1,4)),
                              path.moveto(*w_point(A, D, 2,3)),
                              path.lineto(*w_point(B, C, 2,3)),
                              path.moveto(*w_point(A, D, 3,2)),
                              path.lineto(*w_point(B, C, 3,2)),
                              path.moveto(*w_point(A, D, 4,1)),
                              path.lineto(*w_point(B, C, 4,1)),
                              path.moveto(*w_point(A, B, 1,4)),
                              path.lineto(*w_point(D, C, 1,4)),
                              path.moveto(*w_point(A, B, 2,3)),
                              path.lineto(*w_point(D, C, 2,3)),
                              path.moveto(*w_point(A, B, 3,2)),
                              path.lineto(*w_point(D, C, 3,2)),
                              path.moveto(*w_point(A, B, 4,1)),
                              path.lineto(*w_point(D, C, 4,1))), BASE+DOTTED+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002i():
    '''Egyptian Tangram grid colored'''

    name = "figures/figure002i"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*I),
                              path.lineto(*N),
                              path.lineto(*J),
                              path.lineto(*O),
                              path.lineto(*K),
                              path.lineto(*P),
                              path.lineto(*L),
                              path.lineto(*M),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*P),
                              path.lineto(*Q),
                              path.lineto(*L),
                              path.closepath(),
                              path.moveto(*L),
                              path.lineto(*R),
                              path.lineto(*M),
                              path.closepath(),
                              path.moveto(*M),
                              path.lineto(*S),
                              path.lineto(*I),
                              path.closepath(),
                              path.moveto(*I),
                              path.lineto(*T),
                              path.lineto(*N),
                              path.closepath(),
                              path.moveto(*N),
                              path.lineto(*U),
                              path.lineto(*J),
                              path.closepath(),
                              path.moveto(*J),
                              path.lineto(*V),
                              path.lineto(*O),
                              path.closepath(),
                              path.moveto(*O),
                              path.lineto(*W),
                              path.lineto(*K),
                              path.closepath(),
                              path.moveto(*K),
                              path.lineto(*Y),
                              path.lineto(*P),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*U),
                              path.lineto(*F),
                              path.closepath(),
                              path.moveto(*B),
                              path.lineto(*V),
                              path.lineto(*F),
                              path.closepath(),
                              path.moveto(*B),
                              path.lineto(*W),
                              path.lineto(*G),
                              path.closepath(),
                              path.moveto(*C),
                              path.lineto(*Y),
                              path.lineto(*G),
                              path.closepath(),
                              path.moveto(*C),
                              path.lineto(*Q),
                              path.lineto(*H),
                              path.closepath(),
                              path.moveto(*D),
                              path.lineto(*R),
                              path.lineto(*H),
                              path.closepath(),
                              path.moveto(*D),
                              path.lineto(*S),
                              path.lineto(*E),
                              path.closepath(),
                              path.moveto(*A),
                              path.lineto(*T),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*U),
                              path.lineto(*N),
                              path.lineto(*T),
                              path.closepath(),
                              path.moveto(*B),
                              path.lineto(*W),
                              path.lineto(*O),
                              path.lineto(*V),
                              path.closepath(),
                              path.moveto(*C),
                              path.lineto(*Q),
                              path.lineto(*P),
                              path.lineto(*Y),
                              path.closepath(),
                              path.moveto(*D),
                              path.lineto(*S),
                              path.lineto(*M),
                              path.lineto(*R),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*T),
                              path.lineto(*I),
                              path.lineto(*S),
                              path.closepath(),
                              path.moveto(*F),
                              path.lineto(*U),
                              path.lineto(*J),
                              path.lineto(*V),
                              path.closepath(),
                              path.moveto(*G),
                              path.lineto(*Y),
                              path.lineto(*K),
                              path.lineto(*W),
                              path.closepath(),
                              path.moveto(*H),
                              path.lineto(*R),
                              path.lineto(*L),
                              path.lineto(*Q),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002j():
    '''Egyptian Tangram grid colored'''

    name = "figures/figure002j"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)
    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*L),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002k():
    '''Egyptian Tangram grid colored'''

    name = "figures/figure002k"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)
    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*G),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*L),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*L),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*O),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure003a():
    '''El Tangram Egípci - Decomposat'''

    name = "figures/figure003a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(I, B, 1,1)
    K = w_point(I, C, 1,1)
    L = w_point(C, E, 3,2)
    M = w_point(B, E, 1,4)
    N = w_point(C, E, 1,4)
    O = w_point(A, M, 1,1)
    P = w_point(N, D, 1,1)
    drawing = []


    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C)), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E)), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F)), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.lineto(*D)), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I)), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*G),
                              path.lineto(*K),
                              path.lineto(*J),
                              path.moveto(*N),
                              path.lineto(*D),
                              path.moveto(*P),
                              path.lineto(*L),
                              path.lineto(*H),
                              path.lineto(*P),
                              path.moveto(*A),
                              path.lineto(*M),
                              path.moveto(*F),
                              path.lineto(*O),
                              path.lineto(*I)), BASE+THIN+DASHED))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure003b():
    '''Tangram de la Creu - Decomposat'''

    name = "figures/figure003b"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(C, E, 3,2)
    H = w_point(C, E, 1,4)
    I = w_point(A, F, 3,2)
    J = w_point(A, F, 1,4)
    K = w_point(A, B, 1,1)
    L = w_point(D, C, 1,1)
    M = w_point(J, B, 1,1)
    N = w_point(G, C, 1,1)
    O = w_point(I, J, 1,1)
    P = w_point(G, H, 1,1)
    Q = w_point(A, I, 1,1)
    R = w_point(H, D, 1,1)


    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*F),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*J),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*N),
                              path.lineto(*J),
                              path.moveto(*G),
                              path.lineto(*O),
                              path.lineto(*P),
                              path.lineto(*I),
                              path.lineto(*A),
                              path.moveto(*D),
                              path.lineto(*H),
                              path.lineto(*Q),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*L),
                              path.lineto(*R),
                              path.lineto(*G),
                              path.moveto(*K),
                              path.lineto(*I),
                              path.lineto(*M),
                              path.lineto(*K)), BASE+THIN+DASHED))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*H),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.moveto(*G),
                              path.lineto(*B)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure003c():
    '''Tangram Xinés - Decomposat'''

    name = "figures/figure003c"

    X = 3*R2
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(E, F, 1,1)
    H = w_point(A, C, 3,1)
    I = w_point(A, C, 1,1)
    J = w_point(A, C, 1,3)
    K = w_point(C, D, 1,1)
    L = w_point(D, A, 1,1)
    M = w_point(I, D, 1,1)

    drawing = []
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*C),
                              path.lineto(*J),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*I),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(PINK)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*D),
                              path.lineto(*I),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*I),
                              path.lineto(*H),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*H),
                              path.lineto(*G),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*G),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*M),
                              path.lineto(*J),
                              path.moveto(*E),
                              path.lineto(*L),
                              path.lineto(*K),
                              path.lineto(*J),
                              path.lineto(*G),
                              path.lineto(*B)), BASE+THIN+DASHED))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004a():
    '''T1+T4+T5 - Figura a'''

    name = "figures/figure004a"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,1*X*R5)
    C = (2*X*R5,1*X*R5)
    D = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004b():
    '''T1+T4+T5 - Figura b'''

    name = "figures/figure004b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,2*X)
    C = (5*X,2*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004c():
    '''T1+T4+T5 - Figura c'''

    name = "figures/figure004c"

    X = 1 # Scale #
    A = (     0,     0)
    B = (1*X*R5,2*X*R5)
    C = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004d():
    '''T1+T4+T5 - Figura d'''

    name = "figures/figure004d"

    X = 1 # Scale #
    A = (     0,     0)
    B = (2*X*R5,1*X*R5)
    C = (4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004e():
    '''T1+T4+T5 - Figura e'''

    name = "figures/figure004e"

    X = 1 # Scale #
    A = (  0,  0)
    B = (1*X,2*X)
    C = (5*X,2*X)
    D = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004f():
    '''T1+T4+T5 - Figura f'''

    name = "figures/figure004f"

    X = 1 # Scale #
    A = (  0,  0)
    B = (4*X,2*X)
    C = (5*X,2*X)
    D = (9*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004g():
    '''T1+T4+T5 - Figura g'''

    name = "figures/figure004g"

    X = 1 # Scale #
    A = (   0,  0)
    B = (   0,4*X)
    C = (-1*X,4*X)
    D = (-4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004h():
    '''T1+T4+T5 - Figura h'''

    name = "figures/figure004h"

    X = 1 # Scale #
    A = (  0,  0)
    B = (1*X,2*X)
    C = (6*X,2*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004i():
    '''T1+T4+T5 - Figura i'''

    name = "figures/figure004i"

    X = 1 # Scale #
    A = (  0,  0)
    B = (4*X,2*X)
    C = (9*X,2*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004j():
    '''T1+T4+T5 - Figura j'''

    name = "figures/figure004j"

    X = 1 # Scale #
    A = (  0,4*X)
    B = (2*X,5*X)
    C = (4*X,4*X)
    D = (2*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004k():
    '''T1+T4+T5 - Figura k'''

    name = "figures/figure004k"

    X = 1.0 # Scale #
    A = (   0,  0)
    B = (-2*X,  0)
    C = (-2*X,4*X)
    D = (   0,5*X)

    E = w_point(C,D, 1,4)
    F = s_point((0,4*X),E, 1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*F),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004l():
    '''T1+T4+T5 - Figura l'''

    name = "figures/figure004l"

    X = 1.0 # Scale #
    A = (0*X*R5, 0*X*R5)
    B = (3*X*R5, 0*X*R5)
    C = (1*X*R5, 1*X*R5)
    D = (1*X*R5, 2*X*R5)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004m():
    '''T1+T4+T5 - Figura m'''

    name = "figures/figure004m"

    X = 1.0 # Scale #
    A = (0*X, 0*X)
    B = (5*X, 0*X)
    C = (5*X, 2*X)
    D = (0*X, 2*X)
    E = (1*X, 2*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure005a():
    '''T1+T4+T5 - Pythagoras of T5'''

    name = "figures/figure005a"

    X = 1.0 # Scale #
    A = (      0,      0)
    B = (-1*X*R5,      0)
    C = (      0, 2*X*R5)

    D = (-1*X*R5, 2*X*R5)
    E = ( 4*X/R5, 2*X/R5)
    F = s_point(E, A, 1)

    drawing = []
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure005b():
    '''T1+T4+T5 - Pythagoras of T4'''

    name = "figures/figure005b"

    X = 1.0 # Scale #
    A = (   0,   0)
    B = (-2*X,   0)
    C = (   0, 4*X)

    E = ( 2*X,  4*X)
    F = (   0, -1*X)
    D = s_point(F,B, 1.0)

    drawing = []
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure005c():
    '''T1+T4+T5 - Pythagoras of T1'''

    name = "figures/figure005c"

    X = 1.0 # Scale #
    A = (   0,   0)
    B = (-1*X,   0)
    C = (   0, 2*X)

    D = (-5*X,  2*X)
    E = ( 4*X,  2*X)
    F = (   0, -2*X)

    drawing = []
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006a():
    '''1:2:sqrt(5) inradius'''

    name = "figures/figure006a"

    X   = 1.0 # Scale #
    PHI = (1.0+R5)/2.0
    A   = (             0,             0)
    B   = (             0, 1*(PHI+1.0)*X)
    C   = ( 2*(PHI+1.0)*X,             0)
    D   = w_point(B,C, PHI+1,1.0)

    drawing = []

    drawing.append((path.circle(X, X, X), BASE))
    drawing.append((path.path(path.moveto(X,X),
                              path.lineto(X,0),
                              path.moveto(X,X),
                              path.lineto(0,X),
                              path.moveto(X,X),
                              path.lineto(*D)), BASE+DASHED+VERYTHIN))

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006b():
    '''3:4:5 inradius'''

    name = "figures/figure006b"

    X   = 1.0 # Scale #
    A   = (  0,   0)
    B   = (  0, 3*X)
    C   = (4*X,   0)
    D   = w_point(B,C, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.circle(X, X, X), BASE))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(X,X),
                              path.lineto(0,X),
                              path.closepath()), BASE+FILLED(RED)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006c():
    '''3:4:5 dissection'''

    name = "figures/figure006c"

    X   = 1.0 # Scale #
    A   = (  0,   0)
    B   = (  0, 3*X)
    C   = (4*X,   0)
    D   = w_point(B,C, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))
    drawing.append((path.circle(X, X, X), BASE+DASHED+VERYTHIN))
    drawing.append((path.path(path.moveto(X,X),
                              path.lineto(X,0),
                              path.moveto(X,X),
                              path.lineto(0,X),
                              path.moveto(X,X),
                              path.lineto(*D),
                              path.moveto(X,X),
                              path.lineto(*C),
                              path.moveto(X,X),
                              path.lineto(*B),
                              path.moveto(X,X),
                              path.lineto(*A)), BASE+THIN))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006d():
    '''3:4:5 dissection'''

    name = "figures/figure006d"

    X   = 1.0 # Scale #
    A   = (  0,   0)
    B   = (  0, 3*X)
    C   = (4*X,   0)
    D   = w_point(B,C, 2,3)
    E   = w_point(A,C, 2.5,1.5)

    drawing = []
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+ULTRATHIN+[deco.filled([YELLOW, color.transparency(0.90)])]+[YELLOW, color.transparency(0.90)]))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+ULTRATHIN+[deco.filled([BLUE, color.transparency(0.90)])]+[BLUE, color.transparency(0.90)]))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+ULTRATHIN+[deco.filled([BLUE, color.transparency(0.90)])]+[BLUE, color.transparency(0.90)]))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*D)), BASE+THIN+DASHED))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006e():
    '''1:2:sqrt(5) dissection'''

    name = "figures/figure006e"

    X   = 1.0 # Scale #
    PHI = (1.0+R5)/2.0
    A   = (             0,             0)
    B   = (             0, 1*(PHI+1.0)*X)
    C   = ( 2*(PHI+1.0)*X,             0)
    D   = w_point(B,C, 1,1)
    E   = w_point(A,C, 5,3)

    drawing = []

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+ULTRATHIN+[deco.filled([YELLOW, color.transparency(0.90)])]+[YELLOW, color.transparency(0.90)]))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+ULTRATHIN+[deco.filled([BLUE, color.transparency(0.90)])]+[BLUE, color.transparency(0.90)]))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+ULTRATHIN+[deco.filled([BLUE, color.transparency(0.90)])]+[BLUE, color.transparency(0.90)]))

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*D)), BASE+THIN+DASHED))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006f():
    '''1:2:sqrt(5) dissection'''

    name = "figures/figure006f"

    X = 1.0 # Scale #
    A = (  0,   0)
    B = (  0, 4*X)
    C = (8*X,   0)
    D = w_point(B,C, 1,1)
    E = w_point(A,C, 5,3)
    F = w_point(B,E, 1,4)

    drawing = []

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*B),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006g():
    '''Pinwheel tiling'''

    name = "figures/figure006g"

    def pinwheel(A, B, C, depth):
        output = [(A, B, C, depth)]
        if depth > 0:
            D = w_point(B,C, 4,1)
            E = w_point(D,C, 1,1)
            F = w_point(A,C, 1,1)
            G = w_point(A,D, 1,1)
            output.extend(pinwheel(D,B,A,depth-1))
            output.extend(pinwheel(E,F,D,depth-1))
            output.extend(pinwheel(G,D,F,depth-1))
            output.extend(pinwheel(G,A,F,depth-1))
            output.extend(pinwheel(E,F,C,depth-1))
        return output


    X = 1.0 # Scale #
    A = (  0,   0)
    B = (  0, 4*X)
    C = (8*X,   0)
    S = [ULTRATHIN, VERYTHIN, VERYTHICK, VERYTHICK]

    drawing = []
    for P,Q,R,s in pinwheel(A, B, C, 3):
        drawing.append((path.path(path.moveto(*P),
                                  path.lineto(*Q),
                                  path.lineto(*R),
                                  path.closepath()), BASE+S[s]))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006h():
    '''Pinwheel Franctal'''

    name = "figures/figure006h"

    def pinwheel(A, B, C, depth):
        output = [(A, B, C, depth)]
        if depth > 0:
            D = w_point(B,C, 4,1)
            E = w_point(D,C, 1,1)
            F = w_point(A,C, 1,1)
            G = w_point(A,D, 1,1)
            output.extend(pinwheel(D,B,A,depth-1))
            output.extend(pinwheel(E,F,D,depth-1))
            output.extend(pinwheel(G,A,F,depth-1))
            output.extend(pinwheel(E,F,C,depth-1))
        return output


    X = 1.0 # Scale #
    A = (  0,   0)
    B = (  0, 4*X)
    C = (8*X,   0)
    S = [ULTRATHIN+DOTTED, ULTRATHIN, VERYTHIN, THIN, NORMAL, THICK]

    drawing = []
    for P,Q,R,s in pinwheel(A, B, C, 5):
        drawing.append((path.path(path.moveto(*P),
                                  path.lineto(*Q),
                                  path.lineto(*R),
                                  path.closepath()), BASE+S[s]))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006i():
    '''1:2:sqrt(5) dissection'''

    name = "figures/figure006i"

    X   = 1.0 # Scale #
    PHI = (1.0+R5)/2.0
    A   = (             0,             0)
    B   = (             0, 1*(PHI+1.0)*X)
    C   = ( 2*(PHI+1.0)*X,             0)
    D   = w_point(B,C, 3,2)
    E   = w_point(A,C, 3,1)

    drawing = []

    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*B),
                              path.lineto(*D),
                              path.closepath()), BASE+ULTRATHIN+[deco.filled([YELLOW, color.transparency(0.90)])]+[YELLOW, color.transparency(0.90)]))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+ULTRATHIN+[deco.filled([BLUE, color.transparency(0.90)])]+[BLUE, color.transparency(0.90)]))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+ULTRATHIN+[deco.filled([BLUE, color.transparency(0.90)])]+[BLUE, color.transparency(0.90)]))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*D)), BASE+THIN+DASHED))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure007a():
    '''Q4 with angles'''

    name = "figures/figure007a"

    X = 1.0 # Scale #
    A = ( 0, 0)
    B = ( 0, R5*X)
    C = w_point(B, (R5*X*2,R5*X*2), 4,1)
    D = ( R5*X,0)
    E = ( 0, R5*X*2)

    drawing = []

    #drawing.append((path.path(path.moveto(*C), path.arc(C[0],C[1], X/2.0, 180, 360)), BASE+COLOR(BLUE)))

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*D)), BASE+DASHED+THIN))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*A),
                              path.lineto(*D),
                              path.closepath()), BASE+DASHED+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure007b():
    '''Golden Rombus with angles'''

    name = "figures/figure007b"

    X = 1.0 # Scale #
    Y = (1.0+R5)/2.0
    A = (-X, 0)
    B = ( 0, Y)
    C = ( X, 0)
    D = ( 0,-Y)

    drawing = []

    #drawing.append((path.path(path.moveto(*C), path.arc(C[0],C[1], X/2.0, 180, 360)), BASE+COLOR(BLUE)))

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*D)), BASE+DASHED+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*C)), BASE+DASHED+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008ag():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008ag"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*V),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*V),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*F),
                              path.lineto(*V),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008bg():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008bg"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*O),
                              path.lineto(*G),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*M),
                              path.lineto(*H),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*G),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*M),
                              path.lineto(*E),
                              path.lineto(*A),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*O),
                              path.lineto(*C),
                              path.lineto(*M),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008cg():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008cg"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*I),
                              path.lineto(*N),
                              path.lineto(*J),
                              path.lineto(*O),
                              path.lineto(*K),
                              path.lineto(*P),
                              path.lineto(*L),
                              path.lineto(*M),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*T),
                              path.lineto(*I),
                              path.lineto(*S),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*U),
                              path.lineto(*F),
                              path.lineto(*V),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*Y),
                              path.lineto(*G),
                              path.lineto(*W),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*L),
                              path.lineto(*R),
                              path.lineto(*H),
                              path.lineto(*Q),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*U),
                              path.lineto(*A),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*V),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*Q),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*R),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*Y),
                              path.lineto(*P),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*O),
                              path.lineto(*W),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*M),
                              path.lineto(*I),
                              path.lineto(*S),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*T),
                              path.lineto(*I),
                              path.lineto(*N),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*N),
                              path.lineto(*U),
                              path.lineto(*A),
                              path.lineto(*T),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*V),
                              path.lineto(*O),
                              path.lineto(*W),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*P),
                              path.lineto(*Y),
                              path.lineto(*C),
                              path.lineto(*Q),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*M),
                              path.lineto(*R),
                              path.lineto(*D),
                              path.lineto(*S),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008dg():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008dg"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*K),
                              path.lineto(*Y),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*L),
                              path.lineto(*R),
                              path.lineto(*H),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*I),
                              path.lineto(*T),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*A),
                              path.lineto(*F),
                              path.lineto(*V),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*V),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*Y),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*R),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*T),
                              path.lineto(*E),
                              path.lineto(*A),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*R),
                              path.lineto(*I),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*T),
                              path.lineto(*A),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*V),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*Y),
                              path.lineto(*L),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008eg():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008eg"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*A),
                              path.lineto(*O),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*L),
                              path.lineto(*Y),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*O),
                              path.lineto(*Y),
                              path.lineto(*L),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*Y),
                              path.lineto(*O),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*L),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008fg():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008fg"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*A),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*P),
                              path.lineto(*W),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*Q),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*P),
                              path.lineto(*Q),
                              path.lineto(*C),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*W),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*E),
                              path.lineto(*A),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*L),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*P),
                              path.lineto(*Q),
                              path.lineto(*L),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*W),
                              path.lineto(*J),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008gg():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008gg"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*K),
                              path.lineto(*Q),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*O),
                              path.lineto(*W),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*U),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*M),
                              path.lineto(*I),
                              path.lineto(*S),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*W),
                              path.lineto(*K),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*S),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*U),
                              path.lineto(*I),
                              path.lineto(*M),
                              path.lineto(*Q),
                              path.lineto(*K),
                              path.lineto(*O),
                              path.closepath()), BASE+THICK+FILLED(D_GREEN)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*D),
                              path.lineto(*S),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*M),
                              path.lineto(*Q),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*U),
                              path.lineto(*O),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*W),
                              path.lineto(*G),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008ak():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008ak"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*V),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*F),
                              path.lineto(*V),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008bk():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008bk"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*O),
                              path.lineto(*G),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*M),
                              path.lineto(*H),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*O),
                              path.lineto(*C),
                              path.lineto(*M),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008ck():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008ck"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*I),
                              path.lineto(*N),
                              path.lineto(*J),
                              path.lineto(*O),
                              path.lineto(*K),
                              path.lineto(*P),
                              path.lineto(*L),
                              path.lineto(*M),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*T),
                              path.lineto(*I),
                              path.lineto(*S),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*U),
                              path.lineto(*F),
                              path.lineto(*V),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*Y),
                              path.lineto(*G),
                              path.lineto(*W),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*L),
                              path.lineto(*R),
                              path.lineto(*H),
                              path.lineto(*Q),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*N),
                              path.lineto(*U),
                              path.lineto(*A),
                              path.lineto(*T),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*V),
                              path.lineto(*O),
                              path.lineto(*W),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*P),
                              path.lineto(*Y),
                              path.lineto(*C),
                              path.lineto(*Q),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*M),
                              path.lineto(*R),
                              path.lineto(*D),
                              path.lineto(*S),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008dk():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008dk"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*K),
                              path.lineto(*Y),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*L),
                              path.lineto(*R),
                              path.lineto(*H),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*I),
                              path.lineto(*T),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*A),
                              path.lineto(*F),
                              path.lineto(*V),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*R),
                              path.lineto(*I),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*T),
                              path.lineto(*A),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*V),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*Y),
                              path.lineto(*L),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008ek():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008ek"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*A),
                              path.lineto(*O),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*L),
                              path.lineto(*Y),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*Y),
                              path.lineto(*O),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*L),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008fk():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008fk"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*A),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*P),
                              path.lineto(*W),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*Q),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*L),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*P),
                              path.lineto(*Q),
                              path.lineto(*L),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*W),
                              path.lineto(*J),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008gk():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008gk"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*K),
                              path.lineto(*Q),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*O),
                              path.lineto(*W),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*U),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*M),
                              path.lineto(*I),
                              path.lineto(*S),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*D),
                              path.lineto(*S),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*M),
                              path.lineto(*Q),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*U),
                              path.lineto(*O),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*W),
                              path.lineto(*G),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008ab():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008ab"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*V),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*F),
                              path.lineto(*V),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008bb():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008bb"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*G),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*M),
                              path.lineto(*E),
                              path.lineto(*A),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*O),
                              path.lineto(*C),
                              path.lineto(*M),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008cb():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008cb"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*I),
                              path.lineto(*N),
                              path.lineto(*J),
                              path.lineto(*O),
                              path.lineto(*K),
                              path.lineto(*P),
                              path.lineto(*L),
                              path.lineto(*M),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*T),
                              path.lineto(*I),
                              path.lineto(*S),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*U),
                              path.lineto(*F),
                              path.lineto(*V),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*Y),
                              path.lineto(*G),
                              path.lineto(*W),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*L),
                              path.lineto(*R),
                              path.lineto(*H),
                              path.lineto(*Q),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*U),
                              path.lineto(*A),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*V),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*Q),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*R),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*Y),
                              path.lineto(*P),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*O),
                              path.lineto(*W),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*M),
                              path.lineto(*I),
                              path.lineto(*S),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*T),
                              path.lineto(*I),
                              path.lineto(*N),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008db():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008db"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*V),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*Y),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*R),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*T),
                              path.lineto(*E),
                              path.lineto(*A),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*R),
                              path.lineto(*I),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*T),
                              path.lineto(*A),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*V),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*Y),
                              path.lineto(*L),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008eb():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008eb"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*O),
                              path.lineto(*Y),
                              path.lineto(*L),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*Y),
                              path.lineto(*O),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*L),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008fb():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008fb"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*P),
                              path.lineto(*Q),
                              path.lineto(*C),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*W),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*E),
                              path.lineto(*A),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*L),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*P),
                              path.lineto(*Q),
                              path.lineto(*L),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*W),
                              path.lineto(*J),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008gb():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008gb"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*W),
                              path.lineto(*K),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*S),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*U),
                              path.lineto(*I),
                              path.lineto(*M),
                              path.lineto(*Q),
                              path.lineto(*K),
                              path.lineto(*O),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*D),
                              path.lineto(*S),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*M),
                              path.lineto(*Q),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*U),
                              path.lineto(*O),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*W),
                              path.lineto(*G),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008ay():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008ay"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*V),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*V),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008by():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008by"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*O),
                              path.lineto(*G),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*M),
                              path.lineto(*H),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*G),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*M),
                              path.lineto(*E),
                              path.lineto(*A),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008cy():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008cy"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*U),
                              path.lineto(*A),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*V),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*Q),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*R),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*Y),
                              path.lineto(*P),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*O),
                              path.lineto(*W),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*M),
                              path.lineto(*I),
                              path.lineto(*S),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*T),
                              path.lineto(*I),
                              path.lineto(*N),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*N),
                              path.lineto(*U),
                              path.lineto(*A),
                              path.lineto(*T),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*V),
                              path.lineto(*O),
                              path.lineto(*W),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*P),
                              path.lineto(*Y),
                              path.lineto(*C),
                              path.lineto(*Q),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*M),
                              path.lineto(*R),
                              path.lineto(*D),
                              path.lineto(*S),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008dy():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008dy"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*K),
                              path.lineto(*Y),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*L),
                              path.lineto(*R),
                              path.lineto(*H),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*I),
                              path.lineto(*T),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*A),
                              path.lineto(*F),
                              path.lineto(*V),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*V),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*Y),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*R),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*T),
                              path.lineto(*E),
                              path.lineto(*A),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008ey():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008ey"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*A),
                              path.lineto(*O),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*L),
                              path.lineto(*Y),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*O),
                              path.lineto(*Y),
                              path.lineto(*L),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008fy():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008fy"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*A),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*P),
                              path.lineto(*W),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*Q),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*P),
                              path.lineto(*Q),
                              path.lineto(*C),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*W),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*E),
                              path.lineto(*A),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure008gy():
    '''Egyptian Tangram carpets'''

    name = "figures/figure008gy"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*K),
                              path.lineto(*Q),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*O),
                              path.lineto(*W),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*U),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*M),
                              path.lineto(*I),
                              path.lineto(*S),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*W),
                              path.lineto(*K),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*S),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*U),
                              path.lineto(*I),
                              path.lineto(*M),
                              path.lineto(*Q),
                              path.lineto(*K),
                              path.lineto(*O),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure009():
    '''El Tangram Egípci - 5 cercles notables'''

    name = "figures/figure009"

    X = 2.0*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(F, B, 1,1)

    C1 = w_point(C, E, 1,1)
    C2 = w_point(F, E, 1,1)
    C3 = G
    C4 = D

    drawing = []
    #drawing.append((path.path(path.moveto(*F), path.arc(J[0], J[1], X/4.0, 270, 90)), BASE+THICK+COLOR(PLUM)))
    drawing.append((path.circle(J[0], J[1], X/4), BASE+THICK+COLOR(PLUM)))

    #drawing.append((path.circle(X, 0, X), BASE+THICK+COLOR(color.rgb.blue)))
    drawing.append((path.path(path.moveto(*C), path.arc(X,0, X, 90, 180)), BASE+THICK+COLOR(color.rgb.blue)))

    #drawing.append((path.circle(X/2.0,X,X/2.0), BASE+THICK+COLOR(color.rgb.green)))
    drawing.append((path.path(path.moveto(*B), path.arc(X/2.0,X, X/2.0, 180, 360)), BASE+THICK+COLOR(color.rgb.green)))

    drawing.append((path.circle(C2[0], C2[1], X/(2*R2)), BASE+THICK+COLOR(ORANGE)))

    drawing.append((path.circle(C1[0], C1[1], X*R5/4.0), BASE+THICK+COLOR(color.rgb.red)))

    #drawing.append((path.path(path.moveto(X/2.0, X/2.0),path.lineto(X/2.0, X/2.0)), BASE+THICK))
    #drawing.append((path.path(path.moveto(X/2.0, X/2.0),path.lineto(X/2.0, X/2.0)), BASE+THICK))
    #drawing.append((path.path(path.moveto(X/2.0, X/2.0),path.lineto(X/2.0, X/2.0)), BASE+THICK))
    #drawing.append((path.path(path.moveto(X/2.0, X/2.0),path.lineto(X/2.0, X/2.0)), BASE+THICK))

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure009b():
    '''El Tangram Egípci - El quadrilater es ciclic'''

    name = "figures/figure009b"

    X = 2.0*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(F, B, 1,1)

    C1 = w_point(C, E, 1,1)
    C2 = w_point(F, E, 1,1)
    C3 = G
    C4 = D

    drawing = []
    drawing.append((path.circle(C2[0], C2[1], X/(2*R2)), BASE+COLOR(ORANGE)))
    drawing.append((path.circle(C1[0], C1[1], X*R5/4.0), BASE+COLOR(color.cmyk.SpringGreen)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure009c():
    '''El Tangram Egípci - 4 circumcircles'''

    name = "figures/figure009c"

    X = 2.0*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(F, B, 1,1)

    C1 = w_point(C, E, 1,1)
    C2 = w_point(F, E, 1,1)
    C3 = G
    C4 = D

    drawing = []
    drawing.append((path.circle(J[0], J[1], X/4), BASE+COLOR(RED)))

    drawing.append((path.path(path.moveto(*B), path.arc(X/2.0,X, X/2.0, 180, 360)), BASE+COLOR(BLUE)))

    drawing.append((path.circle(C2[0], C2[1], X/(2*R2)), BASE+COLOR(ORANGE)))

    drawing.append((path.circle(C1[0], C1[1], X*R5/4.0), BASE+COLOR(color.cmyk.SpringGreen)))

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure009d():
    '''El Tangram Egípci - 2 tangent circles'''

    name = "figures/figure009d"

    X = 2.0*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(F, B, 1,1)

    C1 = w_point(C, E, 1,1)
    C2 = w_point(F, E, 1,1)
    C3 = G
    C4 = D

    drawing = []
    drawing.append((path.circle(J[0], J[1], X/4), BASE+COLOR(RED)))
    drawing.append((path.path(path.moveto(*C), path.arc(X,0, X, 90, 180)), BASE+COLOR(PLUM)))

    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*J)), BASE+THIN+DASHED))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure009e():
    '''El Tangram Egípci - 1 tangent circle'''

    name = "figures/figure009e"

    X = 2.0*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(F, B, 1,1)

    C1 = w_point(C, E, 1,1)
    C2 = w_point(F, E, 1,1)
    C3 = G
    C4 = D

    drawing = []
    drawing.append((path.path(path.moveto(*B), path.arc(X/2.0,X, X/2.0, 180, 360)), BASE+COLOR(BLUE)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*J),
                              path.lineto(*A),
                              path.closepath()), BASE+ULTRATHIN+[deco.filled([YELLOW, color.transparency(0.85)])]+[YELLOW, color.transparency(0.85)]))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*J)), BASE+THIN+DASHED))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure009f():
    '''The Egyptian Tangram'''

    name = "figures/figure009f"

    X   = 2*R5
    PHI = X*(1.0+R5)/2.0

    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    O = w_point(C,(0,2*X-PHI), 1,1)
    R = 2*(X-O[1])/(1.0+R5)
    drawing = []

    drawing.append((path.circle(X/2.0, X/2.0, X/2.0), BASE+COLOR(GREEN)))
    drawing.append((path.circle(O[0], O[1], X-O[1]), BASE+COLOR(GREEN)))
    drawing.append((path.circle(X-R, R, R), BASE+COLOR(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure009g():
    '''El Tangram Egípci - 2 circumcircles and 1 incircle'''

    name = "figures/figure009g"

    X = 2.0*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(F, B, 1,1)

    C1 = w_point(C, E, 1,1)
    C2 = w_point(F, E, 1,1)
    C3 = G
    C4 = D

    drawing = []

    drawing.append((path.path(path.moveto(*B), path.arc(X/2.0,X, X/2.0, 180, 360)), BASE+COLOR(BLUE)))

    drawing.append((path.circle(C2[0], C2[1], X/(2*R2)), BASE+COLOR(ORANGE)))

    drawing.append((path.circle(X/2.0, X/2.0, X/(2.0*R5)), BASE+COLOR(YELLOW)))

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure009h():
    '''The Egyptian Tangram'''

    name = "figures/figure009h"

    X   = 2*R5
    PHI = (1.0+R5)/2.0

    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    O = (I[0] + (I[0]-X/2.0)/(PHI*PHI), I[1] + (I[1]-X/2.0)/(PHI*PHI))
    drawing = []

    drawing.append((path.circle(X/2.0, X/2.0, X/(2*R5)), BASE+COLOR(YELLOW)))
    drawing.append((path.circle(O[0], O[1], X/(2*R5*PHI*PHI)), BASE+COLOR(RED)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


    """
    >>> for x in X: print x, "->", x*phi, "->", x*phi*phi
    ...
    0.38 -> 0.614852915725 -> 0.994852915725
    0.76 -> 1.22970583145  -> 1.98970583145
    0.85 -> 1.37532889044  -> 2.22532889044
    1.00 -> 1.61803398875  -> 2.61803398875
    1.38 -> 2.23288690447  -> 3.61288690447
    2.24 -> 3.6243961348   -> 5.8643961348

    """


def figure009i():
    '''The Egyptian Tangram'''

    name = "figures/figure009i"

    X   = 2*R5
    PHI = (1.0+R5)/2.0

    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    O = (X/2.0, X/2.0 - 1.0 - X/(2*R5*PHI*PHI))

    drawing = []

    drawing.append((path.circle(O[0], O[1], X/(2*R5*PHI*PHI)), BASE+COLOR(RED)))
    drawing.append((path.circle(X/2.0, X/2.0, X/(2*R5)), BASE+COLOR(YELLOW)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


    """
    >>> for x in X: print x, "->", x*phi, "->", x*phi*phi
    ...
    0.38 -> 0.614852915725 -> 0.994852915725
    0.76 -> 1.22970583145  -> 1.98970583145
    0.85 -> 1.37532889044  -> 2.22532889044
    1.00 -> 1.61803398875  -> 2.61803398875
    1.38 -> 2.23288690447  -> 3.61288690447
    2.24 -> 3.6243961348   -> 5.8643961348

    """


def figure010a():
    '''T1+Q4'''

    name = "figures/figure010a"

    X = 2*R5
    A = (0,0)
    B = (X/2.0,0)
    C = (0,X)
    D = w_point(A, C, 1,1)
    E = w_point(B, C, 2,3)
    F = w_point(B, C, 4,1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure010b():
    '''T5'''

    name = "figures/figure010b"

    X = 2*R5
    A = (0,0)
    B = (X/2.0,0)
    C = (0,X)
    D = w_point(A, C, 1,1)
    E = w_point(B, C, 2,3)
    F = w_point(B, C, 4,1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure010c():
    '''T1+T4'''

    name = "figures/figure010c"

    X = 2*R5
    A = (0,0)
    B = (X/2.0,0)
    C = (0,X)
    D = w_point(A, C, 1,1)
    E = w_point(B, C, 2,3)
    F = w_point(B, C, 4,1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*C),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure010d():
    '''T1+Q4+T5'''

    name = "figures/figure010d"

    X = 2*R5
    A = (0,0)
    B = (X,0)
    C = (X/2.0,X)
    D = w_point(A, B, 1,1)
    E = w_point(C, D, 1,1)
    F = w_point(B, C, 2,3)
    G = w_point(A, C, 3,2)

    drawing = []
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure010e():
    '''T4+T6'''

    name = "figures/figure010e"

    X = 2*R5
    A = (0,0)
    B = (X,0)
    C = (X/2.0,X)
    D = w_point(A, B, 1,1)
    E = w_point(C, D, 1,1)
    F = w_point(B, C, 2,3)
    G = w_point(A, C, 3,2)

    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*G),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure010f():
    '''T1+Q4+T5'''

    name = "figures/figure010f"

    X = 2*R5
    A = (X,0)
    B = (0,0)
    C = (X/2.0,X)
    D = w_point(A, B, 1,1)
    E = w_point(C, D, 1,1)
    F = w_point(B, C, 2,3)
    G = w_point(A, C, 3,2)

    drawing = []
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure010g():
    '''T4+T6'''

    name = "figures/figure010g"

    X = 2*R5
    A = (X,0)
    B = (0,0)
    C = (X/2.0,X)
    D = w_point(A, B, 1,1)
    E = w_point(C, D, 1,1)
    F = w_point(B, C, 2,3)
    G = w_point(A, C, 3,2)

    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*G),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure010h():
    '''T6+Q4'''

    name = "figures/figure010h"

    X = 2*R5
    A = (0,0)
    B = (X/2.0,0)
    C = (X,X)
    D = (0,X/2.0)
    E = w_point(C, D, 1,4)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure010i():
    '''T6+Q4'''

    name = "figures/figure010i"

    X = 2*R5
    A = (0,0)
    B = (0,X/2.0)
    C = (X,X)
    D = (X/2.0,0)
    E = w_point(C, D, 1,4)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure010j():
    '''T1+T4+T5+Q4'''

    name = "figures/figure010j"

    X = 1.0 # Scale!
    A = (0  ,X*2)
    B = (0  ,X*0)
    C = (X*7,X*0)
    D = (X*7,X*2)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 5,2)
    G = w_point(D, A, 3,4)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure010k():
    '''T1+T4+T5+Q4'''

    name = "figures/figure010k"

    X = 1.0 # Scale!
    A = (X*7,X*2)
    B = (X*7,X*0)
    C = (X*0,X*0)
    D = (X*0,X*2)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 5,2)
    G = w_point(D, A, 3,4)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure010l():
    '''T1+T4+T5+Q4'''

    name = "figures/figure010l"

    X = 1.0 # Scale!
    A = (0  ,X*0)
    B = (0  ,X*2)
    C = (X*7,X*2)
    D = (X*7,X*0)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 5,2)
    G = w_point(D, A, 3,4)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure010m():
    '''T1+T4+T5+Q4'''

    name = "figures/figure010m"

    X = 1.0 # Scale!
    A = (X*7,X*0)
    B = (X*7,X*2)
    C = (X*0,X*2)
    D = (X*0,X*0)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 5,2)
    G = w_point(D, A, 3,4)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure011a():
    '''El Tangram Egípci - Quadrat 1'''

    name = "figures/figure011a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(C, E, 3,2)
    K = w_point(C, E, 1,4)
    drawing = []


    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure011b():
    '''El Tangram Egípci - Quadrat 2'''

    name = "figures/figure011b"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(C, E, 3,2)
    K = w_point(C, E, 1,4)
    drawing = []


    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*J),
                              path.lineto(*H),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*H),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*H),
                              path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure011c():
    '''El Tangram Egípci - Quadrat 3'''

    name = "figures/figure011c"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(C, E, 3,2)
    K = w_point(C, E, 1,4)
    drawing = []


    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.lineto(*I)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012a():
    '''El Tangram Egípci - Figura 1'''

    name = "figures/figure012a"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,2*X*R5)
    D = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012b():
    '''El Tangram Egípci - Figura 2'''

    name = "figures/figure012b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (5*X,4*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012c():
    '''El Tangram Egípci - Figura 3'''

    name = "figures/figure012c"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (4*X,4*X)
    D = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012d():
    '''El Tangram Egípci - Figura 4'''

    name = "figures/figure012d"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (2*X,4*X)
    D = (6*X,2*X)
    E = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012e():
    '''El Tangram Egípci - Figura 5'''

    name = "figures/figure012e"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (4*X,4*X)
    D = (4*X,2*X)
    E = (6*X,2*X)
    F = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012f():
    '''El Tangram Egípci - Figura 6'''

    name = "figures/figure012f"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (3*X,4*X)
    D = (3*X,5*X)
    E = (5*X,5*X)
    F = (5*X,2*X)
    G = (4*X,2*X)
    H = (4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012g():
    '''El Tangram Egípci - Figura 7'''

    name = "figures/figure012g"

    X = 1 # Scale #
    A = (  0,  0)
    B = (3*X,4*X)
    C = (5*X,4*X)
    D = (8*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012h():
    '''El Tangram Egípci - Figura 8'''

    name = "figures/figure012h"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (5*X,4*X)
    D = (7*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012i():
    '''El Tangram Egípci - Figura 9'''

    name = "figures/figure012i"

    X = 1 # Scale #
    A = (     0,     0)
    B = (1*X*R5,2*X*R5)
    C = (2*X*R5,2*X*R5)
    D = (3*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012j():
    '''El Tangram Egípci - Figura 10'''

    name = "figures/figure012j"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (7*X,4*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012k():
    '''El Tangram Egípci - Figura 11'''

    name = "figures/figure012k"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,1*X*R5)
    C = (-2*X*R5,2*X*R5)
    D = (-3*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012l():
    '''El Tangram Egípci - Figura 12'''

    name = "figures/figure012l"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012m():
    '''El Tangram Egípci - Figura 13'''

    name = "figures/figure012m"

    X = 1 # Scale #
    A = (      0,-1*X*R5)
    B = (-2*X*R5,      0)
    C = (      0, 1*X*R5)
    D = ( 2*X*R5,      0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012n():
    '''El Tangram Egípci - Figura 14'''

    name = "figures/figure012n"

    X = 1 # Scale #
    A = (   0,-3*X)
    B = (-4*X,   0)
    C = (   0, 2*X)
    D = ( 4*X,   0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012o():
    '''El Tangram Egípci - Figura 15'''

    name = "figures/figure012o"

    X = 1 # Scale #
    A = (      0,      0)
    C = (-1*X*R5, 2*X*R5)
    D = ( 1*X*R5, 2*X*R5)

    I = w_point(A,C, 1,4)
    J = w_point(A,D, 1,4)
    K = w_point(C,D, 1,1)
    B = s_point(K,I, 1)
    E = s_point(K,J, 1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012p():
    '''El Tangram Egípci - Figura 16'''

    name = "figures/figure012p"

    X = 1 # Scale #
    A = (      0,      0)
    B = (1*X*R10,1*X*R10)
    C = (      0,2*X*R10)
    D = (3*X*R10,1*X*R10)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012q():
    '''El Tangram Egípci - Figura 17'''

    name = "figures/figure012q"

    X = 1 # Scale #
    A = (     0,     0)
    B = (2*X*R5,1*X*R5)
    C = (     0,2*X*R5)
    D = (2*X*R5,2*X*R5)
    E = (4*X*R5,1*X*R5)
    F = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012r():
    '''El Tangram Egípci - Figura 18'''

    name = "figures/figure012r"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (1*X*R5,2*X*R5)
    D = (3*X*R5,1*X*R5)
    E = (1*X*R5,0*X*R5)

    #A = (     0,     0)
    #B = (     0,2*X*R5)
    #C = (2*X*R5,1*X*R5)
    #D = (2*X*R5,2*X*R5)
    #E = (3*X*R5,2*X*R5)
    #F = (3*X*R5,     0)
    #G = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              #path.lineto(*F),
                              #path.lineto(*G),
                              #path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012s():
    '''El Tangram Egípci - Figura 19'''

    name = "figures/figure012s"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,1*X*R5)
    D = (2*X*R5,2*X*R5)
    E = (4*X*R5,1*X*R5)
    F = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012t():
    '''El Tangram Egípci - Figura 20'''

    name = "figures/figure012t"

    X = 1 # Scale #
    A = (     0/2.0,1*X*R5/2.0)
    B = (     0/2.0,3*X*R5/2.0)
    C = (4*X*R5/2.0,3*X*R5/2.0)
    D = (4*X*R5/2.0,4*X*R5/2.0)
    E = (8*X*R5/2.0,2*X*R5/2.0)
    F = (4*X*R5/2.0,     0/2.0)
    G = (4*X*R5/2.0,1*X*R5/2.0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012u():
    '''El Tangram Egípci - Figura 21'''

    name = "figures/figure012u"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (2*X,6*X)
    D = (4*X,6*X)
    E = (4*X,4*X)
    F = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012v():
    '''El Tangram Egípci - Figura 22'''

    name = "figures/figure012v"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,5*X)
    C = (4*X,2*X)
    D = (7*X,2*X)
    E = (7*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012w():
    '''El Tangram Egípci - Figura 23'''

    name = "figures/figure012w"

    X = 1 # Scale #
    A = (         0,  0)
    B = (         0,2*X*R5)
    C = (1*X*R5    ,2*X*R5)
    D = (2*X*R5-1*X,2*X)
    E = (2*X*R5+2*X,2*X)
    F = (2*X*R5+2*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012x():
    '''El Tangram Egípci - Figura 24'''

    name = "figures/figure012x"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (3*X,4*X)
    D = (4*X,2*X)
    E = (6*X,2*X)
    F = (7*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012y():
    '''El Tangram Egípci - Figura 22'''

    name = "figures/figure012y"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (4*X,2*X)
    D = (6*X,2*X)
    E = (10*X,0*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012z():
    '''El Tangram Egípci - Figura 23'''

    name = "figures/figure012z"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (2*X,4*X)
    D = (2*X,3*X)
    E = (6*X,3*X)
    F = (6*X,0*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013a():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure013a"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (4*X,4*X)
    D = (4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013b():
    '''El Subtangram Egípci - Figura 2'''

    name = "figures/figure013b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (3*X,4*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013c():
    '''El Subtangram Egípci - Figura 3'''

    name = "figures/figure013c"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (8*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013d():
    '''El Subtangram Egípci - Figura 4'''

    name = "figures/figure013d"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (4*X,4*X)
    D = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013e():
    '''El Subtangram Egípci - Figura 5'''

    name = "figures/figure013e"

    X = 1 # Scale #
    A = (  0,  0)
    B = (3*X,4*X)
    C = (4*X,4*X)
    D = (7*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013f():
    '''El Subtangram Egípci - Figura 6'''

    name = "figures/figure013f"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (6*X,4*X)
    D = (4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013g():
    '''El Subtangram Egípci - Figura 7'''

    name = "figures/figure013g"

    X = 1 # Scale #
    A = (  0,  0)
    B = (3*X,4*X)
    C = (7*X,4*X)
    D = (4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013h():
    '''El Subtangram Egípci - Figura 8'''

    name = "figures/figure013h"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,2*X)
    C = (4*X,4*X)
    D = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013i():
    '''El Subtangram Egípci - Figura 9'''

    name = "figures/figure013i"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,1*X)
    C = (4*X,4*X)
    D = (7*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013j():
    '''El Subtangram Egípci - Figura 10'''

    name = "figures/figure013j"

    X = 1 # Scale #
    A = ( 0*X, 2*X)
    B = ( 1*X, 4*X)
    C = (-3*X, 4*X)
    D = (-4*X, 2*X)
    E = (-4*X, 0*X)
    F = ( 0*X, 0*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013k():
    '''El Subtangram Egípci - Figura 11'''

    name = "figures/figure013k"

    X = 1 # Scale #
    A = ( 0*X, 3*X)
    B = ( 2*X, 4*X)
    C = (-2*X, 4*X)
    D = (-4*X, 3*X)
    E = (-4*X, 0*X)
    F = ( 0*X, 0*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013l():
    '''El Subtangram Egípci - Figura 11'''

    name = "figures/figure013l"

    X = 1 # Scale #
    A = ( 5*X, 2*X)
    B = ( 5*X, 0*X)
    C = ( 0*X, 0*X)
    D = ( 0*X, 2*X)
    E = r_point((5*X, 5*X), A, atan2(3,4))

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013m():
    '''El Subtangram Egípci - Figura 11'''

    name = "figures/figure013m"

    X = 1 # Scale #
    A = (-1*R5*X, 0*R5*X)
    B = ( 1*R5*X, 0*R5*X)
    C = ( 0*R5*X, 2*R5*X)
    D = (-2*R5*X, 1*R5*X)
    E = w_point(D, (0,0), 2,3)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013n():
    '''El Subtangram Egípci - Figura 11'''

    name = "figures/figure013n"

    X = 1 # Scale #
    A = ( 0*X, 2*X)
    B = ( 4*X, 4*X)
    C = ( 8*X, 4*X)
    D = ( 4*X, 2*X)
    E = ( 4*X, 0*X)
    F = ( 0*X, 0*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013o():
    '''El Subtangram Egípci - Figura 11'''

    name = "figures/figure013o"

    X = 1 # Scale #
    A = ( 0*X, 1*X)
    B = ( 4*X, 4*X)
    C = ( 8*X, 4*X)
    D = ( 4*X, 1*X)
    E = ( 4*X, 0*X)
    F = ( 0*X, 0*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013p():
    '''El Subtangram Egípci - Figura 11'''

    name = "figures/figure013p"

    X = 1 # Scale #
    A = (-2*R5*X,  1*R5*X)
    B = ( 2*R5*X, -1*R5*X)
    C = (-2*R5*X, -1*R5*X)
    D = w_point((0,0), C, 2,3)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013q():
    '''El Subtangram Egípci - Figura 11'''

    name = "figures/figure013q"

    X = 1 # Scale #
    A = (0*R5*X,      0*X)
    B = (2*R5*X,      0*X)
    C = (2*R5*X,      2*X)
    D = (2*R5*X-X,    2*X)
    E = (1*R5*X,   2*R5*X)
    F = (0*R5*X,   2*R5*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013r():
    '''El Subtangram Egípci - Figura 11'''

    name = "figures/figure013r"

    X = 1 # Scale #
    A = ( 1*R5*X, -2*R5*X)
    B = (-1*R5*X, -2*R5*X)
    C = (-1*R5*X,  0*R5*X)
    D = (    1*X,  0*R5*X)
    E = w_point((0,0), A, 5-R5,R5)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013s():
    '''El Subtangram Egípci - Figura 12'''

    name = "figures/figure013s"

    X = 1 # Scale #
    A = (0*X, 4*X)
    B = (4*X, 4*X)
    C = (4*X, 0*X)
    D = (0*X, 0*X)
    E = (0*X, 2*X)
    F = (1*X, 0*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+VERYTHICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+VERYTHICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+VERYTHICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+VERYTHICK+FILLED(RED)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure014a():
    '''El Tangram Egípci - Triangle 1:2'''

    name = "figures/figure014a"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,2*X)
    C = (1*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure014b():
    '''El Tangram Egípci - Triangle 2:4'''

    name = "figures/figure014b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (2*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure014c():
    '''El Tangram Egípci - Triangle sqrt(5):2*sqrt(5)'''

    name = "figures/figure014c"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (1*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure014d():
    '''El Tangram Egípci - Triangle 3:6'''

    name = "figures/figure014d"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,6*X)
    C = (3*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure014e():
    '''El Tangram Egípci - Triangle 4:8'''

    name = "figures/figure014e"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,8*X)
    C = (4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure014f():
    '''El Tangram Egípci - Triangle 2*sqrt(5):4*sqrt(5)'''

    name = "figures/figure014f"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,4*X*R5)
    C = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure014g():
    '''El Tangram Egípci - Triangle 5:10:3*sqrt(5)'''

    name = "figures/figure014g"

    X = 1 # Scale #
    A = ( 0*X, 0*X)
    B = ( 4*X, 3*X)
    C = (10*X, 0*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure014h():
    '''El Tangram Egípci - Triangle 5:4*sqrt(5):5'''

    name = "figures/figure014h"

    X = 1 # Scale #
    A = (     0,     0)
    B = (2*X*R5,1*X*R5)
    C = (4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure014i():
    '''El Tangram Egípci - Triangle 5:2*sqrt(5):5'''

    name = "figures/figure014i"

    X = 1 # Scale #
    A = (     0,     0)
    B = (1*X*R5,2*X*R5)
    C = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure014j():
    '''El Tangram Egípci - Triangle 3:4:5'''

    name = "figures/figure014j"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (3*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure015a():
    '''El Tangram Egípci - Suma de figures semblants 1'''

    name = "figures/figure015a"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure015b():
    '''El Tangram Egípci - Suma de figures semblants 2'''

    name = "figures/figure015b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (8*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure015c():
    '''El Tangram Egípci - Suma de figures semblants 3'''

    name = "figures/figure015c"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,2*X)
    C = (4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure015d():
    '''El Tangram Egípci - Suma de figures semblants 4'''

    name = "figures/figure015d"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,1*X*R5)
    C = (2*X*R5,2*X*R5)
    D = (3*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure015e():
    '''El Tangram Egípci - Suma de figures semblants 5'''

    name = "figures/figure015e"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,2*X)
    C = (4*X,4*X)
    D = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure015f():
    '''El Tangram Egípci - Suma de figures semblants 6'''

    name = "figures/figure015f"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,1*X)
    C = (2*X,2*X)
    D = (3*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016a():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016a"

    X = 1.0 # Scale #
    A = (     0,      0)
    B = (1*X*R5, 2*X*R5)
    C = (2*X*R5,      0)

    D = w_point(A,B, 5.0-X*R5,X*R5)
    E = (       - 3*X, 4*X)

    F = w_point(C,B, 5.0-X*R5,X*R5)
    G = (2*X*R5 + 3*X, 4*X)
    H = w_point(F,G, 1,1)
    I = w_point(C,G, 2,3)
    J = w_point(H,G, 1,1)
    K = s_point(I,J, 1)


    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*D),
                              path.lineto(*B),
                              path.lineto(*F),
                              path.lineto(*H),
                              path.lineto(*K),
                              path.lineto(*I),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016b():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016b"

    X = 1.0 # Scale #
    A = (  0,   0)
    B = (  0, 2*X)
    C = (2*X, 2*X)
    D = (2*X + 9*X/5.0, 2*X + 12*X/5.0)
    E = (7*X, 2*X)
    F = (7*X, 1*X)
    G = (5*X,   0)

    H = (6.5*X,   0)
    I = (H[0] + X*R5/5.0, 2*X/R5)
    J = (H[0] + X*R5,   0)



    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016c():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016c"

    X = 1.0 # Scale #
    A = (  0, 1*X)
    B = (  0, 2*X)
    C = (7*X, 2*X)
    D = (3*X, 0)
    E = (2*X, 0)


    F = (  0, 2.25*X)
    G = (3*X, 2.25*X)
    H = (3*X, 6.25*X)
    I = (3.25*X, 2.25*X)
    J = (3.25*X + R5*X, 2.25*X)
    K = (3.25*X, 2.25*X + 2*R5*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*I),
                              path.lineto(*J),
                              path.lineto(*K),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016d():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016d"

    X = 1.0 # Scale #
    A = (     0,          0)
    B = (1*X*R5,     2*X*R5)
    C = (2*X*R5,          0)
    D = (1*X*R5-5*X, 2*X*R5)
    E = (1*X*R5+5*X, 2*X*R5)
    F = w_point(A,B, X*R5, 5-X*R5)
    G = w_point(C,B, X*R5, 5-X*R5)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*G),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016e():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016e"

    X = 1.0 # Scale #
    A = (     0,      0)
    B = (     0, 1*X*R5)
    C = (1*X*R5, 3*X*R5)
    D = (2*X*R5, 1*X*R5)
    E = (2*X*R5,      0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016f():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016f"

    X = 1.0 # Scale #
    A = (      0,      0)
    C = (-1*X*R5, 2*X*R5)
    D = ( 1*X*R5, 2*X*R5)

    I = w_point(A,C, 1,4)
    J = w_point(A,D, 1,4)
    K = w_point(C,D, 1,1)
    B = s_point(K,I, 1)
    E = s_point(K,J, 1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016g():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016g"

    X = 1.0 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (2*X,6*X)
    D = (4*X,6*X)
    E = (4*X,4*X)
    F = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016h():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016h"

    X = 1.0 # Scale #


    A  = (         0,       0)
    B  = (1*X*R5,       2*X*R5)
    A1 = (2*X*R5-4*X,       0)
    A2 = (2*X*R5-4*X,     2*X)
    A3 = w_point(A,B, 3,2)
    C  = (2*X*R5-3*X,   2*X*R5)
    D  = (2*X*R5-3*X,   2*X*R5+1*X)
    E  = (2*X*R5-1*X,   2*X*R5+2*X)
    F  = (2*X*R5-1.25*X,   2*X*R5+2.5*X)
    G  = (2*X*R5-0.25*X,   2*X*R5+2.5*X)
    H  = (2*X*R5-0.25*X,   2*X*R5+0.5*X)
    I  = (2*X*R5,       2*X*R5)
    J  = (2*X*R5,       0)

    drawing = []
    drawing.append((path.path(path.moveto(*A1),
                              path.lineto(*A2),
                              path.lineto(*A3),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016i():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016i"

    X = 1.0 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (-2*X*R5,1*X*R5)
    D = (-2*X*R5,2*X*R5)
    E = (-4*X*R5,1*X*R5)
    F = (-2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016j():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016j"

    X = 1.0 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,1*X*R5)

    D = (    0-X*R3,      0)
    E = (    0-X*R3, 2*X*R5)
    F = (-X*R5-X*R3, 2*X*R5)
    G = (-X*R5-X*R3,      0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016k():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016k"

    X = 1.0 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,1*X*R5)
    D = (2*X*R5,2*X*R5)
    E = (4*X*R5,1*X*R5)
    F = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016l():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016l"

    X = 1.0 # Scale #
    A = (      0,     0)
    B = (      0,2*X*R5)
    C = (-4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016m():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016m"

    X = 1.0 # Scale #
    A = (      0,      0)
    B = (      0, 2*X*R5)
    C = ( 2*X*R5, 2*X*R5)
    D = ( 2*X*R5,      0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016n():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016n"

    X = 1.0 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,1*X*R5)
    D = (2*X*R5,2*X*R5)
    E = (3*X*R5,2*X*R5)
    F = (3*X*R5,     0)
    G = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016o():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016o"

    X = 1.0 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (-2*X*R5,1*X*R5)
    D = (-2*X*R5,2*X*R5)
    E = (-3*X*R5,2*X*R5)
    F = (-3*X*R5,     0)
    G = (-2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016p():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016p"

    X = 1.0 # Scale #
    A = (     0,  0)
    B = (     0,5*X)
    D = (1*X*R5,2*X*R5)
    F = (2*X*R5,5*X)
    G = (2*X*R5,  0)
    C = w_point(A,D, 5-2*X*R5, 2*X*R5)
    E = w_point(G,D, 5-2*X*R5, 2*X*R5)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016q():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016q"

    X = 1.0 # Scale #
    a1 = -pi+2*atan2(2,1)+atan2(3,4)
    A = (0,1*X)
    B = (0,5*X)
    C = r_point((0,7*X), B ,a1)
    D = r_point((4*X,7*X), B ,a1)
    E = w_point(D,B, 1,1)
    F = (3*X,2*X)
    H = (2*X+R5*X,0)
    I = (2*X,0)
    G = w_point(F,I, X, R5-X)

    A = r_point(A, (0.0,0.0) , a1/3.0)
    B = r_point(B, (0.0,0.0) , a1/3.0)
    C = r_point(C, (0.0,0.0) , a1/3.0)
    D = r_point(D, (0.0,0.0) , a1/3.0)
    E = r_point(E, (0.0,0.0) , a1/3.0)
    F = r_point(F, (0.0,0.0) , a1/3.0)
    G = r_point(G, (0.0,0.0) , a1/3.0)
    H = r_point(H, (0.0,0.0) , a1/3.0)
    I = r_point(I, (0.0,0.0) , a1/3.0)
    J = I

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016r():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016r"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,5*X)
    C = (4*X,3*X)
    D = s_point(A, C, 2*R5/5.0)
    E = s_point(B, C, 5/(2*R5))

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s+[trafo.rotate(-(90-3*BETA)/2.0)])

    mycanvas.writePDFfile(name)


def figure016s():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016s"

    X = 1.0 # Scale #
    A = (0,0)
    B = (X*R5,0)
    C = (X*R5+X*2,1*X)
    D = (X*R5+X*2,2*X)
    E = r_point((X*R5+X*2,2*X+2*R5*X),  D, pi/2.0-atan2(1,2)-atan2(4,3))
    F = r_point((X*R5+X*2-2*X/R5,2*X+2*R5*X+4*X/R5),  D, pi/2.0-atan2(1,2)-atan2(4,3))
    G = r_point((-X*R5+X*2,2*X+2*R5*X), D, pi/2.0-atan2(1,2)-atan2(4,3))
    H = (X*R5-1*X,6*X)
    I = (X*R5-1*X,2*X)
    J = w_point(B,I, R5-X, X)

    A = (-A[0], A[1])
    B = (-B[0], B[1])
    C = (-C[0], C[1])
    D = (-D[0], D[1])
    E = (-E[0], E[1])
    F = (-F[0], F[1])
    G = (-G[0], G[1])
    H = (-H[0], H[1])
    I = (-I[0], I[1])
    J = (-J[0], J[1])

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016t():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016t"

    X = 1.0 # Scale #
    a1 = -pi+2*atan2(2,1)+atan2(3,4)
    A = (0,1*X)
    B = (0,5*X)
    C = r_point((0,7*X), B ,a1)
    D = r_point((4*X,7*X), B ,a1)
    E = w_point(D,B, 1,1)
    F = (3*X,2*X)
    H = (2*X+R5*X,0)
    I = (2*X,0)
    G = w_point(F,I, X, R5-X)

    A = r_point(A, (0.0,0.0) , pi-a1)
    B = r_point(B, (0.0,0.0) , pi-a1)
    C = r_point(C, (0.0,0.0) , pi-a1)
    D = r_point(D, (0.0,0.0) , pi-a1)
    E = r_point(E, (0.0,0.0) , pi-a1)
    F = r_point(F, (0.0,0.0) , pi-a1)
    G = r_point(G, (0.0,0.0) , pi-a1)
    H = r_point(H, (0.0,0.0) , pi-a1)
    I = r_point(I, (0.0,0.0) , pi-a1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016u():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016u"

    X = 1.0 # Scale #
    a1 = -pi+2*atan2(2,1)+atan2(3,4)
    A = (0,1*X)
    B = (0,5*X)
    C = r_point((0,7*X), B ,a1)
    D = r_point((4*X,7*X), B ,a1)
    E = w_point(D,B, 1,1)
    F = (3*X,2*X)
    H = (2*X+R5*X,0)
    I = (2*X,0)
    G = w_point(F,I, X, R5-X)

    A = r_point(A, (0.0,0.0) , pi-a1)
    B = r_point(B, (0.0,0.0) , pi-a1)
    C = r_point(C, (0.0,0.0) , pi-a1)
    D = r_point(D, (0.0,0.0) , pi-a1)
    E = r_point(E, (0.0,0.0) , pi-a1)
    F = r_point(F, (0.0,0.0) , pi-a1)
    G = r_point(G, (0.0,0.0) , pi-a1)
    H = r_point(H, (0.0,0.0) , pi-a1)
    I = r_point(I, (0.0,0.0) , pi-a1)

    H = w_point(H,G, 1,1)
    H = (H[0]+G[0]-I[0], H[1]+G[1]-I[1])
    G = (G[0]+G[0]-I[0], G[1]+G[1]-I[1])

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016v():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016v"

    X = 1.0 # Scale #
    A = (0,0)
    B = (-6*X,0)
    C = (-6*X,-2*X)
    D = (-8*X,-2*X)
    E = (-8*X,-6*X)

    A = r_point(A, (0.0,0.0) , -atan2(3,4))
    B = r_point(B, (0.0,0.0) , -atan2(3,4))
    C = r_point(C, (0.0,0.0) , -atan2(3,4))
    D = r_point(D, (0.0,0.0) , -atan2(3,4))
    E = r_point(E, (0.0,0.0) , -atan2(3,4))

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016w():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016w"

    X = 1.0 # Scale #
    Y = (2.0*R5+3.0) / (R5*X)
    Z = (4-R5/2.0)*X
    a = atan2(1,2)/2.0
    A = (0,0)
    B = (2*R5*X,-1*R5*X)
    C = (2*R5*X,-4*X)
    G = (2*R5*X+3*X,0)
    D = r_point((2*R5*X+3*X,   -Z), G, -atan2(3,4))
    E = r_point((2*R5*X+5*X,4*X-Z), G, -atan2(3,4))
    F = r_point((2*R5*X+3*X,4*X-Z), G, -atan2(3,4))
    H = (R5*X+4.5*X,0)
    I = (R5*X+3.5*X,2*X)
    J = (R5*X-0.5*X,0)

    A = r_point(A, (0.0,0.0) , a)
    B = r_point(B, (0.0,0.0) , a)
    C = r_point(C, (0.0,0.0) , a)
    D = r_point(D, (0.0,0.0) , a)
    E = r_point(E, (0.0,0.0) , a)
    F = r_point(F, (0.0,0.0) , a)
    G = r_point(G, (0.0,0.0) , a)
    H = r_point(H, (0.0,0.0) , a)
    I = r_point(I, (0.0,0.0) , a)
    J = r_point(J, (0.0,0.0) , a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016x():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016x"

    X = 1.0 # Scale #
    Y = (2.0*R5+3.0) / (R5*X)
    Z = (4-R5/2.0)*X
    a = atan2(1,2)
    K = (1*R5*X-1*X,-2*X)
    A = w_point(K, (R5*X,0), 1, R5-1)
    B = (2*R5*X,-1*R5*X)
    C = (2*R5*X,-4*X)
    G = (2*R5*X+3*X,0)
    D = r_point((2*R5*X+3*X,   -Y), G, -atan2(3,4))
    E = r_point((2*R5*X+5*X,4*X-Y), G, -atan2(3,4))
    F = r_point((2*R5*X+3*X,4*X-Y), G, -atan2(3,4))
    H = (1*R5*X+4*X,0)
    I = (1*R5*X    ,2*X)
    J = (1*R5*X-1*X,0)

    A = r_point(A, (0.0,0.0) , a)
    B = r_point(B, (0.0,0.0) , a)
    C = r_point(C, (0.0,0.0) , a)
    D = r_point(D, (0.0,0.0) , a)
    E = r_point(E, (0.0,0.0) , a)
    F = r_point(F, (0.0,0.0) , a)
    G = r_point(G, (0.0,0.0) , a)
    H = r_point(H, (0.0,0.0) , a)
    I = r_point(I, (0.0,0.0) , a)
    J = r_point(J, (0.0,0.0) , a)
    K = r_point(K, (0.0,0.0) , a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.lineto(*K),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016y():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016y"

    X = 1.0 # Scale #
    Y = (2.0*R5+3.0) / (R5*X)
    Z = (4-R5/2.0)*X
    a = atan2(1,2)*2.0/3.0
    K = (R5*X-3*X/R5,-6*X/R5)
    L = w_point((1*R5*X-1*X,-2*X), (R5*X,0), 1, R5-1)
    B = (2*R5*X,-1*R5*X)
    A = w_point(L, B, 2,1)
    C = (2*R5*X,-4*X)
    G = (2*R5*X+3*X,0)
    D = r_point((2*R5*X+3*X,   -Y), G, -atan2(3,4))
    E = r_point((2*R5*X+5*X,4*X-Y), G, -atan2(3,4))
    F = r_point((2*R5*X+3*X,4*X-Y), G, -atan2(3,4))
    H = (1*R5*X+5*X,0)
    I = (1*R5*X+1*X,2*X)
    J = (1*R5*X,0)

    A = r_point(A, (0.0,0.0) , a)
    B = r_point(B, (0.0,0.0) , a)
    C = r_point(C, (0.0,0.0) , a)
    D = r_point(D, (0.0,0.0) , a)
    E = r_point(E, (0.0,0.0) , a)
    F = r_point(F, (0.0,0.0) , a)
    G = r_point(G, (0.0,0.0) , a)
    H = r_point(H, (0.0,0.0) , a)
    I = r_point(I, (0.0,0.0) , a)
    J = r_point(J, (0.0,0.0) , a)
    K = r_point(K, (0.0,0.0) , a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.lineto(*K),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016z():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016z"

    X = 1.0 # Scale #
    a = -pi/2+atan2(4,3)+atan2(1,2)
    A = (0, 0)
    B = (5*X-R5*X, 0)
    C = (5*X-R5*X - X/R5, -2*X/R5)
    D = (5*X, -X*R5)
    H = (9*X, 2*X-X*R5)
    G = w_point(H, D, 2,5)
    E = r_point((G[0]-16*X/5.0, G[1]-12*X/5.0), G, a)
    F = r_point((G[0]+ 9*X/5.0, G[1]-12*X/5.0), G, a)
    I = (5*X, 2*X-X*R5)
    J = (5*X, 2*X)
    K = (4*X, 2*X)

    A = r_point(A, (0.0,0.0) , -a)
    B = r_point(B, (0.0,0.0) , -a)
    C = r_point(C, (0.0,0.0) , -a)
    D = r_point(D, (0.0,0.0) , -a)
    E = r_point(E, (0.0,0.0) , -a)
    F = r_point(F, (0.0,0.0) , -a)
    G = r_point(G, (0.0,0.0) , -a)
    H = r_point(H, (0.0,0.0) , -a)
    I = r_point(I, (0.0,0.0) , -a)
    J = r_point(J, (0.0,0.0) , -a)
    K = r_point(K, (0.0,0.0) , -a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.lineto(*K),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016aa():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016aa"

    X = 1.0 # Scale #
    a = pi/4
    b = atan2(1,2)*0.9
    A = (0, (R5-3)*X)
    B = (4*X, (R5-3)*X)
    C = (4*X, -R5*X)
    D = r_point((4*X, -(R5+2)*X), C, -atan2(1,3))
    E = r_point((5*X,  -R5   *X), C, -atan2(1,3))
    F = ((R5+4)*X, 0)
    G = (8*X, 0)
    H = (4*X, 3*X)
    I = (4*X, (R5-1)*X)
    A = r_point(A, (0.0,0.0), a)
    B = r_point(B, (0.0,0.0), a)
    C = r_point(C, (0.0,0.0), a)
    D = r_point(D, (0.0,0.0), a)
    E = r_point(E, (0.0,0.0), a)
    F = r_point(F, (0.0,0.0), a)
    G = r_point(G, (0.0,0.0), a)
    H = r_point(H, (0.0,0.0), a)
    I = r_point(I, (0.0,0.0), a)

    J = w_point(G,H,1,3)
    K = (J[0]+R5*X, J[1])
    L = (J[0]+R5*X, J[1]+2*R5*X)
    J = r_point(J, J, b)
    K = r_point(K, J, b)
    L = r_point(L, J, b)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*K),
                              path.lineto(*L),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016ab():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ab"

    X = 1.0 # Scale #
    a = atan2(9,8)
    b = a-atan2(3,4)
    A = (0, 0)
    B = (4*X, 0)
    C = (4*X, -2*R5*X)
    D = (4*X, -2*R5*X)
    E = (4*X, -2*R5*X)
    F = ((R5+4)*X, 0)
    G = (8*X, 0)
    H = (4*X, 3*X)
    I = (4*X, 2*X)
    A = r_point(A, (0.0,0.0), a)
    B = r_point(B, (0.0,0.0), a)
    C = r_point(C, (0.0,0.0), a)
    D = r_point(D, (0.0,0.0), a)
    E = r_point(E, (0.0,0.0), a)
    F = r_point(F, (0.0,0.0), a)
    G = r_point(G, (0.0,0.0), a)
    H = r_point(H, (0.0,0.0), a)
    I = r_point(I, (0.0,0.0), a)

    J = w_point(G,H,3,10)
    K = (J[0]+R5*X, J[1])
    L = (J[0]+R5*X, J[1]+2*R5*X)
    J = r_point(J, J, b)
    K = r_point(K, J, b)
    L = r_point(L, J, b)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*K),
                              path.lineto(*L),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016ac():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ac"

    X = 1.0 # Scale #
    A = (0, 0)
    B = (2*R5*X,   0)
    C = r_point((2*R5*X, 5*X), B, pi/2.0 - atan2(4,3)  - atan2(1,2))
    D = (0, R5*X)
    E = ((1-R5)*X, R5*X)
    F = (-R5*X, (R5+2)*X)
    G = (-R5*X, R5*X)
    H = r_point((-3*X,0), A, -pi/2 + atan2(1,3) + atan2(1,1))

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016ad():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ad"

    X = 1.0 # Scale #
    A = (     0,      0)
    B = (     0, 1*X*R5)
    C = (1*X*R5, 3*X*R5)
    D = (2*X*R5, 1*X*R5)
    E = (2*X*R5,      0)

    Y = (5-2*R5)*X/2.0

    F = (-Y,     X*R5)
    G = (-Y+5*X, X*R5)
    H = r_point((-Y+5*X, 5*X + R5*X), G, pi/2.0 - atan2(4,3))
    H = r_point((-Y, 5*X + R5*X), F, -pi/2.0 + atan2(4,3))

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016ae():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ae"

    X = 1.0 # Scale #
    A = ( 0*X, 0*X)
    B = ( 6*X, 0*X) #( 3*X, 0*X)
    C = ( 7*X, 2*X) #( 7*X, 2*X)
    D = (-1*X, 2*X) #(-4*X, 2*X)

    a = 0 #pi*1.0/12.0
    F = (1.5*X, 2.25*X)
    G = r_point((F[0], F[1]+4*X), F, a)
    H = r_point((F[0]+3*X, F[1]), F, a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016af():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016af"

    X = 1.0 # Scale #
    A = ( 0*X, 0*X)
    B = ( 3*X, 0*X)
    C = ( 7*X, 2*X)
    D = (-4*X, 2*X)

    a = 0 #pi*1.0/12.0
    F = (0.5*X, 2.25*X)
    G = r_point((F[0], F[1]+4*X), F, a)
    H = r_point((F[0]+3*X, F[1]), F, a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016ag():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ag"

    X = 1.0 # Scale #
    a =  pi/2.0 - atan2(1,2) - atan2(3,4)
    b = -pi/2.0 + atan2(1,3) + atan2(1,1)
    c =  pi*1.25

    A = (0*R5*X,     0*X)
    B = (2*R5*X,     0*X)
    C = r_point((2*R5*X,     4*X), B, a)
    D = r_point((2*R5*X-2*X, 8*X), B, a)
    E = r_point((2*R5*X-2*X, 4*X), B, a)
    F = (0*R5*X,  1*R5*X)
    G = ( -R5*X,  1*R5*X)
    H = r_point((-5*X, 1*X), A, b)
    I = r_point((-3*X, 0*X), A, b)

    A = r_point(A, (0,0), c)
    B = r_point(B, (0,0), c)
    C = r_point(C, (0,0), c)
    D = r_point(D, (0,0), c)
    E = r_point(E, (0,0), c)
    F = r_point(F, (0,0), c)
    G = r_point(G, (0,0), c)
    H = r_point(H, (0,0), c)
    I = r_point(I, (0,0), c)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016ah():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ah"

    X = 1.0 # Scale #
    a = -atan2(1,3)
    b = 0 # -pi/2.0

    A = (1*R5*X,     2*R5*X)
    B = (2*R5*X,     0*R5*X)
    C = (0*R5*X,     0*R5*X)
    D = (0*R5*X,     2*R5*X)
    E = r_point((0*R5*X,     2*R5*X+3*X), D, a)
    F = r_point((0*R5*X+1*X, 2*R5*X+5*X), D, a)
    G = r_point((0*R5*X+1*X, 2*R5*X+3*X), D, a)
    H = r_point((0*R5*X+2*X, 2*R5*X+1*X), D, a)

    A = r_point(A, C, b)
    B = r_point(B, C, b)
    C = r_point(C, C, b)
    D = r_point(D, C, b)
    E = r_point(E, C, b)
    F = r_point(F, C, b)
    G = r_point(G, C, b)
    H = r_point(H, C, b)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016ai():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ai"

    X = 1.0 # Scale #
    a = -atan2(1,3)
    b = -2*atan2(1,2)

    A = (1*R5*X,     2*R5*X)
    BB = (2*R5*X,     0*R5*X)
    B = w_point(A, BB, 2, 3)
    C = (0*R5*X,     0*R5*X)
    D = (0*R5*X,     2*R5*X)
    E = r_point((0*R5*X,     2*R5*X+3*X), D, a)
    F = r_point((0*R5*X+1*X, 2*R5*X+5*X), D, a)
    G = r_point((0*R5*X+1*X, 2*R5*X+3*X), D, a)
    H = r_point((0*R5*X+2*X, 2*R5*X+1*X), D, a)
    I = (0,0)
    J = r_point((4*X,0), I, atan2(1,2))
    K = r_point((0, -2*X), I, atan2(1,2))

    A = r_point(A, I, b)
    B = r_point(B, I, b)
    C = r_point(C, I, b)
    D = r_point(D, I, b)
    E = r_point(E, I, b)
    F = r_point(F, I, b)
    G = r_point(G, I, b)
    H = r_point(H, I, b)
    J = r_point(J, I, b)
    K = r_point(K, I, b)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*I),
                              path.lineto(*J),
                              path.lineto(*K),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016aj():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016aj"

    X = 1.0 # Scale #
    a = -2*atan2(1,2)
    b = -pi/2.0 + atan2(1,2) + atan2(3,4)

    A = (     0,      0)
    B = (2*R5*X,      0)
    C = (2*R5*X, 1*X*R5)

    D = (0*X, 0*X)
    E = (0*X, 4*X)
    F = (1*X, 6*X)
    G = r_point((1*X,  7*X), F, a)
    H = r_point((3*X, 11*X), F, a)
    I = (3*X, 5*X)
    J = (3*X, 4*X)

    E = r_point(E, A, b)
    F = r_point(F, A, b)
    G = r_point(G, A, b)
    H = r_point(H, A, b)
    I = r_point(I, A, b)
    J = r_point(J, A, b)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016ak():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ak"

    X = 1.0 # Scale #
    a = atan2(1,2)

    A = (-1*X*R5,          0)
    B = (      0,     2*X*R5)
    C = ( 1*X*R5,          0)

    D = w_point(A,B, 3,2)
    E = r_point((D[0]-2*R5*X, D[1]), D, -a)
    F = r_point((D[0], D[1]+1*R5*X), D, -a)

    G = w_point(C,B, 3,2)
    H = r_point((G[0]+2*R5*X, G[1]), G, a)
    I = r_point((G[0], G[1]+1*R5*X), G, a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016al():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016al"

    X = 1.0 # Scale #
    a = pi/2.0 - atan2(1,2)

    A = (-1*X*R5,          0)
    B = (      0,     2*X*R5)
    C = ( 1*X*R5,          0)

    D = r_point((-1*X*R5,     2*X*R5), B, a)
    E = r_point((      0,     4*X*R5), B, a)
    F = r_point((      0,     2*X*R5), B, a)

    G = r_point(( 1*X*R5,     2*X*R5), B, -a)
    H = r_point((      0,     4*X*R5), B, -a)
    I = r_point((      0,     2*X*R5), B, -a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016am():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016am"

    X = 1.0 # Scale #
    Y = (2.0*R5+3.0) / (R5*X)
    Z = (4-R5/2.0)*X
    a = atan2(1,2)
    K = (1*R5*X-1*X,-2*X)
    A = w_point(K, (R5*X,0), 1, R5-1)
    B = (2*R5*X,-1*R5*X)
    C = (2*R5*X,-4*X)
    G = (2*R5*X+3*X,0)
    D = r_point((2*R5*X+3*X,   -Y), G, -atan2(3,4))
    E = r_point((2*R5*X+5*X,4*X-Y), G, -atan2(3,4))
    F = r_point((2*R5*X+3*X,4*X-Y), G, -atan2(3,4))
    H = (1*R5*X+4*X,0)
    I = (1*R5*X    ,2*X)
    J = (1*R5*X-1*X,0)

    L = (2*I[0]-J[0], 2*I[1]-J[1])
    M = (J[0], J[1])
    N = (M[0], L[1])

    A = r_point(A, (0.0,0.0) , a)
    B = r_point(B, (0.0,0.0) , a)
    C = r_point(C, (0.0,0.0) , a)
    D = r_point(D, (0.0,0.0) , a)
    E = r_point(E, (0.0,0.0) , a)
    F = r_point(F, (0.0,0.0) , a)
    G = r_point(G, (0.0,0.0) , a)
    H = r_point(H, (0.0,0.0) , a)
    I = r_point(I, (0.0,0.0) , a)
    J = r_point(J, (0.0,0.0) , a)
    K = r_point(K, (0.0,0.0) , a)
    L = r_point(L, (0.0,0.0) , a)
    M = r_point(M, (0.0,0.0) , a)
    N = r_point(N, (0.0,0.0) , a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.lineto(*K),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*L),
                              path.lineto(*M),
                              path.lineto(*N),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016an():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016an"

    X = 1.0 # Scale #

    a = atan2(3,4)
    A = (0*X, 0*X)
    B = (4*X, 0*X)
    C = (4*X, 3*X)

    D = (C[0], C[1])
    E = r_point((C[0]-0*X, C[1]+1*X), D, a)
    F = r_point((C[0]-2*X, C[1]+5*X), D, a)
    G = r_point((C[0]-2*X, C[1]+3*X), D, a)
    H = r_point((C[0]-4*X, C[1]+2*X), D, a)
    I = r_point((C[0]-5*X, C[1]+4*X), D, a)
    J = r_point((C[0]-5*X, C[1]+0*X), D, a)
    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016ao():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ao"

    X = 1.0 # Scale #

    a = atan2(3,4)
    A = r_point((0*X, 0*X), (4*X, 3*X), -a)
    B = r_point((4*X, 0*X), (4*X, 3*X), -a)
    C = r_point((4*X, 3*X), (4*X, 3*X), -a)

    D = (C[0], C[1])
    E = (C[0]-0*X, C[1]+1*X)
    F = (C[0]-2*X, C[1]+5*X)
    G = (C[0]-2*X, C[1]+3*X)
    H = (C[0]-4*X, C[1]+2*X)
    I = (C[0]-5*X, C[1]+4*X)
    J = (C[0]-5*X, C[1]+0*X)
    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016ap():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ap"

    X = 1.0 # Scale #

    a = -atan2(1,2)
    b =  pi/2.0 - atan2(1,2)
    c = -atan2(3,4)

    A = (0,0)
    B = (0, 2*R5*X)
    C = (1*R5*X, 0)
    D = r_point((1*R5*X,     -3*X), C, a)
    E = r_point((1*R5*X-2*X, -3*X), C, a)
    F = r_point((-2*X, 0), A, b)
    G = r_point((0,  4*X), A, b)

    H = w_point(C,D, 1,1)
    I = (H[0]+0*X, H[1]-3*X)
    J = (H[0]+4*X, H[1]-0*X)


    B = r_point(B, A, c)
    C = r_point(C, A, c)
    D = r_point(D, A, c)
    E = r_point(E, A, c)
    F = r_point(F, A, c)
    G = r_point(G, A, c)
    H = r_point(H, A, c)
    I = r_point(I, A, c)
    J = r_point(J, A, c)

    drawing = []
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016aq():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016aq"

    X = 1.0 # Scale #
    a = -2*atan2(1,2)
    b =    atan2(3,4)

    A = (1*X,     2*X)
    B = (3*X,     6*X)
    C = (3*X,     0*X)
    D = (0*X,     0*X)

    E = r_point((-1*X, 0*X), D, a)
    F = r_point((-5*X, 2*X), D, a)

    G = w_point(C,D, 1,1)
    H = r_point((G[0]-4*X, G[1]), G, b)
    I = r_point((G[0], G[1]-3*X), G, b)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016ar():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ar"

    X = 1.0 # Scale #
    a = 2*atan2(1,2)

    A = (-1*X*R5,          0)
    B = (      0,     2*X*R5)
    C = ( 1*X*R5,          0)

    D = w_point(A,B, 1,0)
    E = r_point((D[0]-3*X, D[1]),          D, -a)
    F = r_point((D[0]-3*X, D[1]+(1+R5)*X), D, -a)
    H = r_point((D[0]-1*X, D[1]+     2*X), D, -a)
    G = w_point(w_point(E, F, R5, 1), H, R5-1, 1)

    I = w_point(C,B, 1,0)
    J = r_point((I[0]+5*X, I[1]), I, a)
    K = r_point((I[0]+1*X, I[1]+2*X), I, a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    drawing.append((path.path(path.moveto(*I),
                              path.lineto(*J),
                              path.lineto(*K),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016as():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016as"

    X = 1.0 # Scale #
    a = -pi/2 + atan2(4,3) + atan2(1,2)
    b = -atan2(1,2)

    A = (5*X,     0*X)
    B = (0*X,     0*X)
    C = (0*R5*X,     2*R5*X)
    D = r_point((C[0],     C[1]+3*X), C, b)
    E = r_point((C[0]+1*X, C[1]+5*X), C, b)
    F = r_point((C[0]+1*X, C[1]+3*X), C, b)
    G = (1*R5*X,     2*R5*X)

    C = r_point(C, B, a)
    D = r_point(D, B, a)
    E = r_point(E, B, a)
    F = r_point(F, B, a)
    G = r_point(G, B, a)


    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016at():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016at"

    X = 1.0 # Scale #
    a = atan2(2,1)

    A = (5*X+R5*X, 5*X-R5*X)
    B = (5*X,      5*X-R5*X)
    C = (5*X,      0*X)
    D = (0*X,      0*X)
    E = (1*X,      2*X)
    F = (5*X,      5*X)
    G = r_point((6*X+R5*X, 5*X-R5*X), A, a)
    H = r_point((5*X+R5*X, 3*X-R5*X), A, a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016au():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016au"

    X = 1.0 # Scale #
    a = atan2(2,1)

    A = (0*R5*X, 0*R5*X)
    B = (2*R5*X, 0*R5*X)
    C = (2*R5*X, 3*R5*X)
    D = r_point((2*R5*X+2*X, 3*R5*X), C, a)
    E = r_point((2*R5*X, 3*R5*X+1*X), C, a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016av():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016av"

    X = 1.0 # Scale #

    A = (5*X, 2*X)
    B = (5*X, 0*X)
    C = (0*X, 0*X)
    D = (0*X, 2*X)
    E = r_point((5*X, 2*X), D, atan2(4,3))

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016aw():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016aw"

    X = 1.0 # Scale #

    A = (0*X, 0*X)
    B = (4*X, 0*X)
    C = (6*X, 4*X)
    D = (6*X, 5*X)
    E = (4*X, 5*X)
    F = (0*X, 2*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016ax():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ax"

    X = 1.0 # Scale #

    A = (0*X, 4*X)
    E = (0*X, 0*X)
    B = w_point(A, E, R5, 4-R5)
    C = (-R5*X, B[1])
    D = r_point((0*X, 3*X), E, atan2(1,1) + atan2(1,3))
    F = (3*X, 0*X)
    G = (5*X, 0*X)
    H = (5*X, 4*X)
    I = r_point((5*X, 6*X), H, pi/2.0 - 2*atan2(1,2))

    J = w_point(G, H, 1, 7)
    K = (J[0], J[1]-R5*X)
    L = r_point((K[0], K[1]+2*X), K, -atan2(1,2))

    a = atan2(3,4)
    G = r_point(G, F, a)
    H = r_point(H, F, a)
    I = r_point(I, F, a)
    J = r_point(J, F, a)
    K = r_point(K, F, a)
    L = r_point(L, F, a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*K),
                              path.lineto(*L),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016ay():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ay"

    X = 1.0 # Scale #

    A = (0*X, 4*X)
    E = (0*X, 0*X)
    B = w_point(A, E, R5, 4-R5)
    C = (-R5*X, B[1])
    D = r_point((0*X, 3*X), E, atan2(1,1) + atan2(1,3))
    F = (3*X, 0*X)
    G = (5*X, 0*X)
    H = (5*X, 4*X)
    I = r_point((5*X, 6*X), H, pi/2.0 - 2*atan2(1,2))

    J = w_point(G, H, 1, 7)
    K = (J[0], J[1]-R5*X)
    L = r_point((K[0], K[1]+2*X), K, -atan2(1,2))

    a = atan2(3,4)
    G = r_point(G, F, a)
    H = r_point(H, F, a)
    I = r_point(I, F, a)
    J = r_point(J, F, a)
    K = r_point(K, F, a)
    L = r_point(L, F, a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016az():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016az"

    X = 1.0 # Scale #

    A = (0*R5*X, 2*R5*X)
    B = (0*R5*X, 0*R5*X)
    C = (1*R5*X, 0*R5*X)
    D = (2*R5*X, 2*R5*X)
    E = r_point((2*R5*X, 2*R5*X+2*X), D, atan2(1,2))
    F = w_point(A, E, 4-R5, R5)
    G = r_point((0*R5*X+2*X, 2*R5*X), A, 2*atan2(1,2))

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016ba():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ba"

    X = 1.0 # Scale #

    A = (0*X, 4*X)
    B = (0*X, 2*X)
    C = (1*X, 0*X)
    D = (4*X, 0*X)
    E = (4*X, 1*X)
    F = (6*X, 2*X)
    G = (6*X, 4*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bb():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bb"

    X = 1.0 # Scale #

    A = (-1*X, 4*X)
    B = ( 0*X, 2*X)
    C = ( 1*X, 0*X)
    D = ( 4*X, 0*X)
    E = ( 4*X, 1*X)
    F = ( 6*X, 2*X)
    G = ( 5*X, 4*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bc():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bc"

    X = 1.0 # Scale #

    A = ( 0*X, 0*X)
    B = ( 1*X, 2*X)
    C = (-2*X, 6*X)
    D = (-2*X, 1*X)
    E = r_point((R5*X, -2*R5*X), A, atan2(2,1))
    F = r_point((-1*R5*X, -2*R5*X), A, -atan2(1,2))

    a = -atan2(3,4)/2.0
    B = r_point(B, A, a)
    C = r_point(C, A, a)
    D = r_point(D, A, a)
    E = r_point(E, A, a)
    F = r_point(F, A, a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bd():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bd"

    X = 1.0 # Scale #

    A = ( 0*X, 0*X)
    B = (11*X, 0*X)
    C = ( 7*X, 2*X)
    D = ( 7*X, 6*X)
    E = ( 4*X, 2*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016be():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016be"

    X = 1.0 # Scale #

    A = (     0*X,  4*X)
    B = (     5*X,  4*X)
    C = (     5*X,  0*X)
    D = ((2-R5)*X,  0*X)
    E = ((2-R5)*X, R5*X)
    F = w_point(A, (2*X, 0*X), 3, 2*R5-3)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bf():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bf"

    X = 1.0 # Scale #

    a = atan2(1,2)
    b = atan2(3,4)
    c = 3*atan2(1,2) - pi/2.0

    A = (0*R5*X, 0*R5*X)
    B = (0*R5*X, 1*R5*X)
    C = (2*R5*X, 0*R5*X)

    D = (0*R5*X,     1*R5*X)
    E = (0*R5*X+4*X, 1*R5*X)
    F = (0*R5*X,     1*R5*X+3*X)

    G = (0*R5*X-1*X, 1*R5*X+3*X)
    H = (0*R5*X+3*X, 1*R5*X+3*X)
    I = (0*R5*X+3*X, 1*R5*X+5*X)

    J = r_point((0*R5*X-2*X, 1*R5*X+3*X), G, c)
    K = r_point((0*R5*X-2*X, 1*R5*X+6*X), G, c)
    L = r_point((0*R5*X+0*X, 1*R5*X+5*X), G, c)
    M = w_point(G,I, 2*R5-2, 2)

    G = r_point(G, F, -b)
    H = r_point(H, F, -b)
    I = r_point(I, F, -b)
    J = r_point(J, F, -b)
    K = r_point(K, F, -b)
    L = r_point(L, F, -b)
    M = r_point(M, F, -b)

    D = r_point(D, D, -a)
    E = r_point(E, D, -a)
    F = r_point(F, D, -a)
    G = r_point(G, D, -a)
    H = r_point(H, D, -a)
    I = r_point(I, D, -a)
    J = r_point(J, D, -a)
    K = r_point(K, D, -a)
    L = r_point(L, D, -a)
    M = r_point(M, D, -a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*J),
                              path.lineto(*K),
                              path.lineto(*L),
                              path.lineto(*M),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bg():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bg"

    X = 1.0 # Scale #

    A = ( -2*X,  4*X)
    B = (  2*X,  4*X)
    C = (  4*X,  0*X)
    D = (-R5*X,  0*X)
    E = (-R5*X, R5*X)
    F = w_point((0,0), A, 2*R5-3, 3)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bh():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bh"

    X = 1.0 # Scale #

    A = ( -2*X,  4*X)
    B = (  0*X,  4*X)
    C = (  4*X,  2*X)
    D = (  4*X,  0*X)
    E = (-R5*X,  0*X)
    F = (-R5*X, R5*X)
    G = w_point((0,0), A, 2*R5-3, 3)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bi():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bi"

    X = 1.0 # Scale #


    A = (-R5*X, -R5*X)
    B = (-R5*X,  R5*X)
    E = (R5*X,0*X)
    C = w_point(B, E, R5, 5-R5)
    D = r_point((E[0],E[1]+2*X), E, pi/2.0 - 2*atan2(1,2))
    F = (5*X,  0*X)
    G = (2*X, -4*X)
    H = w_point((0,0), G, 2*R5-1, 1)

    a = -atan2(G[1]-A[1], G[0]-A[0])*0.9
    A = r_point(A, A, a)
    B = r_point(B, A, a)
    C = r_point(C, A, a)
    D = r_point(D, A, a)
    E = r_point(E, A, a)
    F = r_point(F, A, a)
    G = r_point(G, A, a)
    H = r_point(H, A, a)


    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bj():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bj"

    X = 1.0 # Scale #


    A = (0*X, 0*X)
    B = (0*X, 4*X)
    C = (2*X, 3*X)
    D = (4*X, 3*X)
    E = (6*X, 4*X)
    F = (6*X, 0*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bk():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bk"

    X = 1.0 # Scale #

    A = (-1*R5*X, 2*R5*X)
    B = ( 1*R5*X, 2*R5*X)
    C = ( 1*R5*X, 0*R5*X)
    D = (   -3*X,    0*X)
    E = (   -3*X,    2*X)
    F = (   -1*X,    2*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bl():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bl"

    X = 1.0 # Scale #

    A = (   -4*X,  -2*X)
    B = (   -3*X,  -4*X)
    C = (    2*X,  -4*X)
    D = (    0*X,   0*X)
    E = (-2*R5*X,   0*X)
    F = (-2*R5*X, -R5*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bm():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bm"

    X = 1.0 # Scale #

    A = (3*(1+R5)*X, 0*X)
    B = (       0*X, 0*X)
    C = (       0*X, 4*X)
    D = (       4*X, 2*X)
    E = r_point((A[0], 6*X), A, pi/2.0 - atan2(1,2))

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bn():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bn"

    X = 1.0 # Scale #

    A = (0*X, 0*X)
    B = (0*X, 6*X)
    C = (8*X, 0*X)
    D = (3*X, 0*X)
    E = (2*X, 2*X)
    F = (1*X, 2*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bo():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bo"

    X = 1.0 # Scale #

    A = (0*X, 0*X)
    B = (4*X, 0*X)
    C = (4*X, 2*X)
    D = (9*X, 2*X)
    E = r_point((9*X, 8*X), D, atan2(4,3))

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bp():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bp"

    X = 1.0 # Scale #

    Y = 0.75*X

    A = ( 0*X, 0*X)
    B = ( 4*X, 0*X)
    C = ( 4*X, 0*X+Y)
    D = ( 6*X, 0*X+Y)
    E = ( 6*X, 0*X+Y+Y)
    F = (10*X, 0*X+Y+Y)
    G = ( 6*X, 2*X+Y+Y)
    H = ( 6*X, 2*X+Y)
    I = ( 4*X, 3*X+Y)
    J = ( 4*X, 3*X)
    K = ( 2*X, 4*X)

    a = atan2(1,2)/2.0 - pi/2.0

    A = r_point(A, A, a)
    B = r_point(B, A, a)
    C = r_point(C, A, a)
    D = r_point(D, A, a)
    E = r_point(E, A, a)
    F = r_point(F, A, a)
    G = r_point(G, A, a)
    H = r_point(H, A, a)
    I = r_point(I, A, a)
    J = r_point(J, A, a)
    K = r_point(K, A, a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.lineto(*K),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bq():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bq"

    X = 1.0 # Scale #

    A = ( 0*X, 0*X)
    B = ( 3*X, 4*X)
    C = ( 6*X, 4*X)
    D = ( 9*X, 0*X)
    E = ( 7*X, 0*X)
    F = ( 7*X, 1*X)
    G = ( 3*X, 1*X)
    H = ( 3*X, 0*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016br():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016br"

    X = 1.0 # Scale #

    A = ( 0*X, 0*X)
    B = ( 2*X, 4*X)
    C = ( (5+R5)*X, 4*X)
    D = r_point(((5+R5)*X, 1*X), C, -atan2(1,2))
    E = ( 5*X, (4-R5)*X)
    F = ( 5*X, 0*X)

    B = (-B[0], -B[1])
    C = (-C[0], -C[1])
    D = (-D[0], -D[1])
    E = (-E[0], -E[1])
    F = (-F[0], -F[1])

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bs():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bs"

    X = 1.0 # Scale #

    A = ( 2*X, 0*X)
    B = ( 0*X, 4*X)
    C = ( (5+R5)*X, 4*X)
    D = r_point(((5+R5)*X, 1*X), C, -atan2(1,2))
    E = ( 5*X, (4-R5)*X)
    F = ( 5*X, 0*X)

    A = (-A[0], -A[1])
    B = (-B[0], -B[1])
    C = (-C[0], -C[1])
    D = (-D[0], -D[1])
    E = (-E[0], -E[1])
    F = (-F[0], -F[1])

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bt():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bt"

    X = 1.0 # Scale #

    A = ( 0*X, 4*X)
    B = ( 4*X, 4*X)
    C = ( 4*X, 2*X)
    D = ( 6*X, 2*X)
    E = ( 6*X, 0*X)
    F = ((2-R5)*X, 0*X)
    G = ((2-R5)*X, R5*X)
    H = w_point(A, (2*X,0), 3, 2*R5-3)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bu():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bu"

    X = 1.0 # Scale #

    A = ( 1*X, 0*X)
    B = ( 1*X, 4*X)
    C = ( (5+R5)*X, 4*X)
    D = r_point(((5+R5)*X, 1*X), C, -atan2(1,2))
    E = ( 5*X, (4-R5)*X)
    F = ( 5*X, 0*X)

    A = (-A[0], -A[1])
    B = (-B[0], -B[1])
    C = (-C[0], -C[1])
    D = (-D[0], -D[1])
    E = (-E[0], -E[1])
    F = (-F[0], -F[1])

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bv():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bv"

    X = 1.0 # Scale #
    a = -atan2(3,4)

    A = ( 0*X, 0*X)
    B = ( 4*X, 3*X)
    C = ( 0*X, 5*X)
    D = r_point((-3*X, R5*X), A, a)
    F = r_point((-(3+R5)*X,  0*X), A, a)
    E = r_point(r_point((-(3+R5)*X, 3*X), (-(3+R5)*X, 0*X), -atan2(1,2)), A, a)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bw():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bw"

    X = 1.0 # Scale #

    X = 1.0 # Scale #
    a = -atan2(1,2)

    A = ( 0*R5*X, 0*R5*X)
    B = ( 2*R5*X, 1*R5*X)
    C = ( 0*R5*X, 2*R5*X)
    D = ( 0*X, 3*X)
    E = (-1*X, 3*X)
    G = r_point((-(3+R5)*X,  0*X), A, -atan2(1,2))
    F = (G[0]+2*R5*X, G[1]+1*R5*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bx():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bx"

    X = 1.0 # Scale #

    A = ((2*R5-3)*X, (1+R5)*X)
    B = ((2*R5-3)*X,    R5 *X)
    C = (0*R5*X, 1*R5*X)
    D = (0*R5*X, 0*R5*X)
    E = (2*R5*X, 0*R5*X)
    F = (2*R5*X, 1*R5*X)
    G = r_point((2*R5*X, (2*R5+3)*X), F, atan2(1,2))
    H = r_point((G[0], G[1]-5*X), G, -atan2(1,2))


    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016by():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016by"

    X = 1.0 # Scale #

    Y = (3-R5)*X/2.0

    A = (0*R5*X, 0*R5*X)
    B = (2*R5*X, 0*R5*X)
    C = (2*R5*X, 1*R5*X)
    D = (0*R5*X, 1*R5*X)

    E = ( 3*X-Y, 2*R5*X)
    F = ( 3*X-Y, (R5+4)*X)
    G = (    -Y, 1*R5*X)
    H = ( (3+R5)*X-Y, 1*R5*X)
    I = r_point((H[0], H[1]+3*X), H, atan2(1,2))

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016bz():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016bz"

    X = 1.0 # Scale #

    A = ( 5*X, 0*X)
    B = ( 0*X, 0*X)
    C = ( 3*X, 4*X)
    D = ( (3+R5)*X, 4*X)
    E = ( (6+R5)*X, 0*X)
    F = ( (3+R5)*X, 0*X)
    G = ( (3+R5)*X, (4-R5)*X)
    H = w_point(A, C, 3, 2*R5-3)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016ca():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ca"

    X = 1.0 # Scale #

    A = ( -R5*X,  0*X)
    B = (   8*X,  0*X)
    C = (   0*X,  4*X)
    D = (   0*X, R5*X)
    E = r_point((A[0], A[1]+3*X), A, -atan2(1,2))

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016cb():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016cb"

    X = 1.0 # Scale #

    A = (1*R5*X, 0*R5*X)
    B = (0*R5*X, 0*R5*X)
    C = (1*R5*X, 2*R5*X)
    D = (2*R5*X, 2*R5*X)
    E = r_point((2*R5*X, (R5-3)*X), D, atan2(1,2))
    F = (E[0]-3*X, E[1])
    G = (E[0]-3*X, E[1]+X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016cc():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016cc"

    X = 1.0 # Scale #

    A = ( R5*X, -R5*X)
    B = (  0*X, -R5*X)
    C = (  0*X,   0*X)
    D = (  4*X,   3*X)
    E = (  6*X,   3*X)
    F = (  6*X,   2*X)
    G = (  4*X,  -2*X)
    H = w_point(C, G, 2*R5-3, 3)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016cd():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016cd"

    X = 1.0 # Scale #

    Y = (R5+0.5)*X/(R5)

    A = (0*R5*X, 0*R5*X)
    B = (2*R5*X, 0*R5*X)
    C = (2*R5*X, 1*R5*X)
    D = (0*R5*X, 1*R5*X)

    E = (2*R5*X+X, 3*X-Y)
    F = (2*R5*X  , 3*X-Y)
    G = (2*R5*X  ,    -Y)
    H = r_point((G[0]+(3+R5)*X, G[1]),     G, atan2(1,2))
    I = r_point((H[0],          H[1]+5*X), H, atan2(2,1))

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016ce():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ce"

    X = 1.0 # Scale #

    A = (0*X, 0*X)
    B = (4*X, 0*X)
    C = (4*X, 2*X)
    D = (0*X, 4*X)

    E = (2*X-1*R5*X, 0*X)
    F = (   -1*R5*X, 0*X)
    G = (   -1*R5*X, 4*X)
    H = (    0*R5*X, 4*X)
    I = (    0*R5*X, 4*X-R5*X)
    J = w_point(E, G, 3, R5*2-3)
    
    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016cf():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016cf"

    X = 1.0 # Scale #

    A = (0*X, 0*X)
    B = (4*X, 0*X)
    C = (2*X, 4*X)
    D = (0*X, 4*X)

    E = (2*X-1*R5*X, 0*X)
    F = (   -1*R5*X, 0*X)
    G = (   -1*R5*X, 4*X)
    H = (    0*R5*X, 4*X)
    I = (    0*R5*X, 4*X-R5*X)
    J = w_point(E, G, 3, R5*2-3)
    
    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure016cg():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016cg"

    X = 1.0 # Scale #

    A = (4*X,      0*X)
    B = (0*X,      0*X)
    C = (0*X,      4*X)
    D = ((2+R5)*X, 4*X)
    E = ((4+R5)*X, 0*X)
    F = ((2+R5)*X, 0*X)
    G = ((2+R5)*X, (4-R5)*X)
    H = w_point(A, (2*X,4*X), 3, R5*2-3)
    
    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)

figure016cg()

def figure018a():
    '''Quadrilaters del Tangram Egípci - Figura 1'''

    name = "figures/figure018a"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,2*X*R5)
    D = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018b():
    '''Quadrilaters del Tangram Egípci - Figura 2'''

    name = "figures/figure018b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (5*X,4*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018c():
    '''Quadrilaters del Tangram Egípci - Figura 3'''

    name = "figures/figure018c"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (4*X,4*X)
    D = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018d():
    '''Quadrilaters del Tangram Egípci - Figura 4'''

    name = "figures/figure018d"

    X = 1 # Scale #
    A = (  0,4*X)
    B = (2*X,4*X)
    C = (10*X,0)
    D = (2*X,0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018e():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure018e"

    X = 1 # Scale #
    A = (  0,  0)
    B = (6*X/R5,12*X/R5)
    D = (4*X*R5, 0)
    C = w_point((2*X*R5,X*R5), D, 4,1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018f():
    '''Quadrilaters del Tangram Egípci - Figura 6'''

    name = "figures/figure018f"

    X = 1 # Scale #
    A = (  0,  0)
    B = (-0.4*X,2.2*X)
    C = (4*X,3*X)
    D = (10*X, 0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018g():
    '''Quadrilaters del Tangram Egípci - Figura 7'''

    name = "figures/figure018g"

    X = 1 # Scale #
    A = (  0,  0)
    B = (3*X,4*X)
    C = (5*X,4*X)
    D = (8*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018h():
    '''Quadrilaters del Tangram Egípci - Figura 8'''

    name = "figures/figure018h"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (5*X,4*X)
    D = (7*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018i():
    '''Quadrilaters del Tangram Egípci - Figura 9'''

    name = "figures/figure018i"

    X = 1 # Scale #
    A = (     0,     0)
    B = (1*X*R5,2*X*R5)
    C = (2*X*R5,2*X*R5)
    D = (3*X*R5,     0)
    E = (1.5*X*R5,0.5*X*R5)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018j():
    '''Quadrilaters del Tangram Egípci - Figura 10'''

    name = "figures/figure018j"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (7*X,4*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018k():
    '''Quadrilaters del Tangram Egípci - Figura 11'''

    name = "figures/figure018k"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,1*X*R5)
    C = (-2*X*R5,2*X*R5)
    D = (-3*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018l():
    '''Quadrilaters del Tangram Egípci - Figura 12'''

    name = "figures/figure018l"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (4*X,3*X)
    D = (10*X, 0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018m():
    '''Quadrilaters del Tangram Egípci - Figura 13'''

    name = "figures/figure018m"

    X = 1 # Scale #
    A = (      0,-1*X*R5)
    B = (-2*X*R5,      0)
    C = (      0, 1*X*R5)
    D = ( 2*X*R5,      0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018n():
    '''Quadrilaters del Tangram Egípci - Figura 14'''

    name = "figures/figure018n"

    X = 1 # Scale #
    A = (   0,-3*X)
    B = (-4*X,   0)
    C = (   0, 2*X)
    D = ( 4*X,   0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018o():
    '''Quadrilaters del Tangram Egípci - Figura 15'''

    name = "figures/figure018o"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,5*X)
    C = (4*X,3*X)
    D = s_point(A, C, 2*R5/5.0)
    E = s_point(B, C, 5/(2*R5))

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s+[trafo.rotate(-(90-3*BETA)/2.0)])

    mycanvas.writePDFfile(name)


def figure018p():
    '''Quadrilaters del Tangram Egípci - Figura 16'''

    name = "figures/figure018p"

    X = 1 # Scale #
    A = (      0,      0)
    B = (1*X*R10,1*X*R10)
    C = (      0,2*X*R10)
    D = (3*X*R10,1*X*R10)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018q():
    '''Quadrilaters del Tangram Egípci - Figura 17'''

    name = "figures/figure018q"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,5*X)
    C = (4*X,3*X)
    D = (8*X,6*X)
    E = (8*X,1*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018r():
    '''Quadrilaters del Tangram Egípci - Figura 18'''

    name = "figures/figure018r"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,1*X*R5)
    D = (4*X*R5,2*X*R5)
    E = (4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018s():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure018s"

    X = 1 # Scale #
    A = (     0,     0)
    B = (   8*X,     0)
    C = (     0,   4*X)
    D = (     0,   6*X)
    E = (  -4*X,   6*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018t():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure018t"

    X = 1 # Scale #
    A = (     0,     0)
    B = (   8*X,     0)
    C = (     0,   4*X)
    D = (     0,   4*X+2*R5*X)
    E = (-4*X/R5,   4*X+X*2.0/R5)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018u():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure018u"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,   4*X)
    C = (   8*X,     0)
    D = (  12*X,     0)
    E = (  12*X,  -2*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018v():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure018v"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,   4*X)
    C = (   8*X,     0)
    D = (8*X+2*R5*X,     0)
    E = (8*X+2*R5*X-X*2.0/R5, -4*X/R5)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018w():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure018w"

    X = 1 # Scale #
    A = (     0,   4*X)
    B = (   8*X,     0)
    C = (     0,     0)
    D = (     0,  -2*X)
    E = (  -4*X,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018x():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure018x"

    X = 1 # Scale #
    A = (     0,   4*X)
    B = (   8*X,     0)
    C = (     0,     0)
    D = (     0,  -4*X)
    E = (  -2*X,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018y():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure018y"

    X = 1 # Scale #
    A = (    6*X,    3*X)
    B = (   10*X,      0)
    C = (      0,      0)
    D = (-2*R5*X,  -R5*X)
    E = (-2*R5*X,      0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018z():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure018z"

    X = 1 # Scale #
    A = (   6*X,   3*X)
    B = (  10*X,     0)
    C = (     0,     0)
    D = (  -4*X,  -2*X)
    E = (  -5*X,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018aa():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure018aa"

    X = 1 # Scale #
    A = (  0,  0)
    B = (-8*X/R5,16*X/R5)
    C = (-8*X/R5,16*X/R5-2*X*R5)
    D = (-4*X*R5, 0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018ab():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure018ab"

    X = 1 # Scale #
    A = (  0,  0)
    B = (4*X,2*X)
    C = (4*X,4*X)
    D = (12*X, 0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018ac():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure018ac"

    X = 1 # Scale #
    A = (  0,  0)
    C = (5*X-X*R5,2*X*R5)
    B = w_point((5*X,0), C,5-R5,R5)
    D = (5*X + 3*X*R5, 0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure018ad():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure018ad"

    X = 1 # Scale #
    A = (  0,  0)
    B = r_point((0,5*X), (0,0), -pi/2+atan2(1,2)+atan2(4,3))
    C = (2*X*R5,1*X*R5)
    D = (4*X*R5, 0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(GREY)+FILLED(GREY)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019a():
    '''Quadrilaters del Tangram Egípci - Figura 1'''

    name = "figures/figure019a"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,2*X*R5)
    D = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019b():
    '''Quadrilaters del Tangram Egípci - Figura 2'''

    name = "figures/figure019b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (5*X,4*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019c():
    '''Quadrilaters del Tangram Egípci - Figura 3'''

    name = "figures/figure019c"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (4*X,4*X)
    D = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019d():
    '''Quadrilaters del Tangram Egípci - Figura 4'''

    name = "figures/figure019d"

    X = 1 # Scale #
    A = (  0,4*X)
    B = (2*X,4*X)
    C = (10*X,0)
    D = (2*X,0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019e():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure019e"

    X = 1 # Scale #
    A = (  0,  0)
    B = (6*X/R5,12*X/R5)
    D = (4*X*R5, 0)
    C = w_point((2*X*R5,X*R5), D, 4,1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019f():
    '''Quadrilaters del Tangram Egípci - Figura 6'''

    name = "figures/figure019f"

    X = 1 # Scale #
    A = (  0,  0)
    B = (-0.4*X,2.2*X)
    C = (4*X,3*X)
    D = (10*X, 0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019g():
    '''Quadrilaters del Tangram Egípci - Figura 7'''

    name = "figures/figure019g"

    X = 1 # Scale #
    A = (  0,  0)
    B = (3*X,4*X)
    C = (5*X,4*X)
    D = (8*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019h():
    '''Quadrilaters del Tangram Egípci - Figura 8'''

    name = "figures/figure019h"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (5*X,4*X)
    D = (7*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019i():
    '''Quadrilaters del Tangram Egípci - Figura 9'''

    name = "figures/figure019i"

    X = 1 # Scale #
    A = (     0,     0)
    B = (1*X*R5,2*X*R5)
    C = (2*X*R5,2*X*R5)
    D = (3*X*R5,     0)
    E = (1.5*X*R5,0.5*X*R5)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019j():
    '''Quadrilaters del Tangram Egípci - Figura 10'''

    name = "figures/figure019j"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (7*X,4*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019k():
    '''Quadrilaters del Tangram Egípci - Figura 11'''

    name = "figures/figure019k"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,1*X*R5)
    C = (-2*X*R5,2*X*R5)
    D = (-3*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019l():
    '''Quadrilaters del Tangram Egípci - Figura 12'''

    name = "figures/figure019l"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (4*X,3*X)
    D = (10*X, 0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019m():
    '''Quadrilaters del Tangram Egípci - Figura 13'''

    name = "figures/figure019m"

    X = 1 # Scale #
    A = (      0,-1*X*R5)
    B = (-2*X*R5,      0)
    C = (      0, 1*X*R5)
    D = ( 2*X*R5,      0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019n():
    '''Quadrilaters del Tangram Egípci - Figura 14'''

    name = "figures/figure019n"

    X = 1 # Scale #
    A = (   0,-3*X)
    B = (-4*X,   0)
    C = (   0, 2*X)
    D = ( 4*X,   0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019o():
    '''Quadrilaters del Tangram Egípci - Figura 15'''

    name = "figures/figure019o"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,5*X)
    C = (4*X,3*X)
    D = s_point(A, C, 2*R5/5.0)
    E = s_point(B, C, 5/(2*R5))

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s+[trafo.rotate(-(90-3*BETA)/2.0)])

    mycanvas.writePDFfile(name)


def figure019p():
    '''Quadrilaters del Tangram Egípci - Figura 16'''

    name = "figures/figure019p"

    X = 1 # Scale #
    A = (      0,      0)
    B = (1*X*R10,1*X*R10)
    C = (      0,2*X*R10)
    D = (3*X*R10,1*X*R10)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019q():
    '''Quadrilaters del Tangram Egípci - Figura 17'''

    name = "figures/figure019q"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,5*X)
    C = (4*X,3*X)
    D = (8*X,6*X)
    E = (8*X,1*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019r():
    '''Quadrilaters del Tangram Egípci - Figura 18'''

    name = "figures/figure019r"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,1*X*R5)
    D = (4*X*R5,2*X*R5)
    E = (4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019s():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure019s"

    X = 1 # Scale #
    A = (     0,     0)
    B = (   8*X,     0)
    C = (     0,   4*X)
    D = (     0,   6*X)
    E = (  -4*X,   6*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019t():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure019t"

    X = 1 # Scale #
    A = (     0,     0)
    B = (   8*X,     0)
    C = (     0,   4*X)
    D = (     0,   4*X+2*R5*X)
    E = (-4*X/R5,   4*X+X*2.0/R5)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019u():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure019u"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,   4*X)
    C = (   8*X,     0)
    D = (  12*X,     0)
    E = (  12*X,  -2*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019v():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure019v"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,   4*X)
    C = (   8*X,     0)
    D = (8*X+2*R5*X,     0)
    E = (8*X+2*R5*X-X*2.0/R5, -4*X/R5)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019w():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure019w"

    X = 1 # Scale #
    A = (     0,   4*X)
    B = (   8*X,     0)
    C = (     0,     0)
    D = (     0,  -2*X)
    E = (  -4*X,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019x():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure019x"

    X = 1 # Scale #
    A = (     0,   4*X)
    B = (   8*X,     0)
    C = (     0,     0)
    D = (     0,  -4*X)
    E = (  -2*X,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019y():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure019y"

    X = 1 # Scale #
    A = (    6*X,    3*X)
    B = (   10*X,      0)
    C = (      0,      0)
    D = (-2*R5*X,  -R5*X)
    E = (-2*R5*X,      0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019z():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure019z"

    X = 1 # Scale #
    A = (   6*X,   3*X)
    B = (  10*X,     0)
    C = (     0,     0)
    D = (  -4*X,  -2*X)
    E = (  -5*X,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019aa():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure019aa"

    X = 1 # Scale #
    A = (  0,  0)
    B = (-8*X/R5,16*X/R5)
    C = (-8*X/R5,16*X/R5-2*X*R5)
    D = (-4*X*R5, 0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019ab():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure019ab"

    X = 1 # Scale #
    A = (  0,  0)
    B = (4*X,2*X)
    C = (4*X,4*X)
    D = (12*X, 0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019ac():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure019ac"

    X = 1 # Scale #
    A = (  0,  0)
    C = (5*X-X*R5,2*X*R5)
    B = w_point((5*X,0), C,5-R5,R5)
    D = (5*X + 3*X*R5, 0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019ad():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure019ad"

    X = 1 # Scale #
    A = (  0,  0)
    B = r_point((0,5*X), (0,0), -pi/2+atan2(1,2)+atan2(4,3))
    C = (2*X*R5,1*X*R5)
    D = (4*X*R5, 0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020a():
    '''Golden Rectangle'''

    name = "figures/figure020a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(E,C, 5-R5, R5)
    K = ((X*(1.0+R5))/2., 0)
    L = ((X*(1.0+R5))/2., X)
    drawing = []


    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*L),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+DASHED))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*J),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020b():
    '''Golden Rectangle'''

    name = "figures/figure020b"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(E,C, 5-R5, R5)
    K = ((X*(1.0+R5))/2., 0)
    L = ((X*(1.0+R5))/2., X)
    drawing = []


    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*L),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+DASHED))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020c():
    '''Golden Rectangle'''

    name = "figures/figure020c"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(E,C, 5-R5, R5)
    K = ((X*(1.0+R5))/2., 0)
    L = ((X*(1.0+R5))/2., X)
    M = (K[0]+C[0]-J[0], K[1]+C[1]-J[1])
    N = w_point(J,K, 1, R5-1)
    O = (J[0]+L[0]-N[0], J[1]+L[1]-N[1])
    Q = (    0, X/2.0-X/(2*R5))
    R = (-X/R5, X/2.0-X/(2*R5))
    S = (-X/R5, 0)
    T = (R[0]+B[0]-I[0], R[1]+B[1]-I[1])
    drawing = []


    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*R),
                              path.lineto(*T),
                              path.closepath()), BASE+THICK+DASHED))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*Q),
                              path.lineto(*R),
                              path.lineto(*S),
                              path.closepath()), BASE+THICK+DASHED))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*Q),
                              path.lineto(*R),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*E),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020d():
    '''Golden Rectangle'''

    name = "figures/figure020d"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(E, C, 5-R5, R5)
    K = ((X*(1.0+R5))/2., 0)
    L = ((X*(1.0+R5))/2., X)
    M = (K[0]+C[0]-J[0], K[1]+C[1]-J[1])
    N = w_point(J,K, 1, R5-1)
    O = (J[0]+L[0]-N[0], J[1]+L[1]-N[1])
    Q = (    0, X/2.0-X/(2*R5))
    R = (-X/R5, X/2.0-X/(2*R5))
    S = (-X/R5, 0)
    T = (R[0]+B[0]-I[0], R[1]+B[1]-I[1])
    drawing = []


    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*L),
                              path.lineto(*N),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+DASHED))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*J),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*L),
                              path.lineto(*N),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*I),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020e():
    '''Golden Rectangle'''

    name = "figures/figure020e"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(E,C, 5-R5, R5)
    K = ((X*(1.0+R5))/2., 0)
    L = ((X*(1.0+R5))/2., X)
    M = (K[0]+C[0]-J[0], K[1]+C[1]-J[1])
    N = w_point(J,K, 1, R5-1)
    O = (J[0]+L[0]-N[0], J[1]+L[1]-N[1])
    Q = (    0, X/2.0-X/(2*R5))
    R = (-X/R5, X/2.0-X/(2*R5))
    S = (-X/R5, 0)
    T = (R[0]+B[0]-I[0], R[1]+B[1]-I[1])
    drawing = []


    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*M),
                              path.lineto(*K),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+DASHED))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*J),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020f():
    '''Golden Rectangle'''

    name = "figures/figure020f"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(E, C, 5-R5, R5)
    K = ((X*(1.0+R5))/2., 0)
    L = ((X*(1.0+R5))/2., X)
    M = (K[0]+C[0]-J[0], K[1]+C[1]-J[1])
    N = w_point(J,K, 1, R5-1)
    O = (J[0]+L[0]-N[0], J[1]+L[1]-N[1])
    Q = (    0, X/2.0-X/(2*R5))
    R = (-X/R5, X/2.0-X/(2*R5))
    S = (-X/R5, 0)
    T = (R[0]+B[0]-I[0], R[1]+B[1]-I[1])
    U = w_point(D,C, 1, R5-1)
    V = (U[0]+2*X/R5, U[1])
    W = (V[0],           0)
    drawing = []


    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*U),
                              path.lineto(*V),
                              path.lineto(*W),
                              path.closepath()), BASE+THICK+DASHED))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*E),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*U),
                              path.lineto(*V),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*I),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure021():
    '''All 32 classes of figures'''

    name = "figures/figure021"

    c_T1 = [color.grey(0.80), color.grey(0.50)]
    c_T4 = [color.grey(0.80), color.grey(0.50)]
    c_T5 = [color.grey(0.80), color.grey(0.50)]
    c_T6 = [color.grey(0.80), color.grey(0.50)]
    c_Q4 = [color.grey(0.80), color.grey(0.50)]

    X = 1.0

    for (T1,T4,T5,T6,Q4) in product((0,1), repeat=5):

        A = (3*X, 0*X)
        B = (0*X, 4*X)
        C = (4*X, 2*X)
        D = (0*X, 0*X)
        E = (2*X, 4*X)
        F = (2*X, 3*X)
        G = (6*X, 3*X)
        H = (6*X, 1*X)
        I = (6*X, 0*X)

        if T1+T5 == 1: E = flip(E, B,F)
        if T4+T5 == 1: G = flip(G, F,H)
        if T6+T5 == 1: D = flip(D, A,B)
        if Q4+T5 == 1: I = flip(I, A,H)
        if T5:
            A = (-A[0], A[1])
            B = (-B[0], B[1])
            C = (-C[0], C[1])
            D = (-D[0], D[1])
            E = (-E[0], E[1])
            F = (-F[0], F[1])
            G = (-G[0], G[1])
            H = (-H[0], H[1])
            I = (-I[0], I[1])

        drawing = []
        drawing.append((path.path(path.moveto(*A),
                                  path.lineto(*B),
                                  path.lineto(*D),
                                  path.closepath()), BASE+ULTRATHIN+COLOR(BLACK)+FILLED(c_T6[T6])))
        drawing.append((path.path(path.moveto(*A),
                                  path.lineto(*B),
                                  path.lineto(*C),
                                  path.closepath()), BASE+ULTRATHIN+COLOR(BLACK)+FILLED(c_T5[T5])))
        drawing.append((path.path(path.moveto(*F),
                                  path.lineto(*G),
                                  path.lineto(*H),
                                  path.closepath()), BASE+ULTRATHIN+COLOR(BLACK)+FILLED(c_T4[T4])))
        drawing.append((path.path(path.moveto(*B),
                                  path.lineto(*E),
                                  path.lineto(*F),
                                  path.closepath()), BASE+ULTRATHIN+COLOR(BLACK)+FILLED(c_T1[T1])))
        drawing.append((path.path(path.moveto(*A),
                                  path.lineto(*C),
                                  path.lineto(*H),
                                  path.lineto(*I),
                                  path.closepath()), BASE+ULTRATHIN+COLOR(BLACK)+FILLED(c_Q4[Q4])))

        mycanvas = canvas.canvas()
        for (p, s) in drawing: mycanvas.stroke(p, s)
        code = "".join("nr"[i] for i in (T1,T4,T5,T6,Q4))
        mycanvas.writePDFfile(name+code)


################################################################################

if __name__ == "__main__":

    figure000a()
    figure000b()
    figure000c()
    figure000d()
    figure000e()
    figure000f()
    figure001a()
    figure001b()
    figure001c()
    figure001d()
    figure001e()
    figure001f()
    figure001g()
    figure001h()
    figure002a()
    figure002b()
    figure002c()
    figure002d()
    figure002e()
    figure002f()
    figure002g()
    figure002h()
    figure002i()
    figure002j()
    figure002k()
    figure003a()
    figure003b()
    figure003c()
    figure004a()
    figure004b()
    figure004c()
    figure004d()
    figure004e()
    figure004f()
    figure004g()
    figure004h()
    figure004i()
    figure004j()
    figure004k()
    figure004l()
    figure004m()
    figure005a()
    figure005b()
    figure005c()
    figure006a()
    figure006b()
    figure006c()
    figure006d()
    figure006e()
    figure006f()
    figure006g()
    figure006h()
    figure006i()
    figure007a()
    figure007b()
    figure008ag()
    figure008bg()
    figure008cg()
    figure008dg()
    figure008eg()
    figure008fg()
    figure008gg()
    figure008ak()
    figure008bk()
    figure008ck()
    figure008dk()
    figure008ek()
    figure008fk()
    figure008gk()
    figure008ab()
    figure008bb()
    figure008cb()
    figure008db()
    figure008eb()
    figure008fb()
    figure008gb()
    figure008ay()
    figure008by()
    figure008cy()
    figure008dy()
    figure008ey()
    figure008fy()
    figure008gy()
    figure009()
    figure009b()
    figure009c()
    figure009d()
    figure009e()
    figure009f()
    figure009g()
    figure009h()
    figure009i()
    figure010a()
    figure010b()
    figure010c()
    figure010d()
    figure010e()
    figure010f()
    figure010g()
    figure010h()
    figure010i()
    figure010j()
    figure010k()
    figure010l()
    figure010m()
    figure011a()
    figure011b()
    figure011c()
    figure012a()
    figure012b()
    figure012c()
    figure012d()
    figure012e()
    figure012f()
    figure012g()
    figure012h()
    figure012i()
    figure012j()
    figure012k()
    figure012l()
    figure012m()
    figure012n()
    figure012o()
    figure012p()
    figure012q()
    figure012r()
    figure012s()
    figure012t()
    figure012u()
    figure012v()
    figure012w()
    figure012x()
    figure012y()
    figure012z()
    figure013a()
    figure013b()
    figure013c()
    figure013d()
    figure013e()
    figure013f()
    figure013g()
    figure013h()
    figure013i()
    figure013j()
    figure013k()
    figure013l()
    figure013m()
    figure013n()
    figure013o()
    figure013p()
    figure013q()
    figure013r()
    figure013s()
    figure014a()
    figure014b()
    figure014c()
    figure014d()
    figure014e()
    figure014f()
    figure014g()
    figure014h()
    figure014i()
    figure014j()
    figure015a()
    figure015b()
    figure015c()
    figure015d()
    figure015e()
    figure015f()
    figure016a()
    figure016b()
    figure016c()
    figure016d()
    figure016e()
    figure016f()
    figure016g()
    figure016h()
    figure016i()
    figure016j()
    figure016k()
    figure016l()
    figure016m()
    figure016n()
    figure016o()
    figure016p()
    figure016q()
    figure016r()
    figure016s()
    figure016t()
    figure016u()
    figure016v()
    figure016w()
    figure016x()
    figure016y()
    figure016z()
    figure016aa()
    figure016ab()
    figure016ac()
    figure016ad()
    figure016ae()
    figure016af()
    figure016ag()
    figure016ah()
    figure016ai()
    figure016aj()
    figure016ak()
    figure016al()
    figure016am()
    figure016an()
    figure016ao()
    figure016ap()
    figure016aq()
    figure016ar()
    figure016as()
    figure016at()
    figure016au()
    figure016av()
    figure016aw()
    figure016ax()
    figure016ay()
    figure016az()
    figure016ba()
    figure016bb()
    figure016bc()
    figure016bd()
    figure016be()
    figure016bf()
    figure016bg()
    figure016bh()
    figure016bi()
    figure016bj()
    figure016bk()
    figure016bl()
    figure016bm()
    figure016bn()
    figure016bo()
    figure016bp()
    figure016bq()
    figure016br()
    figure016bs()
    figure016bt()
    figure016bu()
    figure016bv()
    figure016bw()
    figure016bx()
    figure016by()
    figure016bz()
    figure016ca()
    figure016cb()
    figure016cc()
    figure016cd()
    figure016ce()
    figure016cf()
    figure018a()
    figure018b()
    figure018c()
    figure018d()
    figure018e()
    figure018f()
    figure018g()
    figure018h()
    figure018i()
    figure018j()
    figure018k()
    figure018l()
    figure018m()
    figure018n()
    figure018o()
    figure018p()
    figure018q()
    figure018r()
    figure018s()
    figure018t()
    figure018u()
    figure018v()
    figure018w()
    figure018x()
    figure018y()
    figure018z()
    figure018aa()
    figure018ab()
    figure018ac()
    figure018ad()
    figure019a()
    figure019b()
    figure019c()
    figure019d()
    figure019e()
    figure019f()
    figure019g()
    figure019h()
    figure019i()
    figure019j()
    figure019k()
    figure019l()
    figure019m()
    figure019n()
    figure019o()
    figure019p()
    figure019q()
    figure019r()
    figure019s()
    figure019t()
    figure019u()
    figure019v()
    figure019w()
    figure019x()
    figure019y()
    figure019z()
    figure019aa()
    figure019ab()
    figure019ac()
    figure019ad()
    figure020a()
    figure020b()
    figure020c()
    figure020d()
    figure020e()
    figure020f()
    figure021()
