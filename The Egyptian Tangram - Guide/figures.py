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

# CONSTANTS
BETA = 180*atan2(1,2)/pi
R2  = sqrt(2.0)
R3  = sqrt(3.0)
R5  = sqrt(5.0)
R10 = sqrt(10.0)

# COLOR PALETTE
WHITE    = color.grey.white
BLACK    = color.grey(0.10)
GREY     = color.grey(0.50)
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


def figure019():
    '''El Tangram Egípci - 5 cercles notables'''

    name = "figures/figure019"

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


def figure019b():
    '''El Tangram Egípci - El quadrilater es ciclic'''

    name = "figures/figure019b"

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


def figure019c():
    '''El Tangram Egípci - 4 circumcircles'''

    name = "figures/figure019c"

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


def figure019d():
    '''El Tangram Egípci - 2 tangent circles'''

    name = "figures/figure019d"

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


def figure019e():
    '''El Tangram Egípci - 1 tangent circle'''

    name = "figures/figure019e"

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


def figure019f():
    '''The Egyptian Tangram'''

    name = "figures/figure019f"

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


def figure019g():
    '''El Tangram Egípci - 2 circumcircles and 1 incircle'''

    name = "figures/figure019g"

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


def figure019h():
    '''The Egyptian Tangram'''

    name = "figures/figure019h"

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


def figure020a():
    '''T1+Q4'''

    name = "figures/figure020a"

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


def figure020b():
    '''T5'''

    name = "figures/figure020b"

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


def figure020c():
    '''T1+T4'''

    name = "figures/figure020c"

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


def figure020d():
    '''T1+Q4+T5'''

    name = "figures/figure020d"

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


def figure020e():
    '''T4+T6'''

    name = "figures/figure020e"

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


def figure020f():
    '''T1+Q4+T5'''

    name = "figures/figure020f"

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


def figure020g():
    '''T4+T6'''

    name = "figures/figure020g"

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


def figure020h():
    '''T6+Q4'''

    name = "figures/figure020h"

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


def figure020i():
    '''T6+Q4'''

    name = "figures/figure020i"

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


def figure020j():
    '''T1+T4+T5+Q4'''

    name = "figures/figure020j"

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


def figure020k():
    '''T1+T4+T5+Q4'''

    name = "figures/figure020k"

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


def figure020l():
    '''T1+T4+T5+Q4'''

    name = "figures/figure020l"

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


def figure020m():
    '''T1+T4+T5+Q4'''

    name = "figures/figure020m"

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


def figure021a():
    '''El Tangram Egípci - Quadrat 1'''

    name = "figures/figure021a"

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


def figure021b():
    '''El Tangram Egípci - Quadrat 2'''

    name = "figures/figure021b"

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


def figure021c():
    '''El Tangram Egípci - Quadrat 3'''

    name = "figures/figure021c"

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


def figure022a():
    '''El Tangram Egípci - Figura 1'''

    name = "figures/figure022a"

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


def figure022b():
    '''El Tangram Egípci - Figura 2'''

    name = "figures/figure022b"

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


def figure022c():
    '''El Tangram Egípci - Figura 3'''

    name = "figures/figure022c"

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


def figure022d():
    '''El Tangram Egípci - Figura 4'''

    name = "figures/figure022d"

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


def figure022e():
    '''El Tangram Egípci - Figura 5'''

    name = "figures/figure022e"

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


def figure022f():
    '''El Tangram Egípci - Figura 6'''

    name = "figures/figure022f"

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


def figure022g():
    '''El Tangram Egípci - Figura 7'''

    name = "figures/figure022g"

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


def figure022h():
    '''El Tangram Egípci - Figura 8'''

    name = "figures/figure022h"

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


def figure022i():
    '''El Tangram Egípci - Figura 9'''

    name = "figures/figure022i"

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


def figure022j():
    '''El Tangram Egípci - Figura 10'''

    name = "figures/figure022j"

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


def figure022k():
    '''El Tangram Egípci - Figura 11'''

    name = "figures/figure022k"

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


def figure022l():
    '''El Tangram Egípci - Figura 12'''

    name = "figures/figure022l"

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


def figure022m():
    '''El Tangram Egípci - Figura 13'''

    name = "figures/figure022m"

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


def figure022n():
    '''El Tangram Egípci - Figura 14'''

    name = "figures/figure022n"

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


def figure022o():
    '''El Tangram Egípci - Figura 15'''

    name = "figures/figure022o"

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


def figure022p():
    '''El Tangram Egípci - Figura 16'''

    name = "figures/figure022p"

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


