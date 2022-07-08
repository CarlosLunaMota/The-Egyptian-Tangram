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
R2   = sqrt(2.0)
R3   = sqrt(3.0)
R5   = sqrt(5.0)
R10  = sqrt(10.0)

# COLOR PALETTE
WHITE    = color.grey(0.05)
BLACK    = color.grey(0.90)
D_GREY   = color.grey(0.70)
GREY     = color.grey(0.85)
L_GREY   = color.grey(0.30)
CHALK    = color.grey(0.05)

L_RED      = color.cmyk.Mahogany
L_BLUE     = color.cmyk.NavyBlue
L_GREEN    = color.cmyk.ForestGreen
L_ORANGE   = color.cmyk.Orange
L_YELLOW   = color.cmyk.Dandelion


RED      = color.cmyk.Red
BLUE     = color.cmyk.SkyBlue
GREEN    = color.cmyk.LimeGreen
ORANGE   = color.cmyk.YellowOrange
YELLOW   = color.cmyk.Goldenrod
PLUM     = color.cmyk.Orchid
PINK     = color.cmyk.Lavender
BROWN    = color.cmyk.RawSienna
DBLUE    = color.cmyk.NavyBlue
DGREEN   = color.cmyk.ForestGreen
DARKGREY = color.grey(0.5)
DGREEN   = color.cmyk.ForestGreen

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

def FILLED(color): return [deco.filled([color])]
def COLOR(color):  return [color]

# PYX TEXT SETTINGS:
text.set(text.LatexEngine)
text.preamble(r"\usepackage[utf8]{inputenc}")
text.preamble(r"\usepackage[T1]{fontenc}")

text.preamble(r"\usepackage{xcolor}")
text.preamble(r"\usepackage{lmodern}")
text.preamble(r"\usepackage{textcomp}")
text.preamble(r"\usepackage[cm]{sfmath}")
text.preamble(r"\usepackage[euler]{textgreek}")
text.preamble(r"\renewcommand{\familydefault}{\sfdefault}")

text.preamble(r"\setlength{\fboxsep}{4pt}")
text.preamble(r"\setlength{\fboxrule}{0.75pt}")

text.preamble(r"\usepackage{fancybox}")
text.preamble(r"\newcommand{\button}[1]{\Ovalbox{\parbox[t][1.8ex][c]{2.2em}{\centering #1}}}")

def put_text(x, y, t): return (path.path(path.moveto(x-0.01,y),path.lineto(x+0.01,y)),[deco.curvedtext(t)])

# AUXILIARY FUNCTIONS
def w_point(x, y, Wx, Wy): return ((Wx*x[0]+Wy*y[0])/(Wx+Wy), (Wx*x[1]+Wy*y[1])/(Wx+Wy))
def s_point(x, y, W): return ((W*(y[0]-x[0]))+y[0], (W*(y[1]-x[1]))+y[1])
def r_point(p, c, A): return (c[0]+(p[0]-c[0])*cos(A)-(p[1]-c[1])*sin(A), c[1]+(p[0]-c[0])*sin(A)+(p[1]-c[1])*cos(A))
    
def flip(P, A, B):
    M = ((A[0]+B[0])/2.0, (A[1]+B[1])/2.0)  # Midpoint of the A--B segment
    V = (A[1]-B[1], B[0]-A[0])              # Perpendicular to the A--B line
    W = (P[0]-M[0], P[1]-M[1])              # Vector M->P
    k = (V[0]*W[0] + V[1]*W[1]) / (V[0]*V[0] + V[1]*V[1])
    PPP = (M[0] + k*V[0], M[1] + k*V[1])  # Perpendicular Projection of P
    return (P[0] + 2*(PPP[0]-P[0]), P[1] + 2*(PPP[1]-P[1]))

################################################################################

# OLD FIGURES
def ffigura001():
    '''Tangram Xinés'''

    name = "figures/ffigura001"

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
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura002a():
    '''Silueta Realista'''

    name = "figures/ffigura002a"

    X = R2/2
    A = (  X,  0)
    B = (3*X,  0)
    C = (4*X,  X)
    D = (2*X,  X)
    E = (3*X,2*X)
    F = ((2*R2*X)/2+X, 4*X-R2*X)
    G = (  X,4*X)
    H = (  0,5*X)
    I = (  X,6*X)
    J = (2*X,5*X)
    K = (2*R2*X+X,  4*X)
    L = (2*R2*X,    5*X)
    M = (2*R2*X+X+X,5*X)
    N = (4*X,3*X)
    O = (6*X,  X)
    P = (5.2*X,X)
    Q = (6.2*X,0)
    R = (7.2*X,X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*P),
                              path.lineto(*Q),
                              path.lineto(*R),
                              path.lineto(*O),
                              path.lineto(*N),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*K),
                              path.lineto(*M),
                              path.lineto(*L),
                              path.lineto(*K),
                              path.lineto(*G),
                              path.lineto(*J),
                              path.lineto(*I),
                              path.lineto(*H),
                              path.lineto(*G),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura002b():
    '''Silueta Realista (solución)'''

    name = "figures/ffigura002b"

    X = R2/2
    A = (  X,  0)
    B = (3*X,  0)
    C = (4*X,  X)
    D = (2*X,  X)
    E = (3*X,2*X)
    F = ((2*R2*X)/2+X, 4*X-R2*X)
    G = (  X,4*X)
    H = (  0,5*X)
    I = (  X,6*X)
    J = (2*X,5*X)
    K = (2*R2*X+X,  4*X)
    L = (2*R2*X,    5*X)
    M = (2*R2*X+X+X,5*X)
    N = (4*X,3*X)
    O = (6*X,  X)
    P = (5.2*X,X)
    Q = (6.2*X,0)
    R = (7.2*X,X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*G),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*G),
                              path.lineto(*K),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*L),
                              path.lineto(*M),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*N),
                              path.lineto(*O),
                              path.closepath()), BASE+FILLED(PINK)))
    drawing.append((path.path(path.moveto(*P),
                              path.lineto(*Q),
                              path.lineto(*R),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*P),
                              path.lineto(*Q),
                              path.lineto(*R),
                              path.lineto(*O),
                              path.lineto(*N),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*K),
                              path.lineto(*M),
                              path.lineto(*L),
                              path.lineto(*K),
                              path.lineto(*G),
                              path.lineto(*J),
                              path.lineto(*I),
                              path.lineto(*H),
                              path.lineto(*G),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura003a():
    '''Tangram Xinés - Figura Convexa 1'''

    name = "figures/ffigura003a"

    X = 1.0 # Scale !
    A = (     0,      0)
    B = (     0, 2*R2*X)
    C = (2*R2*X, 2*R2*X)
    D = (2*R2*X,      0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura003b():
    '''Tangram Xinés - Figura Convexa 2'''

    name = "figures/ffigura003b"

    X = 1.0 # Scale !
    A = (     0,      0)
    B = (     0, 2*R2*X)
    C = (1*R2*X, 2*R2*X)
    D = (3*R2*X,      0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura003c():
    '''Tangram Xinés - Figura Convexa 3'''

    name = "figures/ffigura003c"

    X = 1.0 # Scale !
    A = (     0,      0)
    B = (2*R2*X, 2*R2*X)
    C = (4*R2*X,      0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura003d():
    '''Tangram Xinés - Figura Convexa 4'''

    name = "figures/ffigura003d"

    X = 1.0 # Scale !
    A = (  0,   0)
    B = (  0, 2*X)
    C = (1*X, 3*X)
    D = (3*X, 3*X)
    E = (3*X, 1*X)
    F = (2*X,   0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura003e():
    '''Tangram Xinés - Figura Convexa 5'''

    name = "figures/ffigura003e"

    X = 1.0 # Scale !
    A = (  0,   0)
    B = (  0, 2*X)
    C = (1*X, 3*X)
    D = (2*X, 3*X)
    E = (3*X, 2*X)
    F = (3*X,   0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura003f():
    '''Tangram Xinés - Figura Convexa 6'''

    name = "figures/ffigura003f"

    X = 1.0 # Scale !
    A = (  0,   0)
    B = (  0, 1*X)
    C = (2*X, 3*X)
    D = (4*X, 1*X)
    E = (4*X,   0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura003g():
    '''Tangram Xinés - Figura Convexa 7'''

    name = "figures/ffigura003g"

    X = 1.0 # Scale !
    A = (  0,   0)
    B = (  0, 1*X)
    C = (2*X, 3*X)
    D = (4*X, 3*X)
    E = (4*X, 2*X)
    F = (2*X,   0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura003h():
    '''Tangram Xinés - Figura Convexa 8'''

    name = "figures/ffigura003h"

    X = 1.0 # Scale !
    A = (  0,   0)
    B = (3*X, 3*X)
    C = (4*X, 3*X)
    D = (5*X, 2*X)
    E = (3*X,   0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura003i():
    '''Tangram Xinés - Figura Convexa 9'''

    name = "figures/ffigura003i"

    X = 1.0 # Scale !
    A = (  0,   0)
    B = (  0, 2*X)
    C = (4*X, 2*X)
    D = (4*X,   0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura003j():
    '''Tangram Xinés - Figura Convexa 10'''

    name = "figures/ffigura003j"

    X = 1.0 # Scale !
    A = (  0,   0)
    B = (  0, 2*X)
    C = (3*X, 2*X)
    D = (5*X,   0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura003k():
    '''Tangram Xinés - Figura Convexa 11'''

    name = "figures/ffigura003k"

    X = 1.0 # Scale !
    A = (  0,   0)
    B = (2*X, 2*X)
    C = (4*X, 2*X)
    D = (6*X,   0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura003l():
    '''Tangram Xinés - Figura Convexa 12'''

    name = "figures/ffigura003l"

    X = 1.0 # Scale !
    A = (2*X,   0)
    B = (  0, 2*X)
    C = (4*X, 2*X)
    D = (6*X,   0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura003m():
    '''Tangram Xinés - Figura Convexa 13'''

    name = "figures/ffigura003m"

    X = 1.0 # Scale !
    A = (1*X,   0)
    B = (  0, 1*X)
    C = (1*X, 2*X)
    D = (4*X, 2*X)
    E = (5*X, 1*X)
    F = (4*X,   0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura004a():
    '''Paradoxa Triangle Complet'''

    name = "figures/ffigura004a"

    X = R2
    A = (  0,  0)
    B = (4*X,  0)
    C = (2*X,2*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura004b():
    '''Paradoxa Triangle Incomplet'''

    name = "figures/ffigura004b"

    A = (0, 0)
    B = (2, 0)
    C = (2, 1)
    D = (3, 1)
    E = (3, 0)
    F = (4, 0)
    G = (6, 0)
    H = (3, 3)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+FILLED(WHITE)))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura004c():
    '''Paradoxa Triangle Complet Solució'''

    name = "figures/ffigura004c"

    X = R2
    A = (  0,  0)
    B = (4*X,  0)
    C = (2*X,2*X)
    D = w_point(A, B, 1,1)
    E = w_point(A, C, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(C, D, 1,1)
    H = w_point(A, D, 1,1)
    I = w_point(G, H, 1,1)
    J = w_point(A, E, 1,1)
    K = w_point(C, E, 1,1)


    drawing = []
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*H),
                              path.lineto(*G),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*K),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*F),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(PINK)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*D),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*G),
                              path.lineto(*K),
                              path.closepath()), BASE+FILLED(BLUE)))

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura004d():
    '''Paradoxa Triangle Incomplet Solució'''

    name = "figures/ffigura004d"

    A = (0, 0)
    B = (2, 0)
    C = (2, 1)
    D = (3, 1)
    E = (3, 0)
    F = (4, 0)
    G = (6, 0)
    H = (3, 3)
    I = (2, 2)
    J = (4, 2)
    K = (3, 2)
    L = (4, 1)

    drawing = []
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*I),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*I),
                              path.closepath()), BASE+FILLED(PINK)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*G),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*K),
                              path.lineto(*L),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*I),
                              path.lineto(*K),
                              path.lineto(*L),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*L),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura005a():
    '''Dissecció quadrat-dodecagon: quadrat'''

    name = "figures/ffigura005a"

    Y = 4.0/3.0 # scale!
    X = R3*Y/2
    Z = (3*Y+2*X)/R2
    W = Y/R2

    A = (0, 0)
    B = (Z, 0)
    C = (Z, Z)
    D = (0, Z)
    E = (Z/2.0,   Z/2.0-W)
    F = (Z/2.0+W, Z/2.0)
    G = (Z/2.0,   Z/2.0+W)
    H = (Z/2.0-W, Z/2.0)
    I = (Z-W,  W)
    J = (Z-W, Z-W)
    K = ( W,  Z-W)
    L = ( W,   W)
    O = (Z/2.0, Z/2.0)


    drawing = []
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*J),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.lineto(*L),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*L),
                              path.lineto(*E),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*K),
                              path.lineto(*H),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*L),
                              path.lineto(*H),
                              path.lineto(*K),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*K),
                              path.lineto(*G),
                              path.lineto(*J),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura005b():
    '''Dissecció quadrat-dodecagon: dodecagon'''

    name = "figures/ffigura005b"

    Y = 2.0/3.0 # scale!
    X = R3*Y

    A = (   0*Y,     0*Y)
    B = (   2*Y,     0*Y)
    C = ( X+2*Y,     1*Y)
    D = ( X+3*Y,   X+1*Y)
    E = ( X+3*Y,   X+3*Y)
    F = ( X+2*Y, 2*X+3*Y)
    G = (   2*Y, 2*X+4*Y)
    H = (   0*Y, 2*X+4*Y)
    I = (-X,     2*X+3*Y)
    J = (-X-1*Y,   X+3*Y)
    K = (-X-1*Y,   X+1*Y)
    L = (-X,         1*Y)
    M = (   0*Y, 2*X+2*Y)
    N = (   2*Y, 2*X+2*Y)
    O = (   1*Y,   X+2*Y)
    P = (   1*Y,   X)


    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*P),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*N),
                              path.lineto(*O),
                              path.lineto(*P),
                              path.lineto(*B),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*M),
                              path.lineto(*O),
                              path.lineto(*N),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*I),
                              path.lineto(*J),
                              path.lineto(*K),
                              path.lineto(*L),
                              path.lineto(*A),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*P),
                              path.lineto(*O),
                              path.lineto(*M),
                              path.lineto(*I),
                              path.closepath()), BASE+FILLED(PLUM)))
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
                              path.lineto(*L),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura006a():
    '''Tangram Japonés'''

    name = "figures/ffigura006a"

    X = 3*R2
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(E, F, 1,1)
    H = w_point(A, C, 1,1)
    I = w_point(H, C, 1,1)
    J = w_point(C, D, 1,1)
    K = w_point(A, D, 1,1)
    L = w_point(J, K, 1,1)

    drawing = []
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*C),
                              path.lineto(*I),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*J),
                              path.lineto(*K),
                              path.closepath()), BASE+FILLED(PINK)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*K),
                              path.lineto(*L),
                              path.lineto(*I),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*I),
                              path.lineto(*L),
                              path.lineto(*J),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*H),
                              path.lineto(*G),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*F),
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
    

def ffigura006b():
    '''Tangram Double Square'''

    name = "figures/ffigura006b"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, B, 2,1)
    F = w_point(B, C, 1,2)
    G = w_point(C, D, 2,1)
    H = w_point(D, A, 1,2)
    I = w_point(E, F, 1,1)
    J = w_point(D, I, 1,1)
    K = w_point(E, J, 1,1)

    drawing = []
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*B),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*G),
                              path.lineto(*J),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*J),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*K),
                              path.lineto(*H),
                              path.lineto(*D),
                              path.lineto(*I),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*K),
                              path.lineto(*H),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura006c():
    '''Tangram Fletcher'''

    name = "figures/ffigura006c"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(B, C, 1,1)
    F = w_point(C, D, 1,1)
    G = w_point(A, D, 1,1)
    H = w_point(E, G, 1,1)
    I = w_point(H, B, 1,1)
    J = w_point(H, C, 1,1)
    K = w_point(A, B, 1,1)
    
    drawing = []
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*J),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*I),
                              path.closepath()), BASE+FILLED(PINK)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*J),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*G),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*K),
                              path.lineto(*H),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*F),
                              path.lineto(*C),
                              path.lineto(*H),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*K),
                              path.lineto(*H),
                              path.lineto(*G),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura007a():
    '''Tangram de V & Diamond'''

    name = "figures/ffigura007a"

    X = 5.0 # scale!
    Y = X*R3/2

    A = (0,0)
    B = (X,0)
    C = (X,Y)
    D = (0,Y)
    E = w_point(A, B, 1,1)
    F = w_point(D, E, 1,1)
    G = w_point(C, E, 1,1)

    drawing = []
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*F),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura007b():
    '''Tangram de Brügner'''

    name = "figures/ffigura007b"

    PHI = (1.0+R5)/2.0
    Y = 4.0 # scale!
    X = Y*sqrt(PHI)


    A = (0,0)
    B = (X,0)
    C = (X,Y)
    D = (0,Y)
    E = w_point(C, A, 1,PHI-1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*A),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura007c():
    '''Tangram de Pitagoric'''

    name = "figures/ffigura007c"

    X = 1.00 # scale!

    A = (0*X,0*X)
    B = (0*X,4*X)
    C = (5*X,4*X)
    D = (5*X,0*X)
    E = (5*X,2*X)
    F = (0*X,1*X)
    G = (0*X,3*X)
    H = (1*X,4*X)
    I = (3*X,4*X)
    J = (3*X,0*X)
    K = (1*X,0*X)
    L = (2*X,3*X)
    M = (3*X,2*X)
    N = (4*X,1*X)
    O = (2*X,1*X)
    
    drawing = []
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.lineto(*N),
                              path.closepath()), BASE+FILLED(PINK)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*J),
                              path.lineto(*N),
                              path.lineto(*M),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*O),
                              path.lineto(*K),
                              path.lineto(*A),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*D),
                              path.lineto(*J),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.lineto(*I),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*H),
                              path.lineto(*L),
                              path.lineto(*G),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*L),
                              path.lineto(*M),
                              path.lineto(*O),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura008a():
    '''Tangram de l'Ou'''

    name = "figures/ffigura008a"

    X = 1 # scale !
    Y = X*R2/2
    O = (   0, 0)
    A = (-X-Y, 0)
    B = ( X+Y, 0)
    C = ( 0, X+Y)
    D = ( 0,  -Y)
    E = ( 0,-X-Y)
    F = (-Y, X+Y+Y)
    G = ( 0, X+Y+X)
    H = ( Y, X+Y+Y)
    I = (-Y,   0)
    J = ( Y,   0)


    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*O),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*C),
                              path.lineto(*B),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+FILLED(DGREEN)))
    drawing.append((path.path(path.moveto(*C),
                              path.arc(0,X+Y, X, 45, 90),
                              path.closepath()), BASE+FILLED(BROWN)))
    drawing.append((path.path(path.moveto(*C),
                              path.arc(0,X+Y, X, 90, 135),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*B),
                              path.arc(-X-Y,0, X+X+Y+Y, 0, 45),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(PINK)))
    drawing.append((path.path(path.moveto(*F),
                              path.arc(X+Y,0, X+X+Y+Y, 135, 180),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*I),
                              path.lineto(*A),
                              path.arc(0,0, X+Y, 180, 270),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.arc(0,0, X+Y, 270, 360),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.arc(0,0, Y+X, 180, 360),
                              path.arc(-X-Y,0, Y+X+Y+X, 0, 45),
                              path.arc(0,X+Y, X, 45, 135),
                              path.arc(X+Y,0, Y+X+Y+X, 135, 180),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura008b():
    '''Tangram del Cor'''

    name = "figures/ffigura008b"

    X = 1.5 # scale !
    Y = X*R2/2
    O = (   0, 0)
    A = (-2*Y, 0)
    B = (   0,-2*Y)
    C = ( 2*Y, 0)
    D = (   0, 2*Y)
    E = w_point(A,D,1,1)
    F = w_point(D,C,1,1)
    G = w_point(C,B,1,1)
    H = (-2*Y, 2*Y)
    I = ( 2*Y, 2*Y)

    drawing = []
    drawing.append((path.path(path.moveto(*H),
                              path.arc(-Y,Y, X, 135, 225),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*D),
                              path.arc(-Y,Y, X, 45, 135),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*I),
                              path.arc(Y,Y, X, 45, 135),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(PINK)))
    drawing.append((path.path(path.moveto(*C),
                              path.arc(Y,Y, X, -45, 45),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(DGREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*O),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*O),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*E),
                              path.lineto(*A),
                              path.lineto(*B),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.arc(Y,Y,X,-45,135),
                              path.arc(-Y,Y,X,45,225),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura008c():
    '''Tangram Circular 1'''

    name = "figures/ffigura008c"

    X = 1.0  # scale !
    Y = X/R2

    O = (   0,   0)
    A = (   0, 3*X)
    B = ( 3*X,   0)
    C = (   0,-3*X)
    D = (-3*X,   0)
    E = (   0,   X)
    F = (   X,   0)
    G = (   0,  -X)
    H = (  -X,   0)
    I = (   Y,   Y)
    J = ( 3*Y, 3*Y)
    
    drawing = []
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*B),
                              path.arc(0,0, 3*X, 0, 45),
                              path.lineto(*I),
                              path.arcn(0,0,  X, 45, 0),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*I),
                              path.lineto(*J),
                              path.arc(0,0, 3*X, 45, 90),
                              path.lineto(*E),
                              path.arcn(0,0,  X, 90, 45),
                              path.closepath()), BASE+FILLED(PINK)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*A),
                              path.arc(0,0, 3*X, 90, 180),
                              path.lineto(*H),
                              path.arcn(0,0,  X, 180, 90),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*D),
                              path.arc(0,0, 3*X, 180, 270),
                              path.lineto(*G),
                              path.arcn(0,0,  X, 270, 180),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*C),
                              path.arc(0,0, 3*X, 270, 360),
                              path.lineto(*F),
                              path.arcn(0,0,  X, 360, 270),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*O),
                              path.lineto(*F),
                              path.arc(0,0, X, 0, 90),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*O),
                              path.lineto(*E),
                              path.arc(0,0, X, 90, 180),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*O),
                              path.lineto(*H),
                              path.arc(0,0, X, 180, 270),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*O),
                              path.lineto(*G),
                              path.arc(0,0, X, 270, 360),
                              path.closepath()), BASE+FILLED(GREEN)))

    drawing.append((path.path(path.arc(0,0, X, 0, 360),
                              path.closepath()), BASE))

    drawing.append((path.path(path.arc(0,0, 3*X, 0, 360),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura008d():
    '''Tangram Circular 2'''

    name = "figures/ffigura008d"

    X = 1.5  # scale !
    Y = X*R3

    O = (   0,   0)
    A = (   0, 2*X)
    B = ( 2*X,   0)
    C = (   0,-2*X)
    D = (-2*X,   0)
    
    E = (   0,   X)
    F = (   0,  -X)
    G = (  -Y,   X)
    H = (   Y,   X)
    
    drawing = []
    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+FILLED(PINK)))
    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*E),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*F),
                              path.lineto(*B),
                              path.closepath()), BASE+FILLED(BROWN)))
    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*F),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*F),
                              path.lineto(*D),
                              path.arc(0,0, 2*X, 180, 270),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*F),
                              path.lineto(*C),
                              path.arc(0,0, 2*X, 270, 360),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.arc(0,0, 2*X, 0, 30),
                              path.closepath()), BASE+FILLED(DGREEN)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*G),
                              path.arc(0,0, 2*X, 150, 180),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*H),
                              path.arc(0,0, 2*X, 30, 90),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*E),
                              path.lineto(*A),
                              path.arc(0,0, 2*X, 90, 150),
                              path.closepath()), BASE+FILLED(DBLUE)))
    drawing.append((path.path(path.arc(0,0, 2*X, 0, 360),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura009a():
    '''Tangram de Brügner'''

    name = "figures/ffigura009a"

    PHI = (1.0+R5)/2.0
    X = 3.0 # scale!
    Y = X*sqrt(PHI)


    A = (0,0)
    B = (0,Y)
    C = (X,Y)
    D = (X,0)
    E = w_point(C, A, 1,PHI-1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*A),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura009b():
    '''Ostomachion'''

    name = "figures/ffigura009b"

    X = 4.0 # scale !


    A = (0.0,0.0)
    B = (  X,0.0)
    C = (  X,  X)
    D = (0.0,  X)
    E = w_point(A,B, 1,1)
    F = w_point(D,C, 1,1)
    G = w_point(A,F, 1,1)
    H = w_point(B,F, 1,1)
    I = w_point(B,C, 1,1)
    J = w_point(A,E, 1,1)
    K = w_point(A,F, 1,2)
    L = w_point(K,D, 1,1)
    M = w_point(A,F, 2,1)
    N = w_point(B,D, 2,1)
    O = w_point(B,D, 1,1)
    P = w_point(B,C, 1,2)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*J),
                              path.lineto(*M),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*M),
                              path.lineto(*G),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*E),
                              path.lineto(*O),
                              path.lineto(*K),
                              path.lineto(*G),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*O),
                              path.lineto(*N),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*N),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*N),
                              path.lineto(*H),
                              path.closepath()), BASE+FILLED(PINK)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*B),
                              path.lineto(*I),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*P),
                              path.lineto(*I),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*P),
                              path.lineto(*C),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*F),
                              path.lineto(*O),
                              path.lineto(*N),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*K),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*K),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*L),
                              path.lineto(*A),
                              path.closepath()), BASE+FILLED(PINK)))
    drawing.append((path.path(path.moveto(*L),
                              path.lineto(*K),
                              path.lineto(*A),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura010a():
    '''Subtangram Xinés'''

    name = "figures/ffigura010a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(C, D, 1,1)
    H = w_point(A, C, 1,1)

    drawing = []
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*G),
                              path.lineto(*D),
                              path.lineto(*H),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*H),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*D),
                              path.lineto(*H),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*F),
                              path.lineto(*H),
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
    

def ffigura010b():
    '''Tangram de la Creu'''

    name = "figures/ffigura010b"

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
    

def ffigura010c():
    '''Tangram dels Cinc Triangles'''

    name = "figures/ffigura010c"

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
    

def ffigura011a():
    '''Pentominos'''

    name = "figures/ffigura011a"

    X = 0.5
    A = (0,0)
    B = (0,10*X)
    C = (6*X,10*X)
    D = (6*X,0)

    drawing = []
    drawing.append((path.path(path.moveto(0*X,0*X),
                              path.lineto(1*X,0*X),
                              path.lineto(1*X,1*X),
                              path.lineto(2*X,1*X),
                              path.lineto(2*X,2*X),
                              path.lineto(3*X,2*X),
                              path.lineto(3*X,3*X),
                              path.lineto(1*X,3*X),
                              path.lineto(1*X,2*X),
                              path.lineto(0*X,2*X),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(1*X,0*X),
                              path.lineto(5*X,0*X),
                              path.lineto(5*X,2*X),
                              path.lineto(4*X,2*X),
                              path.lineto(4*X,1*X),
                              path.lineto(1*X,1*X),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(5*X,0*X),
                              path.lineto(6*X,0*X),
                              path.lineto(6*X,4*X),
                              path.lineto(5*X,4*X),
                              path.lineto(5*X,3*X),
                              path.lineto(4*X,3*X),
                              path.lineto(4*X,2*X),
                              path.lineto(5*X,2*X),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(2*X,1*X),
                              path.lineto(4*X,1*X),
                              path.lineto(4*X,3*X),
                              path.lineto(5*X,3*X),
                              path.lineto(5*X,4*X),
                              path.lineto(3*X,4*X),
                              path.lineto(3*X,2*X),
                              path.lineto(2*X,2*X),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(0*X,2*X),
                              path.lineto(1*X,2*X),
                              path.lineto(1*X,3*X),
                              path.lineto(3*X,3*X),
                              path.lineto(3*X,4*X),
                              path.lineto(1*X,4*X),
                              path.lineto(1*X,5*X),
                              path.lineto(0*X,5*X),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(1*X,4*X),
                              path.lineto(6*X,4*X),
                              path.lineto(6*X,5*X),
                              path.lineto(1*X,5*X),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(0*X,5*X),
                              path.lineto(3*X,5*X),
                              path.lineto(3*X,6*X),
                              path.lineto(2*X,6*X),
                              path.lineto(2*X,7*X),
                              path.lineto(0*X,7*X),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(3*X,5*X),
                              path.lineto(6*X,5*X),
                              path.lineto(6*X,6*X),
                              path.lineto(4*X,6*X),
                              path.lineto(4*X,7*X),
                              path.lineto(2*X,7*X),
                              path.lineto(2*X,6*X),
                              path.lineto(3*X,6*X),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(4*X,6*X),
                              path.lineto(6*X,6*X),
                              path.lineto(6*X,7*X),
                              path.lineto(5*X,7*X),
                              path.lineto(5*X,9*X),
                              path.lineto(4*X,9*X),
                              path.lineto(4*X,8*X),
                              path.lineto(3*X,8*X),
                              path.lineto(3*X,7*X),
                              path.lineto(4*X,7*X),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(0*X,7*X),
                              path.lineto(2*X,7*X),
                              path.lineto(2*X,8*X),
                              path.lineto(1*X,8*X),
                              path.lineto(1*X,9*X),
                              path.lineto(2*X,9*X),
                              path.lineto(2*X,10*X),
                              path.lineto(0*X,10*X),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(2*X,7*X),
                              path.lineto(3*X,7*X),
                              path.lineto(3*X,8*X),
                              path.lineto(4*X,8*X),
                              path.lineto(4*X,9*X),
                              path.lineto(3*X,9*X),
                              path.lineto(3*X,10*X),
                              path.lineto(2*X,10*X),
                              path.lineto(2*X,9*X),
                              path.lineto(1*X,9*X),
                              path.lineto(1*X,8*X),
                              path.lineto(2*X,8*X),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(3*X,9*X),
                              path.lineto(5*X,9*X),
                              path.lineto(5*X,7*X),
                              path.lineto(6*X,7*X),
                              path.lineto(6*X,10*X),
                              path.lineto(3*X,10*X),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s+[trafo.rotate(270)])
    mycanvas.writePDFfile(name)
    

def ffigura011b():
    '''Hexamants'''

    name = "figures/ffigura011b"

    X = 0.6 # Scale !
    Y = X*R3/2.0
    A = (0*X,0*Y)
    B = (3*X,6*Y)
    C = (9*X,6*Y)
    D = (6*X,0*Y)

    drawing = []
    drawing.append((path.path(path.moveto(0.0*X,0*Y),
                              path.lineto(2.0*X,0*Y),
                              path.lineto(1.5*X,1*Y),
                              path.lineto(2.5*X,1*Y),
                              path.lineto(2.0*X,2*Y),
                              path.lineto(1.0*X,2*Y),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(2.0*X,0*Y),
                              path.lineto(4.0*X,0*Y),
                              path.lineto(4.5*X,1*Y),
                              path.lineto(3.5*X,1*Y),
                              path.lineto(3.0*X,2*Y),
                              path.lineto(2.5*X,1*Y),
                              path.lineto(1.5*X,1*Y),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(4.0*X,0*Y),
                              path.lineto(6.0*X,0*Y),
                              path.lineto(7.0*X,2*Y),
                              path.lineto(6.0*X,2*Y),
                              path.lineto(5.5*X,1*Y),
                              path.lineto(4.5*X,1*Y),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(1.0*X,2*Y),
                              path.lineto(2.0*X,2*Y),
                              path.lineto(2.5*X,1*Y),
                              path.lineto(3.5*X,3*Y),
                              path.lineto(2.5*X,3*Y),
                              path.lineto(2.0*X,4*Y),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(3.5*X,1*Y),
                              path.lineto(4.5*X,1*Y),
                              path.lineto(5.0*X,2*Y),
                              path.lineto(4.5*X,3*Y),
                              path.lineto(3.5*X,3*Y),
                              path.lineto(3.0*X,2*Y),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(4.5*X,1*Y),
                              path.lineto(5.5*X,1*Y),
                              path.lineto(6.0*X,2*Y),
                              path.lineto(5.5*X,3*Y),
                              path.lineto(6.0*X,4*Y),
                              path.lineto(5.0*X,4*Y),
                              path.lineto(4.5*X,3*Y),
                              path.lineto(5.0*X,2*Y),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(6.0*X,2*Y),
                              path.lineto(7.0*X,2*Y),
                              path.lineto(7.5*X,3*Y),
                              path.lineto(6.5*X,3*Y),
                              path.lineto(7.0*X,4*Y),
                              path.lineto(6.5*X,5*Y),
                              path.lineto(5.5*X,3*Y),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(2.5*X,3*Y),
                              path.lineto(3.5*X,5*Y),
                              path.lineto(4.5*X,5*Y),
                              path.lineto(4.0*X,6*Y),
                              path.lineto(3.0*X,6*Y),
                              path.lineto(2.0*X,4*Y),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(2.5*X,3*Y),
                              path.lineto(4.5*X,3*Y),
                              path.lineto(5.0*X,4*Y),
                              path.lineto(4.0*X,4*Y),
                              path.lineto(4.5*X,5*Y),
                              path.lineto(3.5*X,5*Y),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(6.5*X,3*Y),
                              path.lineto(7.5*X,3*Y),
                              path.lineto(9.0*X,6*Y),
                              path.lineto(8.0*X,6*Y),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(4.0*X,4*Y),
                              path.lineto(6.0*X,4*Y),
                              path.lineto(6.5*X,5*Y),
                              path.lineto(5.5*X,5*Y),
                              path.lineto(5.0*X,6*Y),
                              path.lineto(4.0*X,6*Y),
                              path.lineto(4.5*X,5*Y),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(7.0*X,4*Y),
                              path.lineto(8.0*X,6*Y),
                              path.lineto(5.0*X,6*Y),
                              path.lineto(5.5*X,5*Y),
                              path.lineto(6.5*X,5*Y),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura012a():
    '''Subtangram Xinés - Costats inconmensurables'''

    name = "figures/ffigura012a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(C, D, 1,1)
    H = w_point(A, C, 1,1)


    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*H),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*G)), BASE+THICK+COLOR(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*H),
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura012b():
    '''Tangram de la Creu - Costats inconmensurables'''

    name = "figures/ffigura012b"

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
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.moveto(*H),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.moveto(*B),
                              path.lineto(*G)), BASE+THICK+COLOR(color.rgb.blue)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura012c():
    '''Tangram dels cinc triangles - Costats inconmensurables'''

    name = "figures/ffigura012c"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(B, C, 1,1)
    F = w_point(A, C, 1,1)

    drawing = []
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*E)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*D)), BASE+THICK+COLOR(color.rgb.blue)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*D)), BASE+THICK+COLOR(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura012d():
    '''Tangram dels 4 triangles - Costats inconmensurables'''

    name = "figures/ffigura012d"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(C, D, 1,1)
    H = w_point(A, C, 1,1)


    drawing = []
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*B),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK+COLOR(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura012e():
    '''Tangram Median - Costats inconmensurables'''

    name = "figures/ffigura012e"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(B, C, 1,1)
    
    drawing = []
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.moveto(*E),
                              path.lineto(*C)), BASE+THICK+COLOR(color.rgb.blue)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura013():
    '''Tangram Xinés - Retícules'''

    name = "figures/ffigura013"

    X = 3*R2
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
                              path.lineto(*C),
                              path.moveto(*B),
                              path.lineto(*D)), BASE+THICK+COLOR(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+THICK+COLOR(RED)))
    drawing.append((path.path(path.moveto(*w_point(A,E, 1,1)),
                              path.lineto(*w_point(A,E, 1,1)),
                              path.moveto(*w_point(A,E, 1,1)),
                              path.lineto(*w_point(A,E, 1,1))), BASE+THICK))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*H),
                              path.moveto(*E),
                              path.lineto(*G),
                              path.moveto(*w_point(A,E, 1,1)),
                              path.lineto(*w_point(D,G, 1,1)),
                              path.moveto(*w_point(E,B, 1,1)),
                              path.lineto(*w_point(G,C, 1,1)),
                              path.moveto(*w_point(A,H, 1,1)),
                              path.lineto(*w_point(B,F, 1,1)),
                              path.moveto(*w_point(D,H, 1,1)),
                              path.lineto(*w_point(C,F, 1,1))), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura013a():
    '''Subtangram Xinés - Retícules'''

    name = "figures/ffigura013a"

    X = 3*R2
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
                              path.lineto(*C),
                              path.moveto(*B),
                              path.lineto(*D)), BASE+THICK+COLOR(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+THICK+COLOR(RED)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*H),
                              path.moveto(*E),
                              path.lineto(*G)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura013b():
    '''Tangram de la Creu - Retícula'''

    name = "figures/ffigura013b"

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
    