def figure022q():
    '''El Tangram Egípci - Figura 17'''

    name = "figures/figure022q"

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


def figure022r():
    '''El Tangram Egípci - Figura 18'''

    name = "figures/figure022r"

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


def figure022s():
    '''El Tangram Egípci - Figura 19'''

    name = "figures/figure022s"

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


def figure022t():
    '''El Tangram Egípci - Figura 20'''

    name = "figures/figure022t"

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


def figure022u():
    '''El Tangram Egípci - Figura 21'''

    name = "figures/figure022u"

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


def figure022v():
    '''El Tangram Egípci - Figura 22'''

    name = "figures/figure022v"

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


def figure022w():
    '''El Tangram Egípci - Figura 23'''

    name = "figures/figure022w"

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


def figure022x():
    '''El Tangram Egípci - Figura 24'''

    name = "figures/figure022x"

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


def figure023a():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure023a"

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


def figure023b():
    '''El Subtangram Egípci - Figura 2'''

    name = "figures/figure023b"

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


def figure023c():
    '''El Subtangram Egípci - Figura 3'''

    name = "figures/figure023c"

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


def figure023d():
    '''El Subtangram Egípci - Figura 4'''

    name = "figures/figure023d"

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


def figure023e():
    '''El Subtangram Egípci - Figura 5'''

    name = "figures/figure023e"

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


def figure023f():
    '''El Subtangram Egípci - Figura 6'''

    name = "figures/figure023f"

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


def figure023g():
    '''El Subtangram Egípci - Figura 7'''

    name = "figures/figure023g"

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


def figure023h():
    '''El Subtangram Egípci - Figura 8'''

    name = "figures/figure023h"

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


def figure023i():
    '''El Subtangram Egípci - Figura 9'''

    name = "figures/figure023i"

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


def figure024a():
    '''El Tangram Egípci - Triangle 1:2'''

    name = "figures/figure024a"

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


def figure024b():
    '''El Tangram Egípci - Triangle 2:4'''

    name = "figures/figure024b"

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


def figure024c():
    '''El Tangram Egípci - Triangle sqrt(5):2*sqrt(5)'''

    name = "figures/figure024c"

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


def figure024d():
    '''El Tangram Egípci - Triangle 3:6'''

    name = "figures/figure024d"

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


def figure024e():
    '''El Tangram Egípci - Triangle 4:8'''

    name = "figures/figure024e"

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


def figure024f():
    '''El Tangram Egípci - Triangle 2*sqrt(5):4*sqrt(5)'''

    name = "figures/figure024f"

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


def figure024g():
    '''El Tangram Egípci - Triangle 5:10:3*sqrt(5)'''

    name = "figures/figure024g"

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


def figure024h():
    '''El Tangram Egípci - Triangle 5:4*sqrt(5):5'''

    name = "figures/figure024h"

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


def figure024i():
    '''El Tangram Egípci - Triangle 5:2*sqrt(5):5'''

    name = "figures/figure024i"

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


def figure024j():
    '''El Tangram Egípci - Triangle 3:4:5'''

    name = "figures/figure024j"

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


def figure025a():
    '''El Tangram Egípci - Suma de figures semblants 1'''

    name = "figures/figure025a"

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


def figure025b():
    '''El Tangram Egípci - Suma de figures semblants 2'''

    name = "figures/figure025b"

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


def figure025c():
    '''El Tangram Egípci - Suma de figures semblants 3'''

    name = "figures/figure025c"

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


def figure025d():
    '''El Tangram Egípci - Suma de figures semblants 4'''

    name = "figures/figure025d"

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


def figure025e():
    '''El Tangram Egípci - Suma de figures semblants 5'''

    name = "figures/figure025e"

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


def figure025f():
    '''El Tangram Egípci - Suma de figures semblants 6'''

    name = "figures/figure025f"

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


def figure026a():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026a"

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


def figure026b():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026b"

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


def figure026c():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026c"

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


def figure026d():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026d"

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


def figure026e():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026e"

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


def figure026f():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026f"

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


def figure026g():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026g"

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


def figure026h():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026h"

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


def figure026i():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026i"

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


def figure026j():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026j"

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


def figure026k():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026k"

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


def figure026l():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026l"

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


def figure026m():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026m"

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


def figure026n():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026n"

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


def figure026o():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026o"

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


def figure026p():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026p"

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


def figure026q():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026q"

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


def figure026r():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026r"

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


def figure026s():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026s"

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


def figure026t():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026t"

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


def figure026u():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026u"

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


def figure026v():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026v"

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


def figure026w():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026w"

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


def figure026x():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026x"

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


def figure026y():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026y"

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