def ffigura013c():
    '''Tangram dels cinc triangles - Retícula'''

    name = "figures/ffigura013c"

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

    
def ffigura013d():
    '''Tangram dels 4 triangles - Retícules'''

    name = "figures/ffigura013d"

    X = 3*R2
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
                              path.lineto(*C),
                              path.moveto(*B),
                              path.lineto(*D)), BASE+THICK+COLOR(RED)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*H),
                              path.moveto(*E),
                              path.lineto(*G)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura013e():
    '''Tangram median - Retícula'''

    name = "figures/ffigura013e"

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
    

def ffigura014():
    '''Quadrat amb un Tall'''

    name = "figures/ffigura014"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)

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
    

def ffigura015a():
    '''Tangram de dues peces - Quadrat'''

    name = "figures/ffigura015a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura015b():
    '''Tangram de dues peces - Trapezi'''

    name = "figures/ffigura015b"

    X = 2*R5
    A = (0,0)
    B = (0.5*X,X)
    C = (X,X)
    D = (1.5*X,0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura015c():
    '''Tangram de dues peces - Paralelogram'''

    name = "figures/ffigura015c"

    X = 2*R5
    A = (0,0)
    B = (0.5*X,X)
    C = (1.5*X,X)
    D = (X,0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura015d():
    '''Tangram de dues peces - Triangle'''

    name = "figures/ffigura015d"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (2*X,0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura015e():
    '''Tangram de dues peces - Quadrilater'''

    name = "figures/ffigura015e"

    X = 2*R5
    A = (0,0)
    B = (0.5*X,X)
    C = (1.5*X,0.5*X)
    D = (1.5*X,0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura016a():
    '''Quadrat amb dos Talls 1'''

    name = "figures/ffigura016a"

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
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*E),
                              path.lineto(*B)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura016b():
    '''Quadrat amb dos Talls 2'''

    name = "figures/ffigura016b"

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
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura016c():
    '''Quadrat amb dos Talls 3'''

    name = "figures/ffigura016c"

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
                              path.lineto(*A)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura016d():
    '''Quadrat amb dos Talls 1 - retícula'''

    name = "figures/ffigura016d"

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
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura016e():
    '''Quadrat amb dos Talls 2 - retícula'''

    name = "figures/ffigura016e"

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
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura016f():
    '''Quadrat amb dos Talls 3 - retícula'''

    name = "figures/ffigura016f"

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
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*C),
                              path.moveto(*B),
                              path.lineto(*D)), BASE+THICK+COLOR(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura016g():
    '''Quadrat amb dos Talls 2 - retícula sense color'''

    name = "figures/ffigura016g"

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
                              path.lineto(*D)), BASE+THICK))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*B),
                              path.moveto(*D),
                              path.lineto(*G),
                              path.moveto(*A),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*C)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura017():
    '''El Tangram Egípci'''

    name = "figures/ffigura017"

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
    

def ffigura017b():
    '''El Tangram Egípci'''

    name = "figures/ffigura017b"

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
    

def ffigura018a():
    '''El Tangram Egípci - Decomposat'''

    name = "figures/ffigura018a"

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
    

def ffigura018b():
    '''Tangram de la Creu - Decomposat'''

    name = "figures/ffigura018b"

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
    

def ffigura019():
    '''El Tangram Egípci - 5 cercles notables'''

    name = "figures/ffigura019"

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
    

def ffigura019b():
    '''El Tangram Egípci - El quadrilater es ciclic'''

    name = "figures/ffigura019b"

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
    drawing.append((path.circle(C2[0], C2[1], X/(2*R2)), BASE+THICK+COLOR(ORANGE)))
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
    

def ffigura020a():
    '''T1+Q4'''

    name = "figures/ffigura020a"

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
    

def ffigura020b():
    '''T5'''

    name = "figures/ffigura020b"

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
    

def ffigura020c():
    '''T1+T4'''

    name = "figures/ffigura020c"

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
    

def ffigura020d():
    '''T1+Q4+T5'''

    name = "figures/ffigura020d"

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
    

def ffigura020e():
    '''T4+T6'''

    name = "figures/ffigura020e"

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
    

def ffigura020f():
    '''T1+Q4+T5'''

    name = "figures/ffigura020f"

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
    

def ffigura020g():
    '''T4+T6'''

    name = "figures/ffigura020g"

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
    

def ffigura020h():
    '''T6+Q4'''

    name = "figures/ffigura020h"

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
    

def ffigura020i():
    '''T6+Q4'''

    name = "figures/ffigura020i"

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
    

def ffigura020j():
    '''T1+T4+T5+Q4'''

    name = "figures/ffigura020j"

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
    

def ffigura020k():
    '''T1+T4+T5+Q4'''

    name = "figures/ffigura020k"

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
    

def ffigura020l():
    '''T1+T4+T5+Q4'''

    name = "figures/ffigura020l"

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
    

def ffigura020m():
    '''T1+T4+T5+Q4'''

    name = "figures/ffigura020m"

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
    

def ffigura021a():
    '''El Tangram Egípci - Quadrat 1'''

    name = "figures/ffigura021a"

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
    

def ffigura021b():
    '''El Tangram Egípci - Quadrat 2'''

    name = "figures/ffigura021b"

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
    

def ffigura021c():
    '''El Tangram Egípci - Quadrat 3'''

    name = "figures/ffigura021c"

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
    

def ffigura022a():
    '''El Tangram Egípci - Figura 1'''

    name = "figures/ffigura022a"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022b():
    '''El Tangram Egípci - Figura 2'''

    name = "figures/ffigura022b"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022c():
    '''El Tangram Egípci - Figura 3'''

    name = "figures/ffigura022c"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022d():
    '''El Tangram Egípci - Figura 4'''

    name = "figures/ffigura022d"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022e():
    '''El Tangram Egípci - Figura 5'''

    name = "figures/ffigura022e"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022f():
    '''El Tangram Egípci - Figura 6'''

    name = "figures/ffigura022f"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022g():
    '''El Tangram Egípci - Figura 7'''

    name = "figures/ffigura022g"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022h():
    '''El Tangram Egípci - Figura 8'''

    name = "figures/ffigura022h"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022i():
    '''El Tangram Egípci - Figura 9'''

    name = "figures/ffigura022i"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022j():
    '''El Tangram Egípci - Figura 10'''

    name = "figures/ffigura022j"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022k():
    '''El Tangram Egípci - Figura 11'''

    name = "figures/ffigura022k"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022l():
    '''El Tangram Egípci - Figura 12'''

    name = "figures/ffigura022l"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022m():
    '''El Tangram Egípci - Figura 13'''

    name = "figures/ffigura022m"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022n():
    '''El Tangram Egípci - Figura 14'''

    name = "figures/ffigura022n"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022o():
    '''El Tangram Egípci - Figura 15'''

    name = "figures/ffigura022o"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022p():
    '''El Tangram Egípci - Figura 16'''

    name = "figures/ffigura022p"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022q():
    '''El Tangram Egípci - Figura 17'''

    name = "figures/ffigura022q"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022r():
    '''El Tangram Egípci - Figura 18'''

    name = "figures/ffigura022r"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022s():
    '''El Tangram Egípci - Figura 19'''

    name = "figures/ffigura022s"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022t():
    '''El Tangram Egípci - Figura 20'''

    name = "figures/ffigura022t"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022u():
    '''El Tangram Egípci - Figura 21'''

    name = "figures/ffigura022u"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022v():
    '''El Tangram Egípci - Figura 22'''

    name = "figures/ffigura022v"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022w():
    '''El Tangram Egípci - Figura 23'''

    name = "figures/ffigura022w"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura022x():
    '''El Tangram Egípci - Figura 24'''

    name = "figures/ffigura022x"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura023a():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/ffigura023a"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura023b():
    '''El Subtangram Egípci - Figura 2'''

    name = "figures/ffigura023b"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura023c():
    '''El Subtangram Egípci - Figura 3'''

    name = "figures/ffigura023c"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (8*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura023d():
    '''El Subtangram Egípci - Figura 4'''

    name = "figures/ffigura023d"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura023e():
    '''El Subtangram Egípci - Figura 5'''

    name = "figures/ffigura023e"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura023f():
    '''El Subtangram Egípci - Figura 6'''

    name = "figures/ffigura023f"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura023g():
    '''El Subtangram Egípci - Figura 7'''

    name = "figures/ffigura023g"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura023h():
    '''El Subtangram Egípci - Figura 8'''

    name = "figures/ffigura023h"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura023i():
    '''El Subtangram Egípci - Figura 9'''

    name = "figures/ffigura023i"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura024a():
    '''El Tangram Egípci - Triangle 1:2'''

    name = "figures/ffigura024a"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,2*X)
    C = (1*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura024b():
    '''El Tangram Egípci - Triangle 2:4'''

    name = "figures/ffigura024b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (2*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura024c():
    '''El Tangram Egípci - Triangle sqrt(5):2*sqrt(5)'''

    name = "figures/ffigura024c"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (1*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura024d():
    '''El Tangram Egípci - Triangle 3:6'''

    name = "figures/ffigura024d"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,6*X)
    C = (3*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura024e():
    '''El Tangram Egípci - Triangle 4:8'''

    name = "figures/ffigura024e"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,8*X)
    C = (4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura024f():
    '''El Tangram Egípci - Triangle 2*sqrt(5):4*sqrt(5)'''

    name = "figures/ffigura024f"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,4*X*R5)
    C = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura025a():
    '''El Tangram Egípci - Suma de figures semblants 1'''

    name = "figures/ffigura025a"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura025b():
    '''El Tangram Egípci - Suma de figures semblants 2'''

    name = "figures/ffigura025b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (8*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura025c():
    '''El Tangram Egípci - Suma de figures semblants 3'''

    name = "figures/ffigura025c"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,2*X)
    C = (4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura025d():
    '''El Tangram Egípci - Suma de figures semblants 4'''

    name = "figures/ffigura025d"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura025e():
    '''El Tangram Egípci - Suma de figures semblants 5'''

    name = "figures/ffigura025e"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura025f():
    '''El Tangram Egípci - Suma de figures semblants 6'''

    name = "figures/ffigura025f"

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
                              path.closepath()), BASE+FILLED(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura026a():
    '''Tangram del triangle'''

    name = "figures/ffigura026a"

    Y = 2.0 # scale !
    X = Y*R3
    A = (0,0)
    B = (Y,0)
    C = (Y,-X)
    D = (0,-X)
    E = w_point(A, D, 1,1)
    F = w_point(A, C, 1,1)
    G = w_point(F, C, 1,1)

    drawing = []
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*A),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*G),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*G),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura026b():
    '''Tangram de l'Hexàgon'''

    name = "figures/ffigura026b"

    Y = 2.0 # scale !
    X = Y*R3
    A = (0,0)
    B = (0,-X)
    C = (1.5*Y,-X)
    D = (1.5*Y,0)
    E = w_point(B, C, 1,2)
    F = w_point(A, D, 1,2)
    G = w_point(E, F, 1,1)
    H = w_point(B, F, 1,1)

    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*G),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.lineto(*G),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura028a():
    '''El Puzzle Egipci'''

    name = "figures/ffigura028a"

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
    

def ffigura028b():
    '''Tangents'''

    name = "figures/ffigura028b"

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
    Q = w_point(E, B, 2,1)
    drawing = []


    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*N),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(DGREEN)))
    drawing.append((path.path(path.moveto(*Q),
                              path.lineto(*N),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(PINK)))
    drawing.append((path.path(path.moveto(*Q),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*Q),
                              path.lineto(*N),
                              path.lineto(*C),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*Q),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*N),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*F),
                              path.lineto(*D),
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
    

def ffigura029a():
    '''Quadrilaters del Tangram Egípci - Figura 1'''

    name = "figures/ffigura029a"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura029b():
    '''Quadrilaters del Tangram Egípci - Figura 2'''

    name = "figures/ffigura029b"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura029c():
    '''Quadrilaters del Tangram Egípci - Figura 3'''

    name = "figures/ffigura029c"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura029d():
    '''Quadrilaters del Tangram Egípci - Figura 4'''

    name = "figures/ffigura029d"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura029e():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/ffigura029e"

    X = 1 # Scale #
    A = (  0,  0)
    B = (0.89*X,4.92*X)
    C = (2*X*R5, 1*X*R5)
    D = (4*X*R5, 0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(BLACK)))
    #drawing.append((path.path(path.moveto(*A),
    #                          path.lineto(*C)), BASE+DASHED+THICK+COLOR(WHITE)))
    #drawing.append((path.path(path.moveto(*B),
    #                          path.lineto(*D)), BASE+DASHED+THICK+COLOR(BLACK)))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura029f():
    '''Quadrilaters del Tangram Egípci - Figura 6'''

    name = "figures/ffigura029f"

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
                              path.closepath()), BASE+FILLED(BLACK)))
    #drawing.append((path.path(path.moveto(*A),
    #                          path.lineto(*C)), BASE+DASHED+THICK+COLOR(WHITE)))
    #drawing.append((path.path(path.moveto(*B),
    #                          path.lineto(*D)), BASE+DASHED+THICK+COLOR(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura029g():
    '''Quadrilaters del Tangram Egípci - Figura 7'''

    name = "figures/ffigura029g"

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
                              path.closepath()), BASE+FILLED(BLACK)))
    drawing.append((path.circle(4*X, 2*X, 2*X), BASE+DASHED+THICK+COLOR(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura029h():
    '''Quadrilaters del Tangram Egípci - Figura 8'''

    name = "figures/ffigura029h"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura029i():
    '''Quadrilaters del Tangram Egípci - Figura 9'''

    name = "figures/ffigura029i"

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
                              path.closepath()), BASE+FILLED(BLACK)))
    #drawing.append((path.circle(1.5*X*R5, 0.5*X*R5, X*5/R2), BASE+DASHED+THICK+COLOR(RED)))
    drawing.append((path.path(path.moveto(*D),
                              path.arc(E[0],E[1], X*5/R2, -18.43, 198.43)), BASE+DASHED+THICK+COLOR(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura029j():
    '''Quadrilaters del Tangram Egípci - Figura 10'''

    name = "figures/ffigura029j"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura029k():
    '''Quadrilaters del Tangram Egípci - Figura 11'''

    name = "figures/ffigura029k"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura029l():
    '''Quadrilaters del Tangram Egípci - Figura 12'''

    name = "figures/ffigura029l"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (4*X,3*X)
    D = (10*X, 0)
    
    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(BLACK)))
    #drawing.append((path.path(path.moveto(*A),
    #                          path.lineto(*C)), BASE+DASHED+THICK+COLOR(WHITE)))
    #drawing.append((path.path(path.moveto(*B),
    #                          path.lineto(*D)), BASE+DASHED+THICK+COLOR(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura029m():
    '''Quadrilaters del Tangram Egípci - Figura 13'''

    name = "figures/ffigura029m"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura029n():
    '''Quadrilaters del Tangram Egípci - Figura 14'''

    name = "figures/ffigura029n"

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
                              path.closepath()), BASE+FILLED(BLACK)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*C),
                              path.moveto(*B),
                              path.lineto(*D)), BASE+DASHED+THICK+COLOR(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura029o():
    '''Quadrilaters del Tangram Egípci - Figura 15'''

    name = "figures/ffigura029o"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,5*X)
    C = (4*X,3*X)
    D = s_point(A, C, 2*R5/5.0)
    E = s_point(B, C, 5/(2*R5))

    drawing = []
    #drawing.append((path.path(path.moveto(*A),
    #                          path.lineto(*E),
    #                          path.moveto(*B),
    #                          path.lineto(*D)), BASE+DASHED+THICK+COLOR(BLACK)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s+[trafo.rotate(-(90-3*BETA)/2.0)])
    
    mycanvas.writePDFfile(name)
    

def ffigura029p():
    '''Quadrilaters del Tangram Egípci - Figura 16'''

    name = "figures/ffigura029p"

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
                              path.closepath()), BASE+FILLED(BLACK)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*C)), BASE+DASHED+THICK+COLOR(BLACK)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*D)), BASE+DASHED+THICK+COLOR(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura029q():
    '''Quadrilaters del Tangram Egípci - Figura 17'''

    name = "figures/ffigura029q"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,5*X)
    C = (4*X,3*X)
    D = (8*X,6*X)
    E = (8*X,1*X)

    drawing = []
    #drawing.append((path.path(path.moveto(*A),
    #                          path.lineto(*E),
    #                          path.moveto(*B),
    #                          path.lineto(*D)), BASE+DASHED+THICK+COLOR(BLACK)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura029r():
    '''Quadrilaters del Tangram Egípci - Figura 18'''

    name = "figures/ffigura029r"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,1*X*R5)
    D = (4*X*R5,2*X*R5)
    E = (4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*D)), BASE+DASHED+THICK+COLOR(BLACK)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura030a():
    '''DIDI puzzle'''

    name = "figures/ffigura030a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = (X-X/R2, X/R2)

    drawing = []
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*D),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura030b():
    '''Tangram dels 4 triangles iguals'''

    name = "figures/ffigura030b"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = (X/2.0,X/2.0)

    drawing = []
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*D),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    

def ffigura030c():
    '''Tangram dels 4 triangles differents'''

    name = "figures/ffigura030c"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = (X/2.0, X/2.0)
    F = (0, X/2.0)

    drawing = []
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def ffigura030d():
    '''Tangram de Median'''

    name = "figures/ffigura030d"

    X = 2*R5
    A = (0,0)
    B = (X,0)
    C = (X,X)
    D = (0,X)
    E = (X/2.0, 0)
    F = (X/2.0, X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*D),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)    


def ffigura031():
    '''T-puzzle'''

    name = "figures/ffigura031"

    X = 2.0
    A = (0*X, 0*X)
    B = (0*X, 2*X)
    C = (3*X, 2*X)
    D = (3*X, 0*X)
    E = (0*X, 1*X)
    F = (R2*X,2*X)
    G = (3*X, 1*X)
    H = (2*X, 0*X)
    I = (1*X, 1*X)
    J = (2*X, 1*X)
    K = ((1+R2)*X, 1*X)

    drawing = []
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*H),
                              path.lineto(*A),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*C),
                              path.lineto(*G),
                              path.lineto(*K),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*F),
                              path.lineto(*K),
                              path.lineto(*J),
                              path.lineto(*H),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*J),
                              path.lineto(*G),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


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


def figure001aa():
    '''The Egyptian Tangram'''

    name = "figures/figure001aa"

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

    mycanvas.draw(*put_text(0.08*X, 0.62*X, r"\textbf{{T1}}"))
    mycanvas.draw(*put_text(0.82*X, 0.17*X, r"\large\textbf{{T5}}"))
    mycanvas.draw(*put_text(0.30*X, 0.80*X, r"\large\textbf{{T4}}"))
    mycanvas.draw(*put_text(0.50*X, 0.45*X, r"\Large\textbf{{T6}}"))
    mycanvas.draw(*put_text(0.17*X, 0.17*X, r"\large\textbf{{Q4}}"))

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


def figure004n():
    '''T1+T4+T5 - Figura n'''

    name = "figures/figure004n"

    X = 1.0*R5 # Scale #
    A = ( 0*X,-1*X)
    B = (-2*X, 0*X)
    C = ( 2*X, 0*X)
    D = ( 0*X, 1*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004o():
    '''T1+T4+T5 - Figura o'''

    name = "figures/figure004o"

    X = 1.0*R5 # Scale #
    A = ( 0*X,-1*X)
    B = (-2*X,-1*X)
    C = ( 2*X, 1*X)
    D = ( 0*X, 1*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004p():
    '''T1+T4+T5 - Figura p'''

    name = "figures/figure004p"

    X = 1.0*R5 # Scale #
    A = ( 2*X,-1*X)
    B = ( 2*X, 0*X)
    C = (-2*X, 0*X)
    D = (-2*X, 1*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004q():
    '''T1+T4+T5 - Figura q'''

    name = "figures/figure004q"

    X = 1.0*R5 # Scale #
    A = ( 0*X,-1*X)
    B = (-2*X, 0*X)
    C = ( 1*X, 0*X)
    D = ( 0*X, 2*X)

    A = r_point(A, (0,0), -atan2(1,1))
    B = r_point(B, (0,0), -atan2(1,1))
    C = r_point(C, (0,0), -atan2(1,1))
    D = r_point(D, (0,0), -atan2(1,1))

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
 

def figure004r():
    '''T1+T4+T5 - Figura r'''

    name = "figures/figure004r"

    X = 1.0 # Scale #
    A = (-1*R5*X, 2*R5*X)
    B = (-1*R5*X, 0*R5*X)
    C = (    5*X,    0*X)
    D = (    1*X,   -2*X)

    alpha = atan2(2,1)/2.0
    A = r_point(A, (0,0), alpha)
    B = r_point(B, (0,0), alpha)
    C = r_point(C, (0,0), alpha)
    D = r_point(D, (0,0), alpha)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
 

def figure004s():
    '''T1+T4+T5 - Figura s'''

    name = "figures/figure004s"

    X = 1.0 # Scale #
    A = (-2*X*R5, 1*X*R5)
    B = (-2*X*R5, 0*X*R5)
    C = ( 5*X,    0*X)
    D = ( 4*X,   -2*X)

    alpha = atan2(1,2)/2.0
    A = r_point(A, (0,0), alpha)
    B = r_point(B, (0,0), alpha)
    C = r_point(C, (0,0), alpha)
    D = r_point(D, (0,0), alpha)


    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
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


def figure005d():
    '''T1+T4+T5 - Pythagoras'''

    name = "figures/figure005d"

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
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLUE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)

    mycanvas.draw(*put_text(0.50*X, 1.65*X, r"\small{$a^2$}"))
    mycanvas.draw(*put_text(3.10*X, 1.65*X, r"\small{$b^2$}"))
    mycanvas.draw(*put_text(1.80*X, 0.15*X, r"\small{$c^2$}"))
    mycanvas.draw(*put_text(0.70*X, 0.75*X, r"\small{$a c$}"))
    mycanvas.draw(*put_text(2.65*X, 0.75*X, r"\small{$b c$}"))
    mycanvas.draw(*put_text(0.25*X, 1.10*X, r"\small{$a b$}"))
    mycanvas.draw(*put_text(4.75*X, 1.10*X, r"\small{$a b$}"))

    mycanvas.writePDFfile(name)


def figure005e():
    '''T1+T4+T5 - T5'''

    name = "figures/figure005e"

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
                              path.closepath()), BASE+FILLED(GREEN)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)

    mycanvas.draw(*put_text(0.60*X, 0.75*X, r"\small{$a$}"))
    mycanvas.draw(*put_text(2.65*X, 0.75*X, r"\small{$b$}"))
    mycanvas.draw(*put_text(1.80*X, 0.15*X, r"\small{$c$}"))

    mycanvas.writePDFfile(name)


def figure005f():
    '''T1+T4+T5 - T1+T4'''

    name = "figures/figure005f"

    X = 1.0 # Scale #
    A = (0*X, 0*X)
    B = (5*X, 0*X)
    C = (5*X, 2*X)
    D = (0*X, 2*X)
    E = (1*X, 2*X)
    F = (1*X, 0*X)


    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*F),
                              path.lineto(*B),
                              path.closepath()), BASE+FILLED(BLUE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)

    mycanvas.draw(*put_text(0.60*X, 0.75*X, r"\small{$a$}"))
    mycanvas.draw(*put_text(2.65*X, 0.75*X, r"\small{$b$}"))
    mycanvas.draw(*put_text(0.60*X, 0.15*X, r"\small{$x$}"))
    mycanvas.draw(*put_text(2.00*X, 0.15*X, r"\small{$y$}"))
    mycanvas.draw(*put_text(1.20*X, 0.75*X, r"\small{$h$}"))

    mycanvas.writePDFfile(name)


def figure005g():
    '''T1+T4+T5 - Trapezoid'''

    name = "figures/figure005g"

    X = 1.0 # Scale #
    A = (0*X, 0*X)
    B = (4*X, 0*X)
    C = (4*X, 4*X)
    D = (0*X, 1*X)
    E = (2*X, 0*X)

    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(BLUE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)

    mycanvas.draw(*put_text(3.10*X, 0.13*X, r"\small{$\sqrt{\!ab}$}"))
    mycanvas.draw(*put_text(0.65*X, 0.13*X, r"\small{$\sqrt{\!ab}$}"))
    mycanvas.draw(*put_text(0.15*X, 0.40*X, r"\small{$a$}"))
    mycanvas.draw(*put_text(3.80*X, 1.65*X, r"\small{$b$}"))
    mycanvas.draw(*put_text(2.00*X, 2.00*X, r"\small{$a+b$}"))

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
    #drawing.append((path.path(path.moveto(*E),
    #                          path.lineto(*C),
    #                          path.lineto(*D),
    #                          path.closepath()), BASE+ULTRATHIN+[deco.filled([YELLOW, color.transparency(0.90)])]+[YELLOW, color.transparency(0.90)]))
    #drawing.append((path.path(path.moveto(*D),
    #                          path.lineto(*B),
    #                          path.lineto(*E),
    #                          path.closepath()), BASE+ULTRATHIN+[deco.filled([BLUE, color.transparency(0.90)])]+[BLUE, color.transparency(0.90)]))
    #drawing.append((path.path(path.moveto(*A),
    #                          path.lineto(*B),
    #                          path.lineto(*E),
    #                          path.closepath()), BASE+ULTRATHIN+[deco.filled([BLUE, color.transparency(0.90)])]+[BLUE, color.transparency(0.90)]))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*D)), BASE+VERYTHIN+DASHED))

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

    #drawing.append((path.path(path.moveto(*A),
    #                          path.lineto(*B),
    #                          path.lineto(*E),
    #                          path.closepath()), BASE+ULTRATHIN+[deco.filled([YELLOW, color.transparency(0.90)])]+[YELLOW, color.transparency(0.90)]))
    #drawing.append((path.path(path.moveto(*D),
    #                          path.lineto(*B),
    #                          path.lineto(*E),
    #                          path.closepath()), BASE+ULTRATHIN+[deco.filled([BLUE, color.transparency(0.90)])]+[BLUE, color.transparency(0.90)]))
    #drawing.append((path.path(path.moveto(*E),
    #                          path.lineto(*C),
    #                          path.lineto(*D),
    #                          path.closepath()), BASE+ULTRATHIN+[deco.filled([BLUE, color.transparency(0.90)])]+[BLUE, color.transparency(0.90)]))

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*D)), BASE+VERYTHIN+DASHED))

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

    #drawing.append((path.path(path.moveto(*E),
    #                          path.lineto(*B),
    #                          path.lineto(*D),
    #                          path.closepath()), BASE+ULTRATHIN+[deco.filled([YELLOW, color.transparency(0.90)])]+[YELLOW, color.transparency(0.90)]))
    #drawing.append((path.path(path.moveto(*A),
    #                          path.lineto(*B),
    #                          path.lineto(*E),
    #                          path.closepath()), BASE+ULTRATHIN+[deco.filled([BLUE, color.transparency(0.90)])]+[BLUE, color.transparency(0.90)]))
    #drawing.append((path.path(path.moveto(*E),
    #                          path.lineto(*C),
    #                          path.lineto(*D),
    #                          path.closepath()), BASE+ULTRATHIN+[deco.filled([BLUE, color.transparency(0.90)])]+[BLUE, color.transparency(0.90)]))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*D)), BASE+VERYTHIN+DASHED))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006j():
    '''3:4:5 dissection'''

    name = "figures/figure006j"

    X   = 1.0 # Scale #
    A   = (  0,   0)
    B   = (  0, 3*X)
    C   = (4*X,   0)
    D   = w_point(B,C, 2,3)
    E   = w_point(A,C, 2.5,1.5)
    F   = w_point(E,C, 2,3)
    G   = w_point(D,C, 2.5,1.5)
    H   = w_point(G,C, 2,3)
    I   = w_point(F,C, 2.5,1.5)
    J   = w_point(I,C, 2,3)
    K   = w_point(H,C, 2.5,1.5)
    L   = w_point(K,C, 2,3)
    M   = w_point(J,C, 2.5,1.5)
    N   = w_point(M,C, 2,3)
    O   = w_point(L,C, 2.5,1.5)
    P   = w_point(O,C, 2,3)
    Q   = w_point(N,C, 2.5,1.5)
    
    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*D),
                              path.moveto(*E),
                              path.lineto(*G),
                              path.lineto(*F),
                              path.moveto(*G),
                              path.lineto(*I),
                              path.lineto(*H),
                              path.moveto(*I),
                              path.lineto(*K),
                              path.lineto(*J),
                              path.moveto(*K),
                              path.lineto(*M),
                              path.lineto(*L),
                              path.moveto(*M),
                              path.lineto(*O),
                              path.lineto(*N),
                              path.moveto(*O),
                              path.lineto(*Q),
                              path.lineto(*P)), BASE+VERYTHIN+DASHED))



    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006k():
    '''1:2:sqrt(5) dissection'''

    name = "figures/figure006k"

    X   = 1.0 # Scale #
    PHI = (1.0+R5)/2.0
    A   = (             0,             0)
    B   = (             0, 1*(PHI+1.0)*X)
    C   = ( 2*(PHI+1.0)*X,             0)

    def koch(A, B, C, depth):
        if depth == 0: yield (A,B,C) 
        else:
            D = w_point(B,C, 1,1)
            E = w_point(A,C, 5,3)
            yield from koch(D,E,B,depth-1)
            yield from koch(D,E,C,depth-1)

    drawing = []
    for P,Q,R in koch(A,B,C, 8):
        drawing.append((path.path(path.moveto(*P),
                                  path.lineto(*Q),
                                  path.lineto(*R),
                                  path.closepath()), BASE+ULTRATHIN+FILLED(WHITE)))

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+ULTRATHIN+DOTTED))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006l():
    '''1:2:sqrt(5) dissection'''

    name = "figures/figure006l"

    X   = 1.0 # Scale #
    PHI = (1.0+R5)/2.0
    A   = (             0,             0)
    B   = (             0, 1*(PHI+1.0)*X)
    C   = ( 2*(PHI+1.0)*X,             0)

    def koch_2(A, B, C, depth):
        if depth == 0: yield (A,B,C) 
        else:
            D = w_point(B,C, 3,2)
            E = w_point(A,C, 3,1)
            yield from koch_2(A,E,B,depth-1)
            yield from koch_2(D,E,C,depth-1)

    drawing = []
    for P,Q,R in koch_2(A,B,C, 10):
        drawing.append((path.path(path.moveto(*P),
                                  path.lineto(*Q),
                                  path.lineto(*R),
                                  path.closepath()), BASE+ULTRATHIN+FILLED(WHITE)))

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+ULTRATHIN+DOTTED))

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
    drawing.append((path.circle(C2[0], C2[1], X/(2*R2)), BASE+COLOR(L_ORANGE)))
    drawing.append((path.circle(C1[0], C1[1], X*R5/4.0), BASE+COLOR(L_GREEN)))
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

    drawing.append((path.path(path.moveto(*B), path.arc(X/2.0,X, X/2.0, 180, 360)), BASE+COLOR(L_BLUE)))

    drawing.append((path.circle(C2[0], C2[1], X/(2*R2)), BASE+COLOR(L_ORANGE)))

    drawing.append((path.circle(C1[0], C1[1], X*R5/4.0), BASE+COLOR(L_GREEN)))

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
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))


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
    drawing.append((path.path(path.moveto(*B), path.arc(X/2.0,X, X/2.0, 180, 360)), BASE+COLOR(L_BLUE)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*J),
                              path.lineto(*A),
                              path.closepath()), BASE+ULTRATHIN+[deco.filled([YELLOW, color.transparency(0.85)])]+[YELLOW, color.transparency(0.85)]))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*J)), BASE+THIN+DASHED))
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


def figure009f():
    '''The Egyptian Tangram'''

    name = "figures/figure009f"

    X   = 2*R5
    PHI = X*(1.0+R5)/2.0
    PHI_2 = 4/(1.0+R5)/(1.0+R5)

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
    P = (O[0], O[1]*PHI_2)
    Q = (P[0], P[1]*PHI_2)
    R = X-O[1]
    drawing = []

    drawing.append((path.circle(O[0], O[1], R), BASE+COLOR(L_GREEN)))
    drawing.append((path.circle(P[0], P[1], R*PHI_2), BASE+COLOR(L_GREEN)))
    drawing.append((path.circle(Q[0], Q[1], R*PHI_2*PHI_2), BASE+COLOR(L_GREEN)))
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

    drawing.append((path.path(path.moveto(*B), path.arc(X/2.0,X, X/2.0, 180, 360)), BASE+COLOR(L_BLUE)))

    drawing.append((path.circle(C2[0], C2[1], X/(2*R2)), BASE+COLOR(L_ORANGE)))

    drawing.append((path.circle(X/2.0, X/2.0, X/(2.0*R5)), BASE+COLOR(L_YELLOW)))

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

    drawing.append((path.circle(X/2.0, X/2.0, X/(2*R5)), BASE+COLOR(L_YELLOW)))
    drawing.append((path.circle(O[0], O[1], X/(2*R5*PHI*PHI)), BASE+COLOR(RED)))
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
    drawing.append((path.circle(X/2.0, X/2.0, X/(2*R5)), BASE+COLOR(L_YELLOW)))
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


def figure009j():
    '''The Egyptian Tangram'''

    name = "figures/figure009j"

    X   = 2*R5
    PHI = X*(1.0+R5)/2.0
    RHO = 2/(1+R5)

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
    R = (X-O[1])*RHO
    S = R*RHO
    drawing = []

    drawing.append((path.circle(X/2.0, X/2.0, X/2.0), BASE+COLOR(L_GREEN)))
    drawing.append((path.circle(O[0], O[1], X-O[1]), BASE+COLOR(L_GREEN)))
    drawing.append((path.circle(R, R, R), BASE+COLOR(L_GREEN)))
    drawing.append((path.circle(X-S, R+R+S, S), BASE+COLOR(L_GREEN)))
    drawing.append((path.path(path.moveto(0,R+R),
                              path.lineto(X,R+R)), BASE+THIN+DASHED))
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


def figure010n():
    '''T1+T4+T5'''

    name = "figures/figure010n"

    X = 2*R5
    A = (0,0)
    B = (X,0)
    C = (X/2.0,X)
    D = w_point(A, B, 1,1)
    E = w_point(B, C, 4,1)

    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*B),
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


def figure010o():
    '''T1+T4+T5'''

    name = "figures/figure010o"

    X = 2*R5
    A = (X,0)
    B = (0,0)
    C = (X/2.0,X)
    D = w_point(A, B, 1,1)
    E = w_point(B, C, 4,1)

    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*B),
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


def figure012aa():
    '''El Tangram Egípci - Figura 23'''

    name = "figures/figure012aa"

    X = 1 # Scale #
    A = ( 0*X,5*X)
    B = ( 1*X,5*X)
    C = (11*X,0*X)
    D = ( 5*X,0*X)
    E = ( 1*X,3*X)

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


def figure012ab():
    '''El Tangram Egípci - Figura 23'''

    name = "figures/figure012ab"

    X = 1 # Scale #
    A = ( 0*X,5*X)
    B = ( 8*X,1*X)
    C = ( 8*X,0*X)
    D = ( 2*X,0*X)
    E = ( 0*X,4*X)

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


def figure012ac():
    '''El Tangram Egípci - Figura 23'''

    name = "figures/figure012ac"

    X = 1 # Scale #
    A = ( 0*X,5*X)
    B = ( 3*X,5*X)
    C = ( 7*X,2*X)
    D = ( 8*X,0*X)
    E = ( 5*X,0*X)
    F = ( 3*X,1*X)

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


def figure012ad():
    '''El Tangram Egípci - Figura 23'''

    name = "figures/figure012ad"

    X = 1 # Scale #
    A = (0*R5*X,2*R5*X)
    B = (1*R5*X,2*R5*X)
    C = (3*R5*X,1*R5*X)
    D = (3*R5*X,0*R5*X)
    E = (1*R5*X,0*R5*X)

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