def figure026z():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026z"

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


def figure026aa():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026aa"

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


def figure026ab():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026ab"

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


def figure028a():
    '''Quadrilaters del Tangram Egípci - Figura 1'''

    name = "figures/figure028a"

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


def figure028b():
    '''Quadrilaters del Tangram Egípci - Figura 2'''

    name = "figures/figure028b"

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


def figure028c():
    '''Quadrilaters del Tangram Egípci - Figura 3'''

    name = "figures/figure028c"

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


def figure028d():
    '''Quadrilaters del Tangram Egípci - Figura 4'''

    name = "figures/figure028d"

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


def figure028e():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure028e"

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


def figure028f():
    '''Quadrilaters del Tangram Egípci - Figura 6'''

    name = "figures/figure028f"

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


def figure028g():
    '''Quadrilaters del Tangram Egípci - Figura 7'''

    name = "figures/figure028g"

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


def figure028h():
    '''Quadrilaters del Tangram Egípci - Figura 8'''

    name = "figures/figure028h"

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


def figure028i():
    '''Quadrilaters del Tangram Egípci - Figura 9'''

    name = "figures/figure028i"

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


def figure028j():
    '''Quadrilaters del Tangram Egípci - Figura 10'''

    name = "figures/figure028j"

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


def figure028k():
    '''Quadrilaters del Tangram Egípci - Figura 11'''

    name = "figures/figure028k"

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


def figure028l():
    '''Quadrilaters del Tangram Egípci - Figura 12'''

    name = "figures/figure028l"

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


def figure028m():
    '''Quadrilaters del Tangram Egípci - Figura 13'''

    name = "figures/figure028m"

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


def figure028n():
    '''Quadrilaters del Tangram Egípci - Figura 14'''

    name = "figures/figure028n"

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


def figure028o():
    '''Quadrilaters del Tangram Egípci - Figura 15'''

    name = "figures/figure028o"

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


def figure028p():
    '''Quadrilaters del Tangram Egípci - Figura 16'''

    name = "figures/figure028p"

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


def figure028q():
    '''Quadrilaters del Tangram Egípci - Figura 17'''

    name = "figures/figure028q"

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


def figure028r():
    '''Quadrilaters del Tangram Egípci - Figura 18'''

    name = "figures/figure028r"

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


def figure028s():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure028s"

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


def figure028t():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure028t"

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


def figure028u():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure028u"

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
    

def figure028v():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure028v"

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
    

def figure028w():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure028w"

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
    

def figure028x():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure028x"

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
    

def figure028y():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure028y"

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
    

def figure028z():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure028z"

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
    

def figure028aa():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure028aa"

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


def figure028ab():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure028ab"

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


def figure028ac():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure028ac"

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


def figure028ad():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure028ad"

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


def figure029a():
    '''Quadrilaters del Tangram Egípci - Figura 1'''

    name = "figures/figure029a"

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


def figure029b():
    '''Quadrilaters del Tangram Egípci - Figura 2'''

    name = "figures/figure029b"

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


def figure029c():
    '''Quadrilaters del Tangram Egípci - Figura 3'''

    name = "figures/figure029c"

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


def figure029d():
    '''Quadrilaters del Tangram Egípci - Figura 4'''

    name = "figures/figure029d"

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


def figure029e():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure029e"

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


def figure029f():
    '''Quadrilaters del Tangram Egípci - Figura 6'''

    name = "figures/figure029f"

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


def figure029g():
    '''Quadrilaters del Tangram Egípci - Figura 7'''

    name = "figures/figure029g"

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


def figure029h():
    '''Quadrilaters del Tangram Egípci - Figura 8'''

    name = "figures/figure029h"

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


def figure029i():
    '''Quadrilaters del Tangram Egípci - Figura 9'''

    name = "figures/figure029i"

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


def figure029j():
    '''Quadrilaters del Tangram Egípci - Figura 10'''

    name = "figures/figure029j"

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


def figure029k():
    '''Quadrilaters del Tangram Egípci - Figura 11'''

    name = "figures/figure029k"

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


def figure029l():
    '''Quadrilaters del Tangram Egípci - Figura 12'''

    name = "figures/figure029l"

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


def figure029m():
    '''Quadrilaters del Tangram Egípci - Figura 13'''

    name = "figures/figure029m"

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


def figure029n():
    '''Quadrilaters del Tangram Egípci - Figura 14'''

    name = "figures/figure029n"

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


def figure029o():
    '''Quadrilaters del Tangram Egípci - Figura 15'''

    name = "figures/figure029o"

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