def figure012ae():
    '''El Tangram Egípci - Figura 23'''

    name = "figures/figure012ae"

    X = 1 # Scale #
    A = (0*R5*X,0*R5*X)
    B = (2*R5*X,0*R5*X)
    C = (3*R5*X,2*R5*X)
    D = (1*R5*X,2*R5*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure012af():
    '''El Tangram Egípci - Figura 23'''

    name = "figures/figure012af"

    X = 1 # Scale #
    A = (0*R5*X,2*R5*X)
    B = (0*R5*X,0*R5*X)
    C = (2*R5*X,0*R5*X)
    D = (2*R5*X,1*R5*X)
    E = flip((2*R5*X,2*R5*X), A, D)

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


def figure013t():
    '''El Subtangram Egípci - Rectangle 2:1'''

    name = "figures/figure013t"

    X = 1 # Scale #
    A = (0*X, 0*X)
    B = (0*X, 4*X)
    C = (8*X, 4*X)
    D = (8*X, 0*X)
    E = (4*X, 0*X)
    F = (4*X, 4*X)
    G = (3*X, 0*X)
    H = (5*X, 4*X)
    I = (4*X, 2*X)
    
    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+VERYTHICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013u():
    '''El Subtangram Egípci - Rectangle 2:1'''

    name = "figures/figure013u"

    X = 1 # Scale #
    A = (0*X, 0*X)
    B = (0*X, 4*X)
    C = (8*X, 4*X)
    D = (8*X, 0*X)
    E = (4*X, 0*X)
    F = (4*X, 4*X)
    G = (3*X, 0*X)
    H = (5*X, 4*X)
    I = (4*X, 2*X)
    
    drawing = []
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*B),
                              path.lineto(*I),
                              path.closepath()), BASE+VERYTHICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*G),
                              path.lineto(*I),
                              path.closepath()), BASE+VERYTHICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*G),
                              path.closepath()), BASE+VERYTHICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+VERYTHICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*I),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+VERYTHICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*I),
                              path.lineto(*D),
                              path.closepath()), BASE+VERYTHICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*H),
                              path.closepath()), BASE+VERYTHICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*E),
                              path.lineto(*I),
                              path.closepath()), BASE+VERYTHICK+FILLED(RED)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013v():
    '''El Subtangram Egípci - Rectangle 2:1'''

    name = "figures/figure013v"

    X = 1 # Scale #
    A = (0*X, 0*X)
    B = (0*X, 4*X)
    C = (8*X, 4*X)
    D = (8*X, 0*X)
    E = (4*X, 0*X)
    F = (4*X, 4*X)
    G = (3*X, 0*X)
    H = (5*X, 4*X)
    I = (4*X, 2*X)
    
    drawing = []
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E)), BASE+DOTTED))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*F),
                              path.lineto(*E),
                              path.closepath()), BASE+VERYTHICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013w():
    '''El Subtangram Egípci - Rectangle 2:1'''

    name = "figures/figure013w"

    X = 1 # Scale #
    A = (0*X, 0*X)
    B = (0*X, 4*X)
    C = (8*X, 4*X)
    D = (8*X, 0*X)
    E = (4*X, 0*X)
    F = (4*X, 4*X)
    G = (3*X, 0*X)
    H = (5*X, 4*X)
    I = (4*X, 2*X)
    #A, B = B, A
    #C = flip(C, A, B)
    #D = flip(D, A, B)
    #E = flip(E, A, B)
    #F = flip(F, A, B)
    #G = flip(G, A, B)
    #H = flip(H, A, B)
    
    drawing = []
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*B),
                              path.lineto(*I),
                              path.closepath()), BASE+VERYTHICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*G),
                              path.lineto(*I),
                              path.closepath()), BASE+VERYTHICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*G),
                              path.closepath()), BASE+VERYTHICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*E),
                              path.lineto(*I),
                              path.closepath()), BASE+VERYTHICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E)), BASE+DOTTED))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013x():
    '''El Subtangram Egípci - Rectangle 2:1'''

    name = "figures/figure013x"

    X = 1 # Scale #
    A = (0*X, 0*X)
    B = (0*X, 4*X)
    C = (8*X, 4*X)
    D = (8*X, 0*X)
    E = (4*X, 0*X)
    F = (4*X, 4*X)
    G = (3*X, 0*X)
    H = (5*X, 4*X)
    I = (4*X, 2*X)
    CC = flip(C, B, D)
    
    drawing = []
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*B)), BASE+DASHED))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*G)), BASE+DOTTED))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+VERYTHICK))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*H),
                              path.lineto(*CC),
                              path.closepath()), BASE+VERYTHICK))
                              
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013y():
    '''El Subtangram Egípci - Rectangle 2:1'''

    name = "figures/figure013y"

    X = 1 # Scale #
    A = (0*X, 0*X)
    B = (0*X, 4*X)
    C = (8*X, 4*X)
    D = (8*X, 0*X)
    E = (4*X, 0*X)
    F = (4*X, 4*X)
    G = (3*X, 0*X)
    H = (5*X, 4*X)
    I = (4*X, 2*X)
    CC = flip(C, B, D)
    #A, CC, = CC, A
    #C, D = D, C
    #G, H = H, G
    #F = flip(F, G, H)
    
    drawing = []
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*G)), BASE+DOTTED))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*B),
                              path.lineto(*I),
                              path.closepath()), BASE+VERYTHICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*G),
                              path.lineto(*I),
                              path.closepath()), BASE+VERYTHICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*G),
                              path.closepath()), BASE+VERYTHICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.closepath()), BASE+VERYTHICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*H),
                              path.lineto(*CC),
                              path.closepath()), BASE+VERYTHICK+FILLED(YELLOW)))
                              
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013z():
    '''El Subtangram Egípci - Rectangle 2:1'''

    name = "figures/figure013z"

    X = 1 # Scale #
    A = (0*X, 0*X)
    B = (0*X, 4*X)
    C = (8*X, 4*X)
    D = (8*X, 0*X)
    E = (4*X, 0*X)
    F = (4*X, 4*X)
    G = (3*X, 0*X)
    H = (5*X, 4*X)
    I = (4*X, 2*X)
    CC = flip(C, B, D)
    
    drawing = []
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*B)), BASE+DASHED))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*A),
                              path.lineto(*D)), BASE+DOTTED))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+VERYTHICK))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*D),
                              path.lineto(*CC),
                              path.closepath()), BASE+VERYTHICK))
                              
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013zz():
    '''El Subtangram Egípci - Rectangle 2:1'''

    name = "figures/figure013zz"

    X = 1 # Scale #
    A = (0*X, 0*X)
    B = (0*X, 4*X)
    C = (8*X, 4*X)
    D = (8*X, 0*X)
    E = (4*X, 0*X)
    F = (4*X, 4*X)
    G = (3*X, 0*X)
    H = (5*X, 4*X)
    I = (4*X, 2*X)
    CC = flip(C, B, D)
    #CC, C = C, CC
    #D, B = B, D
    #F = flip(F, B, D)
    
    drawing = []
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*A),
                              path.lineto(*D)), BASE+DOTTED))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*B),
                              path.lineto(*I),
                              path.closepath()), BASE+VERYTHICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*I),
                              path.lineto(*D),
                              path.closepath()), BASE+VERYTHICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*H),
                              path.closepath()), BASE+VERYTHICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.closepath()), BASE+VERYTHICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*H),
                              path.lineto(*CC),
                              path.closepath()), BASE+VERYTHICK+FILLED(YELLOW)))
                              
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013aa():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure013aa"

    X = 1 # Scale #
    A = (0*X, 0*X)
    B = (2*X,-4*X)
    C = (8*X, 4*X)
    D = (8*X, 0*X)

    B = r_point(B, A, -atan2(1,2))
    C = r_point(C, A, -atan2(1,2))
    D = r_point(D, A, -atan2(1,2))

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013ab():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure013ab"

    X = 1 # Scale #
    A = ( 0*X,0*X)
    B = (10*X,0*X)
    C = ( 2*X,4*X)
    D = w_point(C, (5*X,0), 3, 2)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013ac():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure013ac"

    X = 1 # Scale #
    A = (   0*X,   0*X)
    B = (4*R5*X,   0*X)
    C = r_point((4*R5*X,3*X), B, atan2(2,1)+atan2(3,4)-pi/2)
    D = (2*R5*X,1*R5*X)
    
    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013ad():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure013ad"

    X = 1 # Scale #
    A = (0*X, 0*X)
    B = (5*X, 0*X)
    C = (3*X, 4*X)
    D = flip((0*X,4*X), A, C)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure013ae():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure013ae"

    X = 1 # Scale #
    A = (0*X, 0*X)
    B = (3*X, 6*X)
    C = (5*X, 5*X)
    D = (5*X, 2*X)
    E = (1*X, 0*X)

    B = r_point((B[0],B[1]), A, pi-atan2(2,1))
    C = r_point((C[0],C[1]), A, pi-atan2(2,1))
    D = r_point((D[0],D[1]), A, pi-atan2(2,1))
    E = r_point((E[0],E[1]), A, pi-atan2(2,1))
    
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


def figure013af():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure013af"

    X = 1 # Scale #
    A = ( 5*X, 2*X)
    B = ( 6*X, 0*X)
    C = ( 1*X, 0*X)
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


def figure013ag():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure013ag"

    X = 1 # Scale #
    A = ( 5*X, 2*X)
    B = ( 5*X, 0*X)
    C = (1*X,0*X)
    D = flip((0*X,0*X), (0*X,2*X), (1*X,0*X))
    E = ( 0*X, 2*X)
    F = r_point((5*X, 5*X), A, atan2(3,4))

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


def figure013ah():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure013ah"

    X = 1 # Scale #
    A = (1*X, 0*X)
    B = (6*X, 0*X)
    C = (4*X, 4*X)
    D = (0*X, 2*X)
    E = flip((0*X, 0*X), A, D)
        
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


def figure013ai():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure013ai"

    X = 1 # Scale #
    A = (1*X, 0*X)
    B = (6*X, 0*X)
    C = (4*X, 4*X)
    D = (0*X, 2*X)
    E = flip((0*X, 0*X), A, D)
    D = flip(D, A, C)
    E = flip(E, A, C)
    D, E = E, D
    
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


def figure013aj():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure013aj"

    X = 1 # Scale #
    A = (0*X, 0*X)
    B = (4*X, 0*X)
    C = (4*X, 4*X)
    D = (3*X, 4*X)
    E = flip((0*X,4*X), A, D)

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


def figure013ak():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure013ak"

    X = 1 # Scale #
    A = (3*X, 0*X)
    B = (7*X, 0*X)
    C = (7*X, 1*X)
    D = (3*X, 4*X)
    E = (0*X, 4*X)

    A = (-A[0],A[1])
    B = (-B[0],B[1])
    C = (-C[0],C[1])
    D = (-D[0],D[1])
    E = (-E[0],E[1])

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


def figure013al():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure013al"

    X = 1 # Scale #
    A = ( 5*X, 2*X)
    B = ( 4*X, 0*X)
    C = (-1*X, 0*X)
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


def figure013am():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure013am"

    X = 1 # Scale #
    A = (2*X, 0*X)
    B = (6*X, 0*X)
    C = (6*X, 2*X)
    D = (2*X, 4*X)
    E = (0*X, 4*X)

    A = (-A[0],A[1])
    B = (-B[0],B[1])
    C = (-C[0],C[1])
    D = (-D[0],D[1])
    E = (-E[0],E[1])
    
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


def figure013an():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure013an"

    X = 1 # Scale #
    A = ( 5*X, 2*X)
    B = flip((5*X,0*X),(4*X,0*X),(5*X,2*X))
    C = ( 4*X, 0*X)
    D = ( 0*X, 0*X)
    E = ( 0*X, 2*X)
    F = r_point((5*X, 5*X), A, atan2(3,4))

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


def figure013ao():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure013ao"

    X = 1 # Scale #
    A = (2*X, 0*X)
    B = (5*X, 0*X)
    C = flip((6*X, 0*X), (5*X, 0*X), (6*X, 2*X))
    D = (6*X, 2*X)
    E = (2*X, 4*X)
    F = (0*X, 4*X)

    A = (-A[0],A[1])
    B = (-B[0],B[1])
    C = (-C[0],C[1])
    D = (-D[0],D[1])
    E = (-E[0],E[1])
    F = (-F[0],F[1])
    
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


def figure013ba():
    '''El Subtangram Egípci - Angles'''

    name = "figures/figure013ba"

    X = 1 # Scale #
    A = (0*X, 0*X)
    B = (4*X, 0*X)
    C = (4*X, 4*X)
    D = (0*X, 4*X)
    E = (4*X, 2*X)
    F = (3*X, 4*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*A),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*F),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(RED)))

    R = 0.75*X
    a = atan2(1,2)*180/pi
    b = atan2(1,2)*180/pi

    drawing.append((path.path(path.moveto(A[0]+R, A[1]),
                    path.arc(A[0],A[1], R, 0, a+b)), BASE+THIN))

    drawing.append((path.path(path.moveto(F[0]-R, F[1]),
                    path.arc(F[0],F[1], R, 180, 180+a+b)), BASE+THIN))

    drawing.append((path.path(path.moveto(E[0]-0.2*X, E[1]+0.4*X),
                              path.lineto(E[0]-0.6*X, E[1]+0.2*X),
                              path.lineto(E[0]-0.4*X, E[1]-0.2*X)), BASE+THIN))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)

    mycanvas.draw(*put_text(0.95*X, 0.15*X, r"{\textalpha}"))
    mycanvas.draw(*put_text(0.80*X, 0.60*X, r"{\textbeta}"))
    mycanvas.draw(*put_text(1.80*X, 3.50*X, r"{\textalpha+\textbeta}"))
    mycanvas.draw(*put_text(1.90*X, 1.90*X, r"{1}"))

    mycanvas.draw(path.path(path.moveto(F[0],F[1]),path.lineto(E[0],E[1])),
                  [deco.curvedtext(r"\small\raisebox{-2ex}{{sin\,\textbeta}}")])
    mycanvas.draw(path.path(path.moveto(0.25*E[0],0.25*E[1]),path.lineto(E[0],E[1])),
                  [deco.curvedtext(r"\small\raisebox{ 1ex}{{cos\,\textbeta}}")])
    mycanvas.draw(path.path(path.moveto(F[0],F[1]),path.lineto(C[0],C[1])),
                  [deco.curvedtext(r"\small\raisebox{ 1ex}{{sin\,\textalpha\,\,sin\,\textbeta}}")])
    mycanvas.draw(path.path(path.moveto(C[0],C[1]),path.lineto(E[0],E[1])),
                  [deco.curvedtext(r"\small\raisebox{ 1ex}{{cos\,\textalpha\,\,sin\,\textbeta}}")])
    mycanvas.draw(path.path(path.moveto(E[0],E[1]),path.lineto(B[0],B[1])),
                  [deco.curvedtext(r"\small\raisebox{ 1ex}{{sin\,\textalpha\,\,cos\,\textbeta}}")])
    mycanvas.draw(path.path(path.moveto(A[0],A[1]),path.lineto(B[0],B[1])),
                  [deco.curvedtext(r"\small\raisebox{-2ex}{{cos\,\textalpha\,\,cos\,\textbeta}}")])


    mycanvas.writePDFfile(name)


def figure013bb():
    '''El Subtangram Egípci - Angles 2'''

    name = "figures/figure013bb"

    X = 1 # Scale #
    A = (0*X, 0*X)
    B = (4*X, 0*X)
    C = (4*X, 4*X)
    D = (0*X, 4*X)
    E = (4*X, 2*X)
    F = (3*X, 4*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*A),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*F),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(RED)))

    R = 0.75*X
    a = atan2(1,2)*180/pi
    b = atan2(1,2)*180/pi

    RA = r_point((A[0]+R, A[1]), A, atan2(1,2))

    drawing.append((path.path(path.moveto(*RA),
                    path.arc(A[0],A[1], R, a, 90)), BASE+THIN))

    drawing.append((path.path(path.moveto(E[0], E[1]-R*0.6),
                    path.arcn(E[0],E[1], R*0.6, 270, 180+a)), BASE+THIN))

    drawing.append((path.path(path.moveto(E[0]-0.2*X, E[1]+0.4*X),
                              path.lineto(E[0]-0.6*X, E[1]+0.2*X),
                              path.lineto(E[0]-0.4*X, E[1]-0.2*X)), BASE+THIN))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)

    mycanvas.draw(*put_text(0.35*X, 0.95*X, r"{\textalpha--\textbeta}"))
    mycanvas.draw(*put_text(0.80*X, 0.60*X, r"{\textbeta}"))
    mycanvas.draw(*put_text(3.65*X, 1.35*X, r"{\textalpha}"))
    mycanvas.draw(*put_text(1.90*X, 1.90*X, r"{1}"))

    mycanvas.draw(path.path(path.moveto(F[0],F[1]),path.lineto(E[0],E[1])),
                  [deco.curvedtext(r"\small\raisebox{-2ex}{{sin\,\textbeta}}")])
    mycanvas.draw(path.path(path.moveto(0.25*E[0],0.25*E[1]),path.lineto(E[0],E[1])),
                  [deco.curvedtext(r"\small\raisebox{ 1ex}{{cos\,\textbeta}}")])
    mycanvas.draw(path.path(path.moveto(F[0],F[1]),path.lineto(C[0],C[1])),
                  [deco.curvedtext(r"\small\raisebox{ 1ex}{{cos\,\textalpha\,\,sin\,\textbeta}}")])
    mycanvas.draw(path.path(path.moveto(C[0],C[1]),path.lineto(E[0],E[1])),
                  [deco.curvedtext(r"\small\raisebox{ 1ex}{{sin\,\textalpha\,\,sin\,\textbeta}}")])
    mycanvas.draw(path.path(path.moveto(E[0],E[1]),path.lineto(B[0],B[1])),
                  [deco.curvedtext(r"\small\raisebox{ 1ex}{{cos\,\textalpha\,\,cos\,\textbeta}}")])
    mycanvas.draw(path.path(path.moveto(A[0],A[1]),path.lineto(B[0],B[1])),
                  [deco.curvedtext(r"\small\raisebox{-2ex}{{sin\,\textalpha\,\,cos\,\textbeta}}")])

    mycanvas.writePDFfile(name)


def figure013bc():
    '''El Subtangram Egípci - Angles 3'''

    name = "figures/figure013bc"

    X = 1 # Scale #
    A = (0*X, 0*X)
    B = (4*X, 0*X)
    C = (4*X, 4*X)
    D = (0*X, 4*X)
    E = (4*X, 2*X)
    F = (3*X, 4*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*A),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*F),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(RED)))

    R = 0.75*X
    a = atan2(1,2)*180/pi
    b = atan2(1,2)*180/pi

    drawing.append((path.path(path.moveto(A[0]+R, A[1]),
                    path.arc(A[0],A[1], R, 0, a+b)), BASE+THIN))

    drawing.append((path.path(path.moveto(F[0]-R, F[1]),
                    path.arc(F[0],F[1], R, 180, 180+a+b)), BASE+THIN))

    drawing.append((path.path(path.moveto(E[0]-0.2*X, E[1]+0.4*X),
                              path.lineto(E[0]-0.6*X, E[1]+0.2*X),
                              path.lineto(E[0]-0.4*X, E[1]-0.2*X)), BASE+THIN))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)

    mycanvas.draw(*put_text(0.95*X, 0.15*X, r"{\textalpha}"))
    mycanvas.draw(*put_text(0.80*X, 0.60*X, r"{\textbeta}"))
    mycanvas.draw(*put_text(1.80*X, 3.50*X, r"{\textalpha+\textbeta}"))

    mycanvas.draw(path.path(path.moveto(F[0],F[1]),path.lineto(E[0]-0.1*X, E[1]+0.2*X)),
                  [deco.curvedtext(r"\footnotesize\raisebox{-2ex}{{sec\,\textalpha\,\,tan\,\textbeta}}")])
    mycanvas.draw(path.path(path.moveto(0.25*E[0],0.25*E[1]),path.lineto(E[0],E[1])),
                  [deco.curvedtext(r"\small\raisebox{ 1ex}{{sec\,\textalpha}}")])
    mycanvas.draw(path.path(path.moveto(F[0],F[1]),path.lineto(C[0],C[1])),
                  [deco.curvedtext(r"\small\raisebox{ 1ex}{{tan\,\textalpha\,\,tan\,\textbeta}}")])
    mycanvas.draw(path.path(path.moveto(C[0],C[1]),path.lineto(E[0],E[1])),
                  [deco.curvedtext(r"\small\raisebox{ 1ex}{{tan\,\textbeta}}")])
    mycanvas.draw(path.path(path.moveto(E[0],E[1]),path.lineto(B[0],B[1])),
                  [deco.curvedtext(r"\small\raisebox{ 1ex}{{tan\,\textalpha}}")])
    mycanvas.draw(path.path(path.moveto(A[0],A[1]),path.lineto(B[0],B[1])),
                  [deco.curvedtext(r"\small\raisebox{-2ex}{{1}}")])

    mycanvas.writePDFfile(name)


def figure013bd():
    '''El Subtangram Egípci - Angles 4'''

    name = "figures/figure013bd"

    X = 1 # Scale #
    A = (0*X, 0*X)
    B = (4*X, 0*X)
    C = (4*X, 4*X)
    D = (0*X, 4*X)
    E = (4*X, 2*X)
    F = (3*X, 4*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*A),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*F),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(RED)))

    R = 0.75*X
    a = atan2(1,2)*180/pi
    b = atan2(1,2)*180/pi

    RA = r_point((A[0]+R, A[1]), A, atan2(1,2))

    drawing.append((path.path(path.moveto(*RA),
                    path.arc(A[0],A[1], R, a, 90)), BASE+THIN))

    drawing.append((path.path(path.moveto(E[0], E[1]-R*0.6),
                    path.arcn(E[0],E[1], R*0.6, 270, 180+a)), BASE+THIN))

    drawing.append((path.path(path.moveto(E[0]-0.2*X, E[1]+0.4*X),
                              path.lineto(E[0]-0.6*X, E[1]+0.2*X),
                              path.lineto(E[0]-0.4*X, E[1]-0.2*X)), BASE+THIN))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)

    mycanvas.draw(*put_text(0.35*X, 0.95*X, r"{\textalpha--\textbeta}"))
    mycanvas.draw(*put_text(0.80*X, 0.60*X, r"{\textbeta}"))
    mycanvas.draw(*put_text(3.65*X, 1.35*X, r"{\textalpha}"))
    mycanvas.draw(*put_text(4.20*X, 0.95*X, r"\small{1}"))

    mycanvas.draw(path.path(path.moveto(F[0],F[1]),path.lineto(E[0]-0.1*X, E[1]+0.2*X)),
                  [deco.curvedtext(r"\footnotesize\raisebox{-2ex}{{sec\,\textalpha\,\,tan\,\textbeta}}")])
    mycanvas.draw(path.path(path.moveto(0.25*E[0],0.25*E[1]),path.lineto(E[0],E[1])),
                  [deco.curvedtext(r"\small\raisebox{ 1ex}{{sec\,\textalpha}}")])
    mycanvas.draw(path.path(path.moveto(F[0],F[1]),path.lineto(C[0],C[1])),
                  [deco.curvedtext(r"\small\raisebox{ 1ex}{{tan\,\textbeta}}")])
    mycanvas.draw(path.path(path.moveto(C[0],C[1]),path.lineto(E[0],E[1])),
                  [deco.curvedtext(r"\small\raisebox{ 1ex}{{tan\,\textalpha\,\,tan\,\textbeta}}")])
    mycanvas.draw(path.path(path.moveto(A[0],A[1]),path.lineto(B[0],B[1])),
                  [deco.curvedtext(r"\small\raisebox{-2ex}{{tan\,\textalpha}}")])

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


def figure016ch():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure016ch"

    X = 1.0 # Scale #
    Y = (2.0*R5+3.0) / (R5*X)
    Z = (4-R5/2.0)*X

    b = atan2(1,2)
    c = pi/2.0 - atan2(3,4)
    
    A = ( 0*X, 0*X)
    B = ( 0*X, 3*X)
    C = r_point((B[0]+4*X, B[1] + 2*X), B, b)
    D = r_point((B[0]+5*X, B[1]), B, b)
    J = ( 3*X, 2*X)
    I = r_point((3*X, (R5-2)*X), J, b)
    E = r_point((6*X, (R5+2)*X), J, b)
    H = w_point(E, I, 2, 3)
    G = (H[0] + 4*X, H[1])
    F = (G[0] , G[1] + 2*X)
    F = r_point(F, H, c)
    G = r_point(G, H, c)
    K = ( 1*X, 2*X)
    

    a = atan2(A[1]-I[1],I[0]-A[0])    

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


def figure018ae():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure018ae"

    X = 1 # Scale #
    A = (   0,   0)
    B = (10*X,   0)
    C = w_point(B, (4*X,3*X), 5, 3*R5-5)
    D = r_point((4*X + R5*X,3*X), (4*X,3*X), atan2(3,4))
    
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


def figure019ae():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure019ae"

    X = 1 # Scale #
    A = (   0,   0)
    B = (10*X,   0)
    C = w_point(B, (4*X,3*X), 5, 3*R5-5)
    D = r_point((4*X + R5*X,3*X), (4*X,3*X), atan2(3,4))
    
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


def figure020g():
    '''Golden Rectangle'''

    name = "figures/figure020g"

    X = 1
    A = (0,2*R5*X)
    B = (0,0)
    C = (R5*X,0)
    D = (R5*X+5*X,0)
    E = r_point((R5*X+5*X,4*X),    D, pi/2-atan2(3,4))
    F = r_point((R5*X+5*X,2*R5*X), D, pi/2-atan2(3,4))
    G = r_point((R5*X+5*X,4*X),    D, pi/2-atan2(3,4)-atan2(1,2))
    H = w_point(C, E, 3-R5,R5)
    I = r_point(C, H, -pi/2)
    J = w_point(A, C, 3, 2)
    K = r_point((J[0], J[1]+1*X+R5*X), J, atan2(1,2)-pi/2)
    L = w_point(H, I, 1, R5-1)
    
    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*E),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*L),
                              path.lineto(*I),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020h():
    '''Golden Rectangle'''

    name = "figures/figure020h"

    X = 1
    A = (0  ,0)
    B = (2*X,0)
    C = (5*X,0)
    D = (5*X,3*X)
    E = (9*X,3*X)
    F = r_point((4*X,3*X), E, -atan2(1,2))
    G = (F[0],3*X)
    H = (2*X,4*X)
    I = (2*X,X+R5*X)
    J = (2*X,X)
    K = (4*X,2*X)
    L = w_point(J,K,R5-1,1)

    #A = r_point(A, C, -atan2(1,2))
    #B = r_point(B, C, -atan2(1,2))
    #H = r_point(H, C, -atan2(1,2))
    #I = r_point(I, C, -atan2(1,2))
    #J = r_point(J, C, -atan2(1,2))
    #K = r_point(K, C, -atan2(1,2))
    #L = r_point(L, C, -atan2(1,2))

    D = r_point(D, C, atan2(1,2))
    E = r_point(E, C, atan2(1,2))
    F = r_point(F, C, atan2(1,2))
    G = r_point(G, C, atan2(1,2))
    
    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*E),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*K),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*L),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*G),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*H),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020i():
    '''Golden Rectangle'''

    name = "figures/figure020i"

    X = 1
    A = (0  ,  0)
    B = (4*X,2*X)
    C = (5*X,  0)
    D = r_point((   0,2*X), A, -atan2(2,1))
    E = r_point((-4*X,2*X), A, -atan2(2,1))
    F = r_point((5*X,3*X), C, atan2(1,2))
    G = r_point((9*X,3*X), C, atan2(1,2))
    H = r_point((5*X,3*X), C, -atan2(1,2))
    I = r_point((6*X,3*X), C, -atan2(1,2))
    J = r_point(((6+R5)*X,3*X), C, -atan2(1,2))
    K = r_point((7*X,1*X), C, -atan2(1,2))
    L = w_point(I,K,R5-1,1)
    
    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*C),
                              path.lineto(*K),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*L),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020j():
    '''Golden Rectangle'''

    name = "figures/figure020j"

    X = 1
    A = (0  ,  0)
    B = (4*X,  0)
    C = (4*X,3*X)
    D = (4*X,4*X)
    E = (6*X,4*X)
    F = r_point((4*X,-2*X), C, -atan2(2,1)-atan2(4,3))
    G = r_point((6*X, 2*X), C, -atan2(2,1)-atan2(4,3))
    H = (4*X,     3*X+R5*X)
    I = (4*X-R5*X,3*X+R5*X)
    J = w_point(F,C,3,2)
    K = (5*X-R5*X,3*X+R5*X)
    L = (5*X-R5*X,5*X+R5*X)
    
    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*L),
                              path.lineto(*I),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))

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