def figure029p():
    '''Quadrilaters del Tangram Egípci - Figura 16'''

    name = "figures/figure029p"

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


def figure029q():
    '''Quadrilaters del Tangram Egípci - Figura 17'''

    name = "figures/figure029q"

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


def figure029r():
    '''Quadrilaters del Tangram Egípci - Figura 18'''

    name = "figures/figure029r"

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


def figure029s():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure029s"

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


def figure029t():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure029t"

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


def figure029u():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure029u"

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
    

def figure029v():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure029v"

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
    

def figure029w():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure029w"

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
    

def figure029x():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure029x"

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
    

def figure029y():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure029y"

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
    

def figure029z():
    '''Quadrilaters del Tangram Egípci - Figura 19'''

    name = "figures/figure029z"

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
    

def figure029aa():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure029aa"

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


def figure029ab():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure029ab"

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


def figure029ac():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure029ac"

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


def figure029ad():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure029ad"

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


def figure030a():
    '''Golden Rectangle'''

    name = "figures/figure030a"

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


def figure030b():
    '''Golden Rectangle'''

    name = "figures/figure030b"

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


def figure030c():
    '''Golden Rectangle'''

    name = "figures/figure030c"

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


def figure030d():
    '''Golden Rectangle'''

    name = "figures/figure030d"

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


def figure030e():
    '''Golden Rectangle'''

    name = "figures/figure030e"

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


def figure030f():
    '''Golden Rectangle'''

    name = "figures/figure030f"

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


################################################################################

if __name__ == "__main__":

    figure000a()
    figure000b()
    figure000c()
    figure000d()
    figure000e()
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
    figure019()
    figure019b()
    figure019c()
    figure019d()
    figure019e()
    figure019f()
    figure019g()
    figure019h()
    figure020a()
    figure020b()
    figure020c()
    figure020d()
    figure020e()
    figure020f()
    figure020g()
    figure020h()
    figure020i()
    figure020j()
    figure020k()
    figure020l()
    figure020m()
    figure021a()
    figure021b()
    figure021c()
    figure022a()
    figure022b()
    figure022c()
    figure022d()
    figure022e()
    figure022f()
    figure022g()
    figure022h()
    figure022i()
    figure022j()
    figure022k()
    figure022l()
    figure022m()
    figure022n()
    figure022o()
    figure022p()
    figure022q()
    figure022r()
    figure022s()
    figure022t()
    figure022u()
    figure022v()
    figure022w()
    figure022x()
    figure023a()
    figure023b()
    figure023c()
    figure023d()
    figure023e()
    figure023f()
    figure023g()
    figure023h()
    figure023i()
    figure024a()
    figure024b()
    figure024c()
    figure024d()
    figure024e()
    figure024f()
    figure024g()
    figure024h()
    figure024i()
    figure024j()
    figure025a()
    figure025b()
    figure025c()
    figure025d()
    figure025e()
    figure025f()
    figure026a()
    figure026b()
    figure026c()
    figure026d()
    figure026e()
    figure026f()
    figure026g()
    figure026h()
    figure026i()
    figure026j()
    figure026k()
    figure026l()
    figure026m()
    figure026n()
    figure026o()
    figure026p()
    figure026q()
    figure026r()
    figure026s()
    figure026t()
    figure026u()
    figure026v()
    figure026w()
    figure026x()
    figure026y()
    figure026z()
    figure026aa()
    figure026ab()
    figure028a()
    figure028b()
    figure028c()
    figure028d()
    figure028e()
    figure028f()
    figure028g()
    figure028h()
    figure028i()
    figure028j()
    figure028k()
    figure028l()
    figure028m()
    figure028n()
    figure028o()
    figure028p()
    figure028q()
    figure028r()
    figure028s()
    figure028t()
    figure028u()
    figure028v()
    figure028w()
    figure028x()
    figure028y()
    figure028z()
    figure028aa()
    figure028ab()
    figure028ac()
    figure028ad()
    figure029a()
    figure029b()
    figure029c()
    figure029d()
    figure029e()
    figure029f()
    figure029g()
    figure029h()
    figure029i()
    figure029j()
    figure029k()
    figure029l()
    figure029m()
    figure029n()
    figure029o()
    figure029p()
    figure029q()
    figure029r()
    figure029s()
    figure029t()
    figure029u()
    figure029v()
    figure029w()
    figure029x()
    figure029y()
    figure029z()
    figure029aa()
    figure029ab()
    figure029ac()
    figure029ad()
    figure030a()
    figure030b()
    figure030c()
    figure030d()
    figure030e()
    figure030f()