def figure022a():
    '''Areas and Perimeters'''

    name = "figures/figure022a"

    X  = 1
    A  = (0*X,-0.5*X)
    B  = (1*X,-0.5*X)
    C  = (2*X,-0.5*X)
    D  = (3*X,-0.5*X)
    E  = (4*X,-0.5*X)
    F  = (5*X,-0.5*X)
    G  = (6*X,-0.5*X)
    AA = (0*X, 6.5*X)
    BB = (1*X, 6.5*X)
    CC = (2*X, 6.5*X)
    DD = (3*X, 6.5*X)
    EE = (4*X, 6.5*X)
    FF = (5*X, 6.5*X)
    GG = (6*X, 6.5*X)

    H  = (-0.5*X, 0*X)
    I  = (-0.5*X, 1*X)
    J  = (-0.5*X, 2*X)
    K  = (-0.5*X, 3*X)
    L  = (-0.5*X, 4*X)
    M  = (-0.5*X, 5*X)
    N  = (-0.5*X, 6*X)
    HH = ( 6.5*X, 0*X)
    II = ( 6.5*X, 1*X)
    JJ = ( 6.5*X, 2*X)
    KK = ( 6.5*X, 3*X)
    LL = ( 6.5*X, 4*X)
    MM = ( 6.5*X, 5*X)
    NN = ( 6.5*X, 6*X)

    O = (0*X, 3*X)
    P = (6*X, 0*X)
    Q = (6*X, 5*X)
    R = (4*X, 6*X)

    S = (4*X, 1*X)
    T = (4*X, 3*X)
    U = (5*X, 3*X)
    
    drawing = []

    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*T),
                              path.lineto(*R),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*Q),
                              path.lineto(*R),
                              path.lineto(*T),
                              path.lineto(*U),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*T),
                              path.lineto(*U),
                              path.lineto(*S),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*P),
                              path.lineto(*Q),
                              path.lineto(*S),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*T),
                              path.lineto(*O),
                              path.lineto(*S),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*P),
                              path.lineto(*Q),
                              path.lineto(*R),
                              path.closepath()), BASE))

    drawing.append((path.path(path.moveto(*A), path.lineto(*AA),
                              path.moveto(*B), path.lineto(*BB),
                              path.moveto(*C), path.lineto(*CC),
                              path.moveto(*D), path.lineto(*DD),
                              path.moveto(*E), path.lineto(*EE),
                              path.moveto(*F), path.lineto(*FF),
                              path.moveto(*G), path.lineto(*GG),
                              path.moveto(*H), path.lineto(*HH),
                              path.moveto(*I), path.lineto(*II),
                              path.moveto(*J), path.lineto(*JJ),
                              path.moveto(*K), path.lineto(*KK),
                              path.moveto(*L), path.lineto(*LL),
                              path.moveto(*M), path.lineto(*MM),
                              path.moveto(*N), path.lineto(*NN)), BASE+DOTTED+THIN))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022b():
    '''Areas and Perimeters'''

    name = "figures/figure022b"

    X  = 1
    A  = (0*X,-0.5*X)
    B  = (1*X,-0.5*X)
    C  = (2*X,-0.5*X)
    D  = (3*X,-0.5*X)
    E  = (4*X,-0.5*X)
    F  = (5*X,-0.5*X)
    G  = (6*X,-0.5*X)
    AA = (0*X, 6.5*X)
    BB = (1*X, 6.5*X)
    CC = (2*X, 6.5*X)
    DD = (3*X, 6.5*X)
    EE = (4*X, 6.5*X)
    FF = (5*X, 6.5*X)
    GG = (6*X, 6.5*X)

    H  = (-0.5*X, 0*X)
    I  = (-0.5*X, 1*X)
    J  = (-0.5*X, 2*X)
    K  = (-0.5*X, 3*X)
    L  = (-0.5*X, 4*X)
    M  = (-0.5*X, 5*X)
    N  = (-0.5*X, 6*X)
    HH = ( 6.5*X, 0*X)
    II = ( 6.5*X, 1*X)
    JJ = ( 6.5*X, 2*X)
    KK = ( 6.5*X, 3*X)
    LL = ( 6.5*X, 4*X)
    MM = ( 6.5*X, 5*X)
    NN = ( 6.5*X, 6*X)

    BBB  = (1*X, 2.50*X)
    CCC  = (2*X, 2.00*X)
    DDD  = (3*X, 1.50*X)
    EEE  = (4*X, 1.00*X)
    FFF  = (5*X, 0.50*X)
    BBBB = (1*X, 3.75*X)
    CCCC = (2*X, 4.50*X)
    DDDD = (3*X, 5.25*X)
    EEEE = (4*X, 6.00*X)
    FFFF = (5*X, 5.50*X)
    
    III  = (4.000*X, 1*X)
    JJJ  = (2.000*X, 2*X)
    KKK  = (0.000*X, 3*X)
    LLL  = (1.333*X, 4*X)
    MMM  = (2.666*X, 5*X)
    IIII = (6.000*X, 1*X)
    JJJJ = (6.000*X, 2*X)
    KKKK = (6.000*X, 3*X)
    LLLL = (6.000*X, 4*X)
    MMMM = (6.000*X, 5*X)

    O = (0*X, 3*X)
    P = (6*X, 0*X)
    Q = (6*X, 5*X)
    R = (4*X, 6*X)

    S = (2*X, 2*X)
    T = (4*X, 1*X)
    
    drawing = []

    drawing.append((path.path(path.moveto(*A), path.lineto(*AA),
                              path.moveto(*B), path.lineto(*BB),
                              path.moveto(*C), path.lineto(*CC),
                              path.moveto(*D), path.lineto(*DD),
                              path.moveto(*E), path.lineto(*EE),
                              path.moveto(*F), path.lineto(*FF),
                              path.moveto(*G), path.lineto(*GG),
                              path.moveto(*H), path.lineto(*HH),
                              path.moveto(*I), path.lineto(*II),
                              path.moveto(*J), path.lineto(*JJ),
                              path.moveto(*K), path.lineto(*KK),
                              path.moveto(*L), path.lineto(*LL),
                              path.moveto(*M), path.lineto(*MM),
                              path.moveto(*N), path.lineto(*NN)), BASE+DOTTED+THIN))

    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*P),
                              path.lineto(*Q),
                              path.lineto(*R),
                              path.closepath()), BASE+FILLED(WHITE)))

    drawing.append((path.path(path.moveto(*BBB), path.lineto(*BBBB),
                              path.moveto(*CCC), path.lineto(*CCCC),
                              path.moveto(*DDD), path.lineto(*DDDD),
                              path.moveto(*EEE), path.lineto(*EEEE),
                              path.moveto(*FFF), path.lineto(*FFFF),
                              path.moveto(*III), path.lineto(*IIII),
                              path.moveto(*JJJ), path.lineto(*JJJJ),
                              path.moveto(*KKK), path.lineto(*KKKK),
                              path.moveto(*LLL), path.lineto(*LLLL),
                              path.moveto(*MMM), path.lineto(*MMMM)), BASE+DOTTED+THIN+COLOR(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022c():
    '''Areas and Perimeters'''

    name = "figures/figure022c"

    X  = 1
    Y  = 0.125
    A  = (0*X,-0.5*X)
    B  = (1*X,-0.5*X)
    C  = (2*X,-0.5*X)
    D  = (3*X,-0.5*X)
    E  = (4*X,-0.5*X)
    F  = (5*X,-0.5*X)
    G  = (6*X,-0.5*X)
    AA = (0*X, 6.5*X)
    BB = (1*X, 6.5*X)
    CC = (2*X, 6.5*X)
    DD = (3*X, 6.5*X)
    EE = (4*X, 6.5*X)
    FF = (5*X, 6.5*X)
    GG = (6*X, 6.5*X)

    H  = (-0.5*X, 0*X)
    I  = (-0.5*X, 1*X)
    J  = (-0.5*X, 2*X)
    K  = (-0.5*X, 3*X)
    L  = (-0.5*X, 4*X)
    M  = (-0.5*X, 5*X)
    N  = (-0.5*X, 6*X)
    HH = ( 6.5*X, 0*X)
    II = ( 6.5*X, 1*X)
    JJ = ( 6.5*X, 2*X)
    KK = ( 6.5*X, 3*X)
    LL = ( 6.5*X, 4*X)
    MM = ( 6.5*X, 5*X)
    NN = ( 6.5*X, 6*X)

    BBB  = (1*X, 2.50*X)
    CCC  = (2*X, 2.00*X)
    DDD  = (3*X, 1.50*X)
    EEE  = (4*X, 1.00*X)
    FFF  = (5*X, 0.50*X)
    BBBB = (1*X, 3.75*X)
    CCCC = (2*X, 4.50*X)
    DDDD = (3*X, 5.25*X)
    EEEE = (4*X, 6.00*X)
    FFFF = (5*X, 5.50*X)
    
    III  = (4.000*X, 1*X)
    JJJ  = (2.000*X, 2*X)
    KKK  = (0.000*X, 3*X)
    LLL  = (1.333*X, 4*X)
    MMM  = (2.666*X, 5*X)
    IIII = (6.000*X, 1*X)
    JJJJ = (6.000*X, 2*X)
    KKKK = (6.000*X, 3*X)
    LLLL = (6.000*X, 4*X)
    MMMM = (6.000*X, 5*X)

    O = (0*X, 3*X)
    P = (6*X, 0*X)
    Q = (6*X, 5*X)
    R = (4*X, 6*X)

    S = (2*X, 2*X)
    T = (4*X, 1*X)
    

    drawing = []

    drawing.append((path.path(path.moveto(*A), path.lineto(*AA),
                              path.moveto(*B), path.lineto(*BB),
                              path.moveto(*C), path.lineto(*CC),
                              path.moveto(*D), path.lineto(*DD),
                              path.moveto(*E), path.lineto(*EE),
                              path.moveto(*F), path.lineto(*FF),
                              path.moveto(*G), path.lineto(*GG),
                              path.moveto(*H), path.lineto(*HH),
                              path.moveto(*I), path.lineto(*II),
                              path.moveto(*J), path.lineto(*JJ),
                              path.moveto(*K), path.lineto(*KK),
                              path.moveto(*L), path.lineto(*LL),
                              path.moveto(*M), path.lineto(*MM),
                              path.moveto(*N), path.lineto(*NN)), BASE+DOTTED+THIN))

    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*P),
                              path.lineto(*Q),
                              path.lineto(*R),
                              path.closepath()), BASE+THIN+FILLED(WHITE)))

    drawing.append((path.path(path.moveto(*BBB), path.lineto(*BBBB),
                              path.moveto(*CCC), path.lineto(*CCCC),
                              path.moveto(*DDD), path.lineto(*DDDD),
                              path.moveto(*EEE), path.lineto(*EEEE),
                              path.moveto(*FFF), path.lineto(*FFFF),
                              path.moveto(*III), path.lineto(*IIII),
                              path.moveto(*JJJ), path.lineto(*JJJJ),
                              path.moveto(*KKK), path.lineto(*KKKK),
                              path.moveto(*LLL), path.lineto(*LLLL),
                              path.moveto(*MMM), path.lineto(*MMMM)), BASE+DOTTED+THIN+COLOR(BLACK)))

    INTERIOR = BASE+VERYTHIN+COLOR(WHITE)+FILLED(GREEN)
    BOUNDARY = BASE+VERYTHIN+COLOR(WHITE)+FILLED(ORANGE)

    drawing.append((path.circle(6*X, 0*X, Y), BOUNDARY))
    drawing.append((path.circle(6*X, 1*X, Y), BOUNDARY))
    drawing.append((path.circle(6*X, 2*X, Y), BOUNDARY))
    drawing.append((path.circle(6*X, 3*X, Y), BOUNDARY))
    drawing.append((path.circle(6*X, 4*X, Y), BOUNDARY))
    drawing.append((path.circle(6*X, 5*X, Y), BOUNDARY))
    drawing.append((path.circle(4*X, 1*X, Y), BOUNDARY))
    drawing.append((path.circle(2*X, 2*X, Y), BOUNDARY))
    drawing.append((path.circle(0*X, 3*X, Y), BOUNDARY))
    drawing.append((path.circle(4*X, 6*X, Y), BOUNDARY))
    
    drawing.append((path.circle(3*X, 5*X, Y), INTERIOR))
    drawing.append((path.circle(4*X, 5*X, Y), INTERIOR))
    drawing.append((path.circle(5*X, 5*X, Y), INTERIOR))
    drawing.append((path.circle(2*X, 4*X, Y), INTERIOR))
    drawing.append((path.circle(3*X, 4*X, Y), INTERIOR))
    drawing.append((path.circle(4*X, 4*X, Y), INTERIOR))
    drawing.append((path.circle(5*X, 4*X, Y), INTERIOR))
    drawing.append((path.circle(1*X, 3*X, Y), INTERIOR))
    drawing.append((path.circle(2*X, 3*X, Y), INTERIOR))
    drawing.append((path.circle(3*X, 3*X, Y), INTERIOR))
    drawing.append((path.circle(4*X, 3*X, Y), INTERIOR))
    drawing.append((path.circle(5*X, 3*X, Y), INTERIOR))
    drawing.append((path.circle(3*X, 2*X, Y), INTERIOR))
    drawing.append((path.circle(4*X, 2*X, Y), INTERIOR))
    drawing.append((path.circle(5*X, 2*X, Y), INTERIOR))
    drawing.append((path.circle(5*X, 1*X, Y), INTERIOR))



    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure023a():
    '''Cairo Tiling'''

    name = "figures/figure023a"

    SCALE  = 1
    WIDTH  = 4
    HEIGHT = 2
    
    drawing = []

    drawing.append((path.path(path.moveto(4*SCALE,      4*SCALE),
                              path.lineto(8*WIDTH*SCALE,4*SCALE),
                              path.lineto(8*WIDTH*SCALE,8*HEIGHT*SCALE),
                              path.lineto(4*SCALE,      8*HEIGHT*SCALE),
                              path.closepath()), BASE+VERYTHICK))

    """for x in range(5,8*WIDTH):
        drawing.append((path.path(path.moveto(x*SCALE,4*SCALE),
                                  path.lineto(x*SCALE,8*HEIGHT*SCALE)), BASE+THIN+DOTTED+COLOR(BLACK)))

    for y in range(5,8*HEIGHT):
        drawing.append((path.path(path.moveto(4*SCALE,y*SCALE),
                                  path.lineto(8*WIDTH*SCALE,y*SCALE)), BASE+THIN+DOTTED+COLOR(BLACK)))
    """
    for x in range(1,2*WIDTH):
        drawing.append((path.path(path.moveto(x*4*SCALE,4*SCALE),
                                  path.lineto(x*4*SCALE,8*HEIGHT*SCALE)), BASE+VERYTHICK))

    for y in range(1,2*HEIGHT):
        drawing.append((path.path(path.moveto(4*SCALE,y*4*SCALE),
                                  path.lineto(8*WIDTH*SCALE,y*4*SCALE)), BASE+VERYTHICK))

    for x in range(4, 8*WIDTH, 8):
        for y in range(4, 8*HEIGHT, 8):

            drawing.append((path.path(path.moveto((x+1)*SCALE, (y+0)*SCALE),
                                      path.lineto((x+3)*SCALE, (y+4)*SCALE)), BASE+VERYTHICK))    
            drawing.append((path.path(path.moveto((x+0)*SCALE, (y+3)*SCALE),
                                      path.lineto((x+4)*SCALE, (y+1)*SCALE)), BASE+VERYTHICK))
            if x+7 < 8*WIDTH:
                drawing.append((path.path(path.moveto((x+7)*SCALE, (y+0)*SCALE),
                                          path.lineto((x+5)*SCALE, (y+4)*SCALE)), BASE+VERYTHICK))
                drawing.append((path.path(path.moveto((x+4)*SCALE, (y+1)*SCALE),
                                          path.lineto((x+8)*SCALE, (y+3)*SCALE)), BASE+VERYTHICK))
            if y+7 < 8*HEIGHT:
                drawing.append((path.path(path.moveto((x+0)*SCALE, (y+5)*SCALE),
                                          path.lineto((x+4)*SCALE, (y+7)*SCALE)), BASE+VERYTHICK))                                      
                drawing.append((path.path(path.moveto((x+3)*SCALE, (y+4)*SCALE),
                                          path.lineto((x+1)*SCALE, (y+8)*SCALE)), BASE+VERYTHICK))    
            if x+7 < 8*WIDTH and y+7 < 8*HEIGHT:
                drawing.append((path.path(path.moveto((x+5)*SCALE, (y+4)*SCALE),
                                          path.lineto((x+7)*SCALE, (y+8)*SCALE)), BASE+VERYTHICK))
                drawing.append((path.path(path.moveto((x+4)*SCALE, (y+7)*SCALE),
                                          path.lineto((x+8)*SCALE, (y+5)*SCALE)), BASE+VERYTHICK))                                      

    drawing.append((path.path(path.moveto(4*SCALE,      4*SCALE),
                              path.lineto(8*WIDTH*SCALE,4*SCALE),
                              path.lineto(8*WIDTH*SCALE,8*HEIGHT*SCALE),
                              path.lineto(4*SCALE,      8*HEIGHT*SCALE),
                              path.closepath()), BASE+VERYTHICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure023b():
    '''Cairo Tiling'''

    name = "figures/figure023b"

    SCALE  = 1
    WIDTH  = 4
    HEIGHT = 2
    
    drawing = []

    drawing.append((path.path(path.moveto(4*SCALE,      4*SCALE),
                              path.lineto(8*WIDTH*SCALE,4*SCALE),
                              path.lineto(8*WIDTH*SCALE,8*HEIGHT*SCALE),
                              path.lineto(4*SCALE,      8*HEIGHT*SCALE),
                              path.closepath()), BASE+VERYTHICK+FILLED(ORANGE)))

    """for x in range(5,8*WIDTH):
        drawing.append((path.path(path.moveto(x*SCALE,4*SCALE),
                                  path.lineto(x*SCALE,8*HEIGHT*SCALE)), BASE+THIN+DOTTED+COLOR(BLACK)))

    for y in range(5,8*HEIGHT):
        drawing.append((path.path(path.moveto(4*SCALE,y*SCALE),
                                  path.lineto(8*WIDTH*SCALE,y*SCALE)), BASE+THIN+DOTTED+COLOR(BLACK)))
    """
    for x in range(1,2*WIDTH):
        drawing.append((path.path(path.moveto(x*4*SCALE,4*SCALE),
                                  path.lineto(x*4*SCALE,8*HEIGHT*SCALE)), BASE+VERYTHICK))

    for y in range(1,2*HEIGHT):
        drawing.append((path.path(path.moveto(4*SCALE,y*4*SCALE),
                                  path.lineto(8*WIDTH*SCALE,y*4*SCALE)), BASE+VERYTHICK))

    for x in range(4, 8*WIDTH, 8):
        for y in range(4, 8*HEIGHT, 8):

            drawing.append((path.path(path.moveto((x+1)*SCALE, (y+0)*SCALE),
                                      path.lineto((x+3)*SCALE, (y+4)*SCALE)), BASE+VERYTHICK))    
            drawing.append((path.path(path.moveto((x+0)*SCALE, (y+3)*SCALE),
                                      path.lineto((x+4)*SCALE, (y+1)*SCALE)), BASE+VERYTHICK))
            if x+7 < 8*WIDTH:
                drawing.append((path.path(path.moveto((x+7)*SCALE, (y+0)*SCALE),
                                          path.lineto((x+5)*SCALE, (y+4)*SCALE)), BASE+VERYTHICK))
                drawing.append((path.path(path.moveto((x+4)*SCALE, (y+1)*SCALE),
                                          path.lineto((x+8)*SCALE, (y+3)*SCALE)), BASE+VERYTHICK))
            if y+7 < 8*HEIGHT:
                drawing.append((path.path(path.moveto((x+0)*SCALE, (y+5)*SCALE),
                                          path.lineto((x+4)*SCALE, (y+7)*SCALE)), BASE+VERYTHICK))                                      
                drawing.append((path.path(path.moveto((x+3)*SCALE, (y+4)*SCALE),
                                          path.lineto((x+1)*SCALE, (y+8)*SCALE)), BASE+VERYTHICK))    
            if x+7 < 8*WIDTH and y+7 < 8*HEIGHT:
                drawing.append((path.path(path.moveto((x+5)*SCALE, (y+4)*SCALE),
                                          path.lineto((x+7)*SCALE, (y+8)*SCALE)), BASE+VERYTHICK))
                drawing.append((path.path(path.moveto((x+4)*SCALE, (y+7)*SCALE),
                                          path.lineto((x+8)*SCALE, (y+5)*SCALE)), BASE+VERYTHICK))                                      

    drawing.append((path.path(path.moveto(4*SCALE,      4*SCALE),
                              path.lineto(8*WIDTH*SCALE,4*SCALE),
                              path.lineto(8*WIDTH*SCALE,8*HEIGHT*SCALE),
                              path.lineto(4*SCALE,      8*HEIGHT*SCALE),
                              path.closepath()), BASE+VERYTHICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure023c():
    '''Cairo Tiling'''

    name = "figures/figure023c"

    SCALE  = 1
    WIDTH  = 4
    HEIGHT = 2
    
    drawing = []

    drawing.append((path.path(path.moveto(4*SCALE,      4*SCALE),
                              path.lineto(8*WIDTH*SCALE,4*SCALE),
                              path.lineto(8*WIDTH*SCALE,8*HEIGHT*SCALE),
                              path.lineto(4*SCALE,      8*HEIGHT*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))

    for x in range(5,8*WIDTH):
        drawing.append((path.path(path.moveto(x*SCALE,4*SCALE),
                                  path.lineto(x*SCALE,8*HEIGHT*SCALE)), BASE+THIN+DOTTED))

    for y in range(5,8*HEIGHT):
        drawing.append((path.path(path.moveto(4*SCALE,y*SCALE),
                                  path.lineto(8*WIDTH*SCALE,y*SCALE)), BASE+THIN+DOTTED))
    
    for x in range(1,2*WIDTH):
        drawing.append((path.path(path.moveto(x*4*SCALE,4*SCALE),
                                  path.lineto(x*4*SCALE,8*HEIGHT*SCALE)), BASE+ULTRATHICK))

    for y in range(1,2*HEIGHT):
        drawing.append((path.path(path.moveto(4*SCALE,y*4*SCALE),
                                  path.lineto(8*WIDTH*SCALE,y*4*SCALE)), BASE+ULTRATHICK))

    for x in range(4, 8*WIDTH, 8):
        for y in range(4, 8*HEIGHT, 8):

            drawing.append((path.path(path.moveto((x+1)*SCALE, (y+0)*SCALE),
                                      path.lineto((x+3)*SCALE, (y+4)*SCALE)), BASE+ULTRATHICK))    
            drawing.append((path.path(path.moveto((x+0)*SCALE, (y+3)*SCALE),
                                      path.lineto((x+4)*SCALE, (y+1)*SCALE)), BASE+ULTRATHICK))
            if x+7 < 8*WIDTH:
                drawing.append((path.path(path.moveto((x+7)*SCALE, (y+0)*SCALE),
                                          path.lineto((x+5)*SCALE, (y+4)*SCALE)), BASE+ULTRATHICK))
                drawing.append((path.path(path.moveto((x+4)*SCALE, (y+1)*SCALE),
                                          path.lineto((x+8)*SCALE, (y+3)*SCALE)), BASE+ULTRATHICK))
            if y+7 < 8*HEIGHT:
                drawing.append((path.path(path.moveto((x+0)*SCALE, (y+5)*SCALE),
                                          path.lineto((x+4)*SCALE, (y+7)*SCALE)), BASE+ULTRATHICK))                                      
                drawing.append((path.path(path.moveto((x+3)*SCALE, (y+4)*SCALE),
                                          path.lineto((x+1)*SCALE, (y+8)*SCALE)), BASE+ULTRATHICK))    
            if x+7 < 8*WIDTH and y+7 < 8*HEIGHT:
                drawing.append((path.path(path.moveto((x+5)*SCALE, (y+4)*SCALE),
                                          path.lineto((x+7)*SCALE, (y+8)*SCALE)), BASE+ULTRATHICK))
                drawing.append((path.path(path.moveto((x+4)*SCALE, (y+7)*SCALE),
                                          path.lineto((x+8)*SCALE, (y+5)*SCALE)), BASE+ULTRATHICK))                                      

    drawing.append((path.path(path.moveto(4*SCALE,      4*SCALE),
                              path.lineto(8*WIDTH*SCALE,4*SCALE),
                              path.lineto(8*WIDTH*SCALE,8*HEIGHT*SCALE),
                              path.lineto(4*SCALE,      8*HEIGHT*SCALE),
                              path.closepath()), BASE+ULTRATHICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure023d():
    '''Cairo Tiling'''

    name = "figures/figure023d"

    SCALE  = 1
    WIDTH  = 4
    HEIGHT = 2
    
    drawing = []

    drawing.append((path.path(path.moveto(4*SCALE,      4*SCALE),
                              path.lineto(8*WIDTH*SCALE,4*SCALE),
                              path.lineto(8*WIDTH*SCALE,8*HEIGHT*SCALE),
                              path.lineto(4*SCALE,      8*HEIGHT*SCALE),
                              path.closepath()), BASE+VERYTHICK))

    for x in range(5,8*WIDTH):
        drawing.append((path.path(path.moveto(x*SCALE,4*SCALE),
                                  path.lineto(x*SCALE,8*HEIGHT*SCALE)), BASE+THIN+DOTTED))

    for y in range(5,8*HEIGHT):
        drawing.append((path.path(path.moveto(4*SCALE,y*SCALE),
                                  path.lineto(8*WIDTH*SCALE,y*SCALE)), BASE+THIN+DOTTED))
    
    for x in range(1,2*WIDTH):
        drawing.append((path.path(path.moveto(x*4*SCALE,4*SCALE),
                                  path.lineto(x*4*SCALE,8*HEIGHT*SCALE)), BASE+VERYTHICK))

    for y in range(1,2*HEIGHT):
        drawing.append((path.path(path.moveto(4*SCALE,y*4*SCALE),
                                  path.lineto(8*WIDTH*SCALE,y*4*SCALE)), BASE+VERYTHICK))

    for x in range(4, 8*WIDTH, 8):
        for y in range(4, 8*HEIGHT, 8):

            drawing.append((path.path(path.moveto((x+1)*SCALE, (y+0)*SCALE),
                                      path.lineto((x+3)*SCALE, (y+4)*SCALE)), BASE+VERYTHICK))    
            drawing.append((path.path(path.moveto((x+0)*SCALE, (y+3)*SCALE),
                                      path.lineto((x+4)*SCALE, (y+1)*SCALE)), BASE+VERYTHICK))
            if x+7 < 8*WIDTH:
                drawing.append((path.path(path.moveto((x+7)*SCALE, (y+0)*SCALE),
                                          path.lineto((x+5)*SCALE, (y+4)*SCALE)), BASE+VERYTHICK))
                drawing.append((path.path(path.moveto((x+4)*SCALE, (y+1)*SCALE),
                                          path.lineto((x+8)*SCALE, (y+3)*SCALE)), BASE+VERYTHICK))
            if y+7 < 8*HEIGHT:
                drawing.append((path.path(path.moveto((x+0)*SCALE, (y+5)*SCALE),
                                          path.lineto((x+4)*SCALE, (y+7)*SCALE)), BASE+VERYTHICK))                                      
                drawing.append((path.path(path.moveto((x+3)*SCALE, (y+4)*SCALE),
                                          path.lineto((x+1)*SCALE, (y+8)*SCALE)), BASE+VERYTHICK))    
            if x+7 < 8*WIDTH and y+7 < 8*HEIGHT:
                drawing.append((path.path(path.moveto((x+5)*SCALE, (y+4)*SCALE),
                                          path.lineto((x+7)*SCALE, (y+8)*SCALE)), BASE+VERYTHICK))
                drawing.append((path.path(path.moveto((x+4)*SCALE, (y+7)*SCALE),
                                          path.lineto((x+8)*SCALE, (y+5)*SCALE)), BASE+VERYTHICK))                                      

    drawing.append((path.path(path.moveto(4*SCALE,      4*SCALE),
                              path.lineto(8*WIDTH*SCALE,4*SCALE),
                              path.lineto(8*WIDTH*SCALE,8*HEIGHT*SCALE),
                              path.lineto(4*SCALE,      8*HEIGHT*SCALE),
                              path.closepath()), BASE+VERYTHICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure023e():
    '''Cairo Tiling'''

    name = "figures/figure023e"

    SCALE  = 1
    WIDTH  = 4
    HEIGHT = 2
    
    drawing = []

    drawing.append((path.path(path.moveto(4*SCALE,      4*SCALE),
                              path.lineto(8*WIDTH*SCALE,4*SCALE),
                              path.lineto(8*WIDTH*SCALE,8*HEIGHT*SCALE),
                              path.lineto(4*SCALE,      8*HEIGHT*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))

    for x in range(5,8*WIDTH):
        drawing.append((path.path(path.moveto(x*SCALE,4*SCALE),
                                  path.lineto(x*SCALE,8*HEIGHT*SCALE)), BASE+THIN+DOTTED))

    for y in range(5,8*HEIGHT):
        drawing.append((path.path(path.moveto(4*SCALE,y*SCALE),
                                  path.lineto(8*WIDTH*SCALE,y*SCALE)), BASE+THIN+DOTTED))
    
    for x in range(1,2*WIDTH):
        drawing.append((path.path(path.moveto(x*4*SCALE,4*SCALE),
                                  path.lineto(x*4*SCALE,8*HEIGHT*SCALE)), BASE+ULTRATHICK))

    for y in range(1,2*HEIGHT):
        drawing.append((path.path(path.moveto(4*SCALE,y*4*SCALE),
                                  path.lineto(8*WIDTH*SCALE,y*4*SCALE)), BASE+ULTRATHICK))

    for x in range(4, 8*WIDTH, 8):
        for y in range(4, 8*HEIGHT, 8):

            drawing.append((path.path(path.moveto((x+1)*SCALE, (y+0)*SCALE),
                                      path.lineto((x+3)*SCALE, (y+4)*SCALE)), BASE+ULTRATHICK))    
            drawing.append((path.path(path.moveto((x+0)*SCALE, (y+3)*SCALE),
                                      path.lineto((x+4)*SCALE, (y+1)*SCALE)), BASE+ULTRATHICK))
            if x+7 < 8*WIDTH:
                drawing.append((path.path(path.moveto((x+7)*SCALE, (y+0)*SCALE),
                                          path.lineto((x+5)*SCALE, (y+4)*SCALE)), BASE+ULTRATHICK))
                drawing.append((path.path(path.moveto((x+4)*SCALE, (y+1)*SCALE),
                                          path.lineto((x+8)*SCALE, (y+3)*SCALE)), BASE+ULTRATHICK))
            if y+7 < 8*HEIGHT:
                drawing.append((path.path(path.moveto((x+0)*SCALE, (y+5)*SCALE),
                                          path.lineto((x+4)*SCALE, (y+7)*SCALE)), BASE+ULTRATHICK))                                      
                drawing.append((path.path(path.moveto((x+3)*SCALE, (y+4)*SCALE),
                                          path.lineto((x+1)*SCALE, (y+8)*SCALE)), BASE+ULTRATHICK))    
            if x+7 < 8*WIDTH and y+7 < 8*HEIGHT:
                drawing.append((path.path(path.moveto((x+5)*SCALE, (y+4)*SCALE),
                                          path.lineto((x+7)*SCALE, (y+8)*SCALE)), BASE+ULTRATHICK))
                drawing.append((path.path(path.moveto((x+4)*SCALE, (y+7)*SCALE),
                                          path.lineto((x+8)*SCALE, (y+5)*SCALE)), BASE+ULTRATHICK))                                      

    drawing.append((path.path(path.moveto(4*SCALE,      4*SCALE),
                              path.lineto(8*WIDTH*SCALE,4*SCALE),
                              path.lineto(8*WIDTH*SCALE,8*HEIGHT*SCALE),
                              path.lineto(4*SCALE,      8*HEIGHT*SCALE),
                              path.closepath()), BASE+ULTRATHICK))

    drawing.append((path.path(path.moveto( 6*SCALE, 4*SCALE),
                              path.lineto(30*SCALE,16*SCALE)), BASE+COLOR(BLACK)+DOTTED))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure023f():
    '''Cairo Tiling'''

    name = "figures/figure023f"

    SCALE = 1
    
    drawing = []

    drawing.append((path.path(path.moveto( 0*SCALE, 0*SCALE),
                              path.lineto( 2*SCALE, 0*SCALE),
                              path.lineto( 2*SCALE, 4*SCALE),
                              path.lineto( 0*SCALE, 4*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto( 2*SCALE, 2*SCALE),
                              path.lineto( 6*SCALE, 2*SCALE),
                              path.lineto( 6*SCALE, 6*SCALE),
                              path.lineto( 2*SCALE, 6*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto( 6*SCALE, 4*SCALE),
                              path.lineto(10*SCALE, 4*SCALE),
                              path.lineto(10*SCALE, 8*SCALE),
                              path.lineto( 6*SCALE, 8*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(10*SCALE, 6*SCALE),
                              path.lineto(14*SCALE, 6*SCALE),
                              path.lineto(14*SCALE,10*SCALE),
                              path.lineto(10*SCALE,10*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(14*SCALE, 8*SCALE),
                              path.lineto(18*SCALE, 8*SCALE),
                              path.lineto(18*SCALE,12*SCALE),
                              path.lineto(14*SCALE,12*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(18*SCALE,10*SCALE),
                              path.lineto(22*SCALE,10*SCALE),
                              path.lineto(22*SCALE,12*SCALE),
                              path.lineto(18*SCALE,12*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))

    drawing.append((path.path(path.moveto( 4*SCALE, 0*SCALE),
                              path.lineto( 8*SCALE, 0*SCALE),
                              path.lineto( 8*SCALE, 2*SCALE),
                              path.lineto( 4*SCALE, 2*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto( 8*SCALE, 0*SCALE),
                              path.lineto(12*SCALE, 0*SCALE),
                              path.lineto(12*SCALE, 4*SCALE),
                              path.lineto( 8*SCALE, 4*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(12*SCALE, 2*SCALE),
                              path.lineto(16*SCALE, 2*SCALE),
                              path.lineto(16*SCALE, 6*SCALE),
                              path.lineto(12*SCALE, 6*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(16*SCALE, 4*SCALE),
                              path.lineto(20*SCALE, 4*SCALE),
                              path.lineto(20*SCALE, 8*SCALE),
                              path.lineto(16*SCALE, 8*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(20*SCALE, 6*SCALE),
                              path.lineto(24*SCALE, 6*SCALE),
                              path.lineto(24*SCALE,10*SCALE),
                              path.lineto(20*SCALE,10*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(24*SCALE, 8*SCALE),
                              path.lineto(28*SCALE, 8*SCALE),
                              path.lineto(28*SCALE,12*SCALE),
                              path.lineto(24*SCALE,12*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))

    drawing.append((path.path(path.moveto(14*SCALE, 0*SCALE),
                              path.lineto(18*SCALE, 0*SCALE),
                              path.lineto(18*SCALE, 2*SCALE),
                              path.lineto(14*SCALE, 2*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(18*SCALE, 0*SCALE),
                              path.lineto(22*SCALE, 0*SCALE),
                              path.lineto(22*SCALE, 4*SCALE),
                              path.lineto(18*SCALE, 4*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(22*SCALE, 2*SCALE),
                              path.lineto(26*SCALE, 2*SCALE),
                              path.lineto(26*SCALE, 6*SCALE),
                              path.lineto(22*SCALE, 6*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(26*SCALE, 4*SCALE),
                              path.lineto(28*SCALE, 4*SCALE),
                              path.lineto(28*SCALE, 8*SCALE),
                              path.lineto(26*SCALE, 8*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))

    drawing.append((path.path(path.moveto(24*SCALE, 0*SCALE),
                              path.lineto(28*SCALE, 0*SCALE),
                              path.lineto(28*SCALE, 2*SCALE),
                              path.lineto(24*SCALE, 2*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))

    drawing.append((path.path(path.moveto( 0*SCALE, 6*SCALE),
                              path.lineto( 4*SCALE, 6*SCALE),
                              path.lineto( 4*SCALE,10*SCALE),
                              path.lineto( 0*SCALE,10*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto( 4*SCALE, 8*SCALE),
                              path.lineto( 8*SCALE, 8*SCALE),
                              path.lineto( 8*SCALE,12*SCALE),
                              path.lineto( 4*SCALE,12*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto( 8*SCALE,10*SCALE),
                              path.lineto(12*SCALE,10*SCALE),
                              path.lineto(12*SCALE,12*SCALE),
                              path.lineto( 8*SCALE,12*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))

    drawing.append((path.path(path.moveto( 0*SCALE,10*SCALE),
                              path.lineto( 2*SCALE,10*SCALE),
                              path.lineto( 2*SCALE,12*SCALE),
                              path.lineto( 0*SCALE,12*SCALE),
                              path.closepath()), BASE+ULTRATHICK+FILLED(ORANGE)))


    for x in range(1,28):
        drawing.append((path.path(path.moveto(x*SCALE, 0*SCALE),
                                  path.lineto(x*SCALE,12*SCALE)), BASE+THIN+DOTTED))
    for y in range(1,12):
        drawing.append((path.path(path.moveto( 0*SCALE,y*SCALE),
                                  path.lineto(28*SCALE,y*SCALE)), BASE+THIN+DOTTED))
    
    drawing.append((path.path(path.moveto( 0*SCALE, 2*SCALE),
                              path.lineto( 1*SCALE, 0*SCALE),
                              path.moveto( 0*SCALE,12*SCALE),
                              path.lineto( 6*SCALE, 0*SCALE),
                              path.moveto( 5*SCALE,12*SCALE),
                              path.lineto(11*SCALE, 0*SCALE),
                              path.moveto(10*SCALE,12*SCALE),
                              path.lineto(16*SCALE, 0*SCALE),
                              path.moveto(15*SCALE,12*SCALE),
                              path.lineto(21*SCALE, 0*SCALE),
                              path.moveto(20*SCALE,12*SCALE),
                              path.lineto(26*SCALE, 0*SCALE),
                              path.moveto(25*SCALE,12*SCALE),
                              path.lineto(28*SCALE, 6*SCALE),
                              path.moveto( 0*SCALE, 7*SCALE),
                              path.lineto(10*SCALE,12*SCALE),
                              path.moveto( 0*SCALE, 2*SCALE),
                              path.lineto(20*SCALE,12*SCALE),
                              path.moveto( 6*SCALE, 0*SCALE),
                              path.lineto(28*SCALE,11*SCALE),
                              path.moveto(16*SCALE, 0*SCALE),
                              path.lineto(28*SCALE, 6*SCALE),
                              path.moveto(26*SCALE, 0*SCALE),
                              path.lineto(28*SCALE, 1*SCALE)), BASE+ULTRATHICK))

    drawing.append((path.path(path.moveto( 0*SCALE, 0*SCALE),
                              path.lineto(28*SCALE, 0*SCALE),
                              path.lineto(28*SCALE,12*SCALE),
                              path.lineto( 0*SCALE,12*SCALE),
                              path.closepath()), BASE+ULTRATHICK))

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
    figure000f()
    figure001a()
    figure001aa()
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
    figure004n()
    figure004o()
    figure004p()
    figure004q()
    figure004r()
    figure004s()
    figure005a()
    figure005b()
    figure005c()
    figure005d()
    figure005e()
    figure005f()
    figure005g()
    figure006a()
    figure006b()
    figure006c()
    figure006d()
    figure006e()
    figure006f()
    figure006g()
    figure006h()
    figure006i()
    figure006j()
    figure006k()
    figure006l()
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
    figure009j()
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
    figure010n()
    figure010o()
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
    figure012aa()
    figure012ab()
    figure012ac()
    figure012ad()
    figure012ae()
    figure012af()
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
    figure013t()
    figure013u()
    figure013v()
    figure013w()
    figure013x()
    figure013y()
    figure013z()
    figure013zz()
    figure013aa()
    figure013ab()
    figure013ac()
    figure013ad()
    figure013ae()
    figure013af()
    figure013ag()
    figure013ah()
    figure013ai()
    figure013aj()
    figure013ak()
    figure013al()
    figure013am()
    figure013an()
    figure013ao()
    figure013ba()
    figure013bb()
    figure013bc()
    figure013bd()
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
    figure016cg()
    figure016ch()
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
    figure018ae()
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
    figure019ae()
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
    figure021()
    figure022a()
    figure022b()
    figure022c()
    figure023a()
    figure023b()
    figure023c()
    figure023d()
    figure023e()
    figure023f()

    ffigura001()
    ffigura002a()
    ffigura002b()
    ffigura003a()
    ffigura003b()
    ffigura003c()
    ffigura003d()
    ffigura003e()
    ffigura003f()
    ffigura003g()
    ffigura003h()
    ffigura003i()
    ffigura003j()
    ffigura003k()
    ffigura003l()
    ffigura003m()
    ffigura004a()
    ffigura004b()
    ffigura004c()
    ffigura004d()
    ffigura005a()
    ffigura005b()
    ffigura006a()
    ffigura006b()
    ffigura006c()
    ffigura007a()
    ffigura007b()
    ffigura007c()
    ffigura008a()
    ffigura008b()
    ffigura008c()
    ffigura008d()
    ffigura009a()
    ffigura009b()
    ffigura010a()
    ffigura010b()
    ffigura010c()
    ffigura011a()
    ffigura011b()
    ffigura012a()
    ffigura012b()
    ffigura012c()
    ffigura012d()
    ffigura012e()
    ffigura013()
    ffigura013a()
    ffigura013b()
    ffigura013c()
    ffigura013d()
    ffigura013e()
    ffigura014()
    ffigura015a()
    ffigura015b()
    ffigura015c()
    ffigura015d()
    ffigura015e()
    ffigura016a()
    ffigura016b()
    ffigura016c()
    ffigura016d()
    ffigura016e()
    ffigura016f()
    ffigura016g()
    ffigura017()
    ffigura017b()
    ffigura018a()
    ffigura018b()
    ffigura019()
    ffigura019b()
    ffigura020a()
    ffigura020b()
    ffigura020c()
    ffigura020d()
    ffigura020e()
    ffigura020f()
    ffigura020g()
    ffigura020h()
    ffigura020i()
    ffigura020j()
    ffigura020k()
    ffigura020l()
    ffigura020m()
    ffigura021a()
    ffigura021b()
    ffigura021c()
    ffigura022a()
    ffigura022b()
    ffigura022c()
    ffigura022d()
    ffigura022e()
    ffigura022f()
    ffigura022g()
    ffigura022h()
    ffigura022i()
    ffigura022j()
    ffigura022k()
    ffigura022l()
    ffigura022m()
    ffigura022n()
    ffigura022o()
    ffigura022p()
    ffigura022q()
    ffigura022r()
    ffigura022s()
    ffigura022t()
    ffigura022u()
    ffigura022v()
    ffigura022w()
    ffigura022x()
    ffigura023a()
    ffigura023b()
    ffigura023c()
    ffigura023d()
    ffigura023e()
    ffigura023f()
    ffigura023g()
    ffigura023h()
    ffigura023i()
    ffigura024a()
    ffigura024b()
    ffigura024c()
    ffigura024d()
    ffigura024e()
    ffigura024f()
    ffigura025a()
    ffigura025b()
    ffigura025c()
    ffigura025d()
    ffigura025e()
    ffigura025f()
    ffigura026a()
    ffigura026b()
    ffigura028a()
    ffigura028b()
    ffigura030a()
    ffigura030b()
    ffigura030c()
    ffigura030d()
    ffigura031() 
