#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
#
# Generador de figures vectorials per la xerrada:
#
#       "Parlem de Tangrams"
#
# Autor: Carlos Luna Mota
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

# GLOBAL VARIABLES
USE_GREYSCALE = False   # Use True if you want greyscale figures

# LINE STYLES
BASE       = [style.linewidth.THick, style.linestyle.solid, style.linecap.round, style.linejoin.round, color.grey.black]
THIN       = [style.linewidth.Thick]
THICK      = [style.linewidth.THIck]
SOLID      = [style.linestyle.solid]
DASHED     = [style.linestyle.dashed]
DOTTED     = [style.linestyle.dotted]
DASHDOTTED = [style.linestyle.dashdotted]

# COLOR PALETTE
WHITE    = color.gray.white
BLACK    = color.grey.black
GREY     = color.grey(0.9)
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

def FILLED(color):
    if color == BLACK: return [deco.filled([BLACK])]
    elif USE_GREYSCALE: return [deco.filled([GREY])]
    else: return [deco.filled([color])]
def COLOR(color):
    if color == BLACK: return [BLACK]
    elif USE_GREYSCALE: return [DARKGREY]
    else: return [color]

# AUXILIARY FUNCTIONS
def w_point((x1,x2), (y1,y2), Wx, Wy): return ((Wx*x1+Wy*y1)/(Wx+Wy), (Wx*x2+Wy*y2)/(Wx+Wy))
def s_point((x1,x2), (y1,y2), W): return ((W*(y1-x1))+y1 , (W*(y2-x2))+y2)

################################################################################

# FIGURES
def figura001():
    '''Tangram Xinés'''

    name = "figures/figura001"

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
    mycanvas.writeEPSfile(name)

def figura002a():
    '''Silueta Realista'''

    name = "figures/figura002a"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura002b():
    '''Silueta Realista (solución)'''

    name = "figures/figura002b"

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
    mycanvas.writeEPSfile(name)

def figura003a():
    '''Tangram Xinés - Figura Convexa 1'''

    name = "figures/figura003a"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura003b():
    '''Tangram Xinés - Figura Convexa 2'''

    name = "figures/figura003b"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura003c():
    '''Tangram Xinés - Figura Convexa 3'''

    name = "figures/figura003c"

    X = 1.0 # Scale !
    A = (     0,      0)
    B = (2*R2*X, 2*R2*X)
    C = (4*R2*X,      0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura003d():
    '''Tangram Xinés - Figura Convexa 4'''

    name = "figures/figura003d"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura003e():
    '''Tangram Xinés - Figura Convexa 5'''

    name = "figures/figura003e"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura003f():
    '''Tangram Xinés - Figura Convexa 6'''

    name = "figures/figura003f"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura003g():
    '''Tangram Xinés - Figura Convexa 7'''

    name = "figures/figura003g"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura003h():
    '''Tangram Xinés - Figura Convexa 8'''

    name = "figures/figura003h"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura003i():
    '''Tangram Xinés - Figura Convexa 9'''

    name = "figures/figura003i"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura003j():
    '''Tangram Xinés - Figura Convexa 10'''

    name = "figures/figura003j"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura003k():
    '''Tangram Xinés - Figura Convexa 11'''

    name = "figures/figura003k"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura003l():
    '''Tangram Xinés - Figura Convexa 12'''

    name = "figures/figura003l"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura003m():
    '''Tangram Xinés - Figura Convexa 13'''

    name = "figures/figura003m"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura004a():
    '''Paradoxa Triangle Complet'''

    name = "figures/figura004a"

    X = R2
    A = (  0,  0)
    B = (4*X,  0)
    C = (2*X,2*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura004b():
    '''Paradoxa Triangle Incomplet'''

    name = "figures/figura004b"

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
                              path.closepath()), BASE+FILLED(BLACK)))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura004c():
    '''Paradoxa Triangle Complet Solució'''

    name = "figures/figura004c"

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
    mycanvas.writeEPSfile(name)

def figura004d():
    '''Paradoxa Triangle Incomplet Solució'''

    name = "figures/figura004d"

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
    mycanvas.writeEPSfile(name)

def figura005a():
    '''Dissecció quadrat-dodecagon: quadrat'''

    name = "figures/figura005a"

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
    mycanvas.writeEPSfile(name)

def figura005b():
    '''Dissecció quadrat-dodecagon: dodecagon'''

    name = "figures/figura005b"

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
    mycanvas.writeEPSfile(name)

def figura006a():
    '''Tangram Japonés'''

    name = "figures/figura006a"

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
    mycanvas.writeEPSfile(name)

def figura006b():
    '''Tangram Double Square'''

    name = "figures/figura006b"

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
    mycanvas.writeEPSfile(name)

def figura006c():
    '''Tangram Fletcher'''

    name = "figures/figura006c"

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
    mycanvas.writeEPSfile(name)

def figura007a():
    '''Tangram de V & Diamond'''

    name = "figures/figura007a"

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
    mycanvas.writeEPSfile(name)

def figura007b():
    '''Tangram de Brügner'''

    name = "figures/figura007b"

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
    mycanvas.writeEPSfile(name)

def figura007c():
    '''Tangram de Pitagoric'''

    name = "figures/figura007c"

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
    mycanvas.writeEPSfile(name)

def figura008a():
    '''Tangram de l'Ou'''

    name = "figures/figura008a"

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
    mycanvas.writeEPSfile(name)

def figura008b():
    '''Tangram del Cor'''

    name = "figures/figura008b"

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
    mycanvas.writeEPSfile(name)

def figura008c():
    '''Tangram Circular 1'''

    name = "figures/figura008c"

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
    mycanvas.writeEPSfile(name)

def figura008d():
    '''Tangram Circular 2'''

    name = "figures/figura008d"

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
    mycanvas.writeEPSfile(name)

def figura009a():
    '''Tangram de Brügner'''

    name = "figures/figura009a"

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
    mycanvas.writeEPSfile(name)

def figura009b():
    '''Ostomachion'''

    name = "figures/figura009b"

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
    mycanvas.writeEPSfile(name)

def figura010a():
    '''Subtangram Xinés'''

    name = "figures/figura010a"

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
    mycanvas.writeEPSfile(name)

def figura010b():
    '''Tangram de la Creu'''

    name = "figures/figura010b"

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
    mycanvas.writeEPSfile(name)

def figura010c():
    '''Tangram dels Cinc Triangles'''

    name = "figures/figura010c"

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
    mycanvas.writeEPSfile(name)

def figura011a():
    '''Pentominos'''

    name = "figures/figura011a"

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
    mycanvas.writeEPSfile(name)

def figura011b():
    '''Hexamants'''

    name = "figures/figura011b"

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
    mycanvas.writeEPSfile(name)

def figura012a():
    '''Subtangram Xinés - Costats inconmensurables'''

    name = "figures/figura012a"

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
    mycanvas.writeEPSfile(name)

def figura012b():
    '''Tangram de la Creu - Costats inconmensurables'''

    name = "figures/figura012b"

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
    mycanvas.writeEPSfile(name)

def figura012c():
    '''Tangram dels cinc triangles - Costats inconmensurables'''

    name = "figures/figura012c"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(B, C, 1,1)
    F = w_point(A, C, 1,1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*D)), BASE+THICK+COLOR(color.rgb.blue)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*D)), BASE+THICK+COLOR(RED)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*A),
                              path.lineto(*B),
                              path.lineto(*E)), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura013a():
    '''Subtangram Xinés - Retícules'''

    name = "figures/figura013a"

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
    mycanvas.writeEPSfile(name)

def figura013b():
    '''Tangram de la Creu - Retícula'''

    name = "figures/figura013b"

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
    mycanvas.writeEPSfile(name)

def figura013c():
    '''Tangram dels cinc triangles - Retícula'''

    name = "figures/figura013c"

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
    mycanvas.writeEPSfile(name)

def figura014():
    '''Quadrat amb un Tall'''

    name = "figures/figura014"

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
    mycanvas.writeEPSfile(name)

def figura015a():
    '''Tangram de dues peces - Quadrat'''

    name = "figures/figura015a"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura015b():
    '''Tangram de dues peces - Trapezi'''

    name = "figures/figura015b"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura015c():
    '''Tangram de dues peces - Paralelogram'''

    name = "figures/figura015c"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura015d():
    '''Tangram de dues peces - Triangle'''

    name = "figures/figura015d"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (2*X,0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura015e():
    '''Tangram de dues peces - Quadrilater'''

    name = "figures/figura015e"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura016a():
    '''Quadrat amb dos Talls 1'''

    name = "figures/figura016a"

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
    mycanvas.writeEPSfile(name)

def figura016b():
    '''Quadrat amb dos Talls 2'''

    name = "figures/figura016b"

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
    mycanvas.writeEPSfile(name)

def figura016c():
    '''Quadrat amb dos Talls 3'''

    name = "figures/figura016c"

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
    mycanvas.writeEPSfile(name)

def figura016d():
    '''Quadrat amb dos Talls 1 - retícula'''

    name = "figures/figura016d"

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
    mycanvas.writeEPSfile(name)

def figura016e():
    '''Quadrat amb dos Talls 2 - retícula'''

    name = "figures/figura016e"

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
    mycanvas.writeEPSfile(name)

def figura016f():
    '''Quadrat amb dos Talls 3 - retícula'''

    name = "figures/figura016f"

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
    mycanvas.writeEPSfile(name)

def figura016g():
    '''Quadrat amb dos Talls 2 - retícula sense color'''

    name = "figures/figura016g"

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
    mycanvas.writeEPSfile(name)

def figura017():
    '''El Tangram Egípci'''

    name = "figures/figura017"

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
    mycanvas.writeEPSfile(name)

def figura017b():
    '''El Tangram Egípci'''

    name = "figures/figura017b"

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
    mycanvas.writeEPSfile(name)

def figura018a():
    '''El Tangram Egípci - Decomposat'''

    name = "figures/figura018a"

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
    mycanvas.writeEPSfile(name)

def figura018b():
    '''Tangram de la Creu - Decomposat'''

    name = "figures/figura018b"

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
    mycanvas.writeEPSfile(name)

def figura019():
    '''El Tangram Egípci - 5 cercles notables'''

    name = "figures/figura019"

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
    mycanvas.writeEPSfile(name)

def figura019b():
    '''El Tangram Egípci - El quadrilater es ciclic'''

    name = "figures/figura019b"

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
    mycanvas.writeEPSfile(name)

def figura020a():
    '''T1+Q4'''

    name = "figures/figura020a"

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
    mycanvas.writeEPSfile(name)

def figura020b():
    '''T5'''

    name = "figures/figura020b"

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
    mycanvas.writeEPSfile(name)

def figura020c():
    '''T1+T4'''

    name = "figures/figura020c"

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
    mycanvas.writeEPSfile(name)

def figura020d():
    '''T1+Q4+T5'''

    name = "figures/figura020d"

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
    mycanvas.writeEPSfile(name)

def figura020e():
    '''T4+T6'''

    name = "figures/figura020e"

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
    mycanvas.writeEPSfile(name)

def figura020f():
    '''T1+Q4+T5'''

    name = "figures/figura020f"

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
    mycanvas.writeEPSfile(name)

def figura020g():
    '''T4+T6'''

    name = "figures/figura020g"

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
    mycanvas.writeEPSfile(name)

def figura020h():
    '''T6+Q4'''

    name = "figures/figura020h"

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
    mycanvas.writeEPSfile(name)

def figura020i():
    '''T6+Q4'''

    name = "figures/figura020i"

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
    mycanvas.writeEPSfile(name)

def figura020j():
    '''T1+T4+T5+Q4'''

    name = "figures/figura020j"

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
    mycanvas.writeEPSfile(name)

def figura020k():
    '''T1+T4+T5+Q4'''

    name = "figures/figura020k"

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
    mycanvas.writeEPSfile(name)

def figura020l():
    '''T1+T4+T5+Q4'''

    name = "figures/figura020l"

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
    mycanvas.writeEPSfile(name)

def figura020m():
    '''T1+T4+T5+Q4'''

    name = "figures/figura020m"

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
    mycanvas.writeEPSfile(name)

def figura021a():
    '''El Tangram Egípci - Quadrat 1'''

    name = "figures/figura021a"

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
    mycanvas.writeEPSfile(name)

def figura021b():
    '''El Tangram Egípci - Quadrat 2'''

    name = "figures/figura021b"

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
    mycanvas.writeEPSfile(name)

def figura021c():
    '''El Tangram Egípci - Quadrat 3'''

    name = "figures/figura021c"

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
    mycanvas.writeEPSfile(name)

def figura022a():
    '''El Tangram Egípci - Figura 1'''

    name = "figures/figura022a"

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
    mycanvas.writeEPSfile(name)

def figura022b():
    '''El Tangram Egípci - Figura 2'''

    name = "figures/figura022b"

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
    mycanvas.writeEPSfile(name)

def figura022c():
    '''El Tangram Egípci - Figura 3'''

    name = "figures/figura022c"

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
    mycanvas.writeEPSfile(name)

def figura022d():
    '''El Tangram Egípci - Figura 4'''

    name = "figures/figura022d"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura022e():
    '''El Tangram Egípci - Figura 5'''

    name = "figures/figura022e"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura022f():
    '''El Tangram Egípci - Figura 6'''

    name = "figures/figura022f"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura022g():
    '''El Tangram Egípci - Figura 7'''

    name = "figures/figura022g"

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

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura022h():
    '''El Tangram Egípci - Figura 8'''

    name = "figures/figura022h"

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
    mycanvas.writeEPSfile(name)

def figura022i():
    '''El Tangram Egípci - Figura 9'''

    name = "figures/figura022i"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura022j():
    '''El Tangram Egípci - Figura 10'''

    name = "figures/figura022j"

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
    mycanvas.writeEPSfile(name)

def figura022k():
    '''El Tangram Egípci - Figura 11'''

    name = "figures/figura022k"

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
    mycanvas.writeEPSfile(name)

def figura022l():
    '''El Tangram Egípci - Figura 12'''

    name = "figures/figura022l"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura022m():
    '''El Tangram Egípci - Figura 13'''

    name = "figures/figura022m"

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
    mycanvas.writeEPSfile(name)

def figura022n():
    '''El Tangram Egípci - Figura 14'''

    name = "figures/figura022n"

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

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura022o():
    '''El Tangram Egípci - Figura 15'''

    name = "figures/figura022o"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura022p():
    '''El Tangram Egípci - Figura 16'''

    name = "figures/figura022p"

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

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura022q():
    '''El Tangram Egípci - Figura 17'''

    name = "figures/figura022q"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura022r():
    '''El Tangram Egípci - Figura 18'''

    name = "figures/figura022r"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura022s():
    '''El Tangram Egípci - Figura 19'''

    name = "figures/figura022s"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura022t():
    '''El Tangram Egípci - Figura 20'''

    name = "figures/figura022t"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura022u():
    '''El Tangram Egípci - Figura 21'''

    name = "figures/figura022u"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura022v():
    '''El Tangram Egípci - Figura 22'''

    name = "figures/figura022v"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura022w():
    '''El Tangram Egípci - Figura 23'''

    name = "figures/figura022w"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura022x():
    '''El Tangram Egípci - Figura 24'''

    name = "figures/figura022x"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura023a():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figura023a"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura023b():
    '''El Subtangram Egípci - Figura 2'''

    name = "figures/figura023b"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura023c():
    '''El Subtangram Egípci - Figura 3'''

    name = "figures/figura023c"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (8*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura023d():
    '''El Subtangram Egípci - Figura 4'''

    name = "figures/figura023d"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura023e():
    '''El Subtangram Egípci - Figura 5'''

    name = "figures/figura023e"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura023f():
    '''El Subtangram Egípci - Figura 6'''

    name = "figures/figura023f"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura023g():
    '''El Subtangram Egípci - Figura 7'''

    name = "figures/figura023g"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura023h():
    '''El Subtangram Egípci - Figura 8'''

    name = "figures/figura023h"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura023i():
    '''El Subtangram Egípci - Figura 9'''

    name = "figures/figura023i"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura024a():
    '''El Tangram Egípci - Triangle 1:2'''

    name = "figures/figura024a"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,2*X)
    C = (1*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura024b():
    '''El Tangram Egípci - Triangle 2:4'''

    name = "figures/figura024b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (2*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura024c():
    '''El Tangram Egípci - Triangle sqrt(5):2*sqrt(5)'''

    name = "figures/figura024c"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (1*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura024d():
    '''El Tangram Egípci - Triangle 3:6'''

    name = "figures/figura024d"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,6*X)
    C = (3*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura024e():
    '''El Tangram Egípci - Triangle 4:8'''

    name = "figures/figura024e"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,8*X)
    C = (4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura024f():
    '''El Tangram Egípci - Triangle 2*sqrt(5):4*sqrt(5)'''

    name = "figures/figura024f"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,4*X*R5)
    C = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura025a():
    '''El Tangram Egípci - Suma de figures semblants 1'''

    name = "figures/figura025a"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura025b():
    '''El Tangram Egípci - Suma de figures semblants 2'''

    name = "figures/figura025b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (8*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura025c():
    '''El Tangram Egípci - Suma de figures semblants 3'''

    name = "figures/figura025c"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,2*X)
    C = (4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura025d():
    '''El Tangram Egípci - Suma de figures semblants 4'''

    name = "figures/figura025d"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura025e():
    '''El Tangram Egípci - Suma de figures semblants 5'''

    name = "figures/figura025e"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura025f():
    '''El Tangram Egípci - Suma de figures semblants 6'''

    name = "figures/figura025f"

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
                              path.closepath()), BASE+FILLED(BLACK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura026a():
    '''Tangram del triangle'''

    name = "figures/figura026a"

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
    mycanvas.writeEPSfile(name)

def figura026b():
    '''Tangram de l'Hexàgon'''

    name = "figures/figura026b"

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
    mycanvas.writeEPSfile(name)

def figura028a():
    '''El Puzzle Egipci'''

    name = "figures/figura028a"

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
    mycanvas.writeEPSfile(name)

def figura028b():
    '''Tangents'''

    name = "figures/figura028b"

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
    mycanvas.writeEPSfile(name)

def figura029a():
    '''Quadrilaters del Tangram Egípci - Figura 1'''

    name = "figures/figura029a"

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
    mycanvas.writeEPSfile(name)

def figura029b():
    '''Quadrilaters del Tangram Egípci - Figura 2'''

    name = "figures/figura029b"

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
    mycanvas.writeEPSfile(name)

def figura029c():
    '''Quadrilaters del Tangram Egípci - Figura 3'''

    name = "figures/figura029c"

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
    mycanvas.writeEPSfile(name)

def figura029d():
    '''Quadrilaters del Tangram Egípci - Figura 4'''

    name = "figures/figura029d"

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
    mycanvas.writeEPSfile(name)

def figura029e():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figura029e"

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
    mycanvas.writeEPSfile(name)

def figura029f():
    '''Quadrilaters del Tangram Egípci - Figura 6'''

    name = "figures/figura029f"

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
    mycanvas.writeEPSfile(name)

def figura029g():
    '''Quadrilaters del Tangram Egípci - Figura 7'''

    name = "figures/figura029g"

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
    mycanvas.writeEPSfile(name)

def figura029h():
    '''Quadrilaters del Tangram Egípci - Figura 8'''

    name = "figures/figura029h"

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
    mycanvas.writeEPSfile(name)

def figura029i():
    '''Quadrilaters del Tangram Egípci - Figura 9'''

    name = "figures/figura029i"

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


    print BETA 
    
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)
    mycanvas.writeEPSfile(name)

def figura029j():
    '''Quadrilaters del Tangram Egípci - Figura 10'''

    name = "figures/figura029j"

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
    mycanvas.writeEPSfile(name)

def figura029k():
    '''Quadrilaters del Tangram Egípci - Figura 11'''

    name = "figures/figura029k"

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
    mycanvas.writeEPSfile(name)

def figura029l():
    '''Quadrilaters del Tangram Egípci - Figura 12'''

    name = "figures/figura029l"

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
    mycanvas.writeEPSfile(name)

def figura029m():
    '''Quadrilaters del Tangram Egípci - Figura 13'''

    name = "figures/figura029m"

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
    mycanvas.writeEPSfile(name)

def figura029n():
    '''Quadrilaters del Tangram Egípci - Figura 14'''

    name = "figures/figura029n"

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
    mycanvas.writeEPSfile(name)

def figura029o():
    '''Quadrilaters del Tangram Egípci - Figura 15'''

    name = "figures/figura029o"

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
    mycanvas.writeEPSfile(name)

def figura029p():
    '''Quadrilaters del Tangram Egípci - Figura 16'''

    name = "figures/figura029p"

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
    mycanvas.writeEPSfile(name)

def figura029q():
    '''Quadrilaters del Tangram Egípci - Figura 17'''

    name = "figures/figura029q"

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
    mycanvas.writeEPSfile(name)

def figura029r():
    '''Quadrilaters del Tangram Egípci - Figura 18'''

    name = "figures/figura029r"

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
    mycanvas.writeEPSfile(name)

def figura030a():
    '''DIDI puzzle'''

    name = "figures/figura030a"

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
    mycanvas.writeEPSfile(name)

def figura030b():
    '''Tangram dels 4 triangles iguals'''

    name = "figures/figura030b"

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
    mycanvas.writeEPSfile(name)

def figura030c():
    '''Tangram dels 4 triangles differents'''

    name = "figures/figura030c"

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
    mycanvas.writeEPSfile(name)

def figura031():
    '''T-puzzle'''

    name = "figures/figura031"

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
    mycanvas.writeEPSfile(name)

################################################################################

if __name__ == "__main__":

    figura001()
    figura002a()
    figura002b()
    figura003a()
    figura003b()
    figura003c()
    figura003d()
    figura003e()
    figura003f()
    figura003g()
    figura003h()
    figura003i()
    figura003j()
    figura003k()
    figura003l()
    figura003m()
    figura004a()
    figura004b()
    figura004c()
    figura004d()
    figura005a()
    figura005b()
    figura006a()
    figura006b()
    figura006c()
    figura007a()
    figura007b()
    figura007c()
    figura008a()
    figura008b()
    figura008c()
    figura008d()
    figura009a()
    figura009b()
    figura010a()
    figura010b()
    figura010c()
    figura011a()
    figura011b()
    figura012a()
    figura012b()
    figura012c()
    figura013a()
    figura013b()
    figura013c()
    figura014()
    figura015a()
    figura015b()
    figura015c()
    figura015d()
    figura015e()
    figura016a()
    figura016b()
    figura016c()
    figura016d()
    figura016e()
    figura016f()
    figura016g()
    figura017()
    figura017b()
    figura018a()
    figura018b()
    figura019()
    figura019b()
    figura020a()
    figura020b()
    figura020c()
    figura020d()
    figura020e()
    figura020f()
    figura020g()
    figura020h()
    figura020i()
    figura020j()
    figura020k()
    figura020l()
    figura020m()
    figura021a()
    figura021b()
    figura021c()
    figura022a()
    figura022b()
    figura022c()
    figura022d()
    figura022e()
    figura022f()
    figura022g()
    figura022h()
    figura022i()
    figura022j()
    figura022k()
    figura022l()
    figura022m()
    figura022n()
    figura022o()
    figura022p()
    figura022q()
    figura022r()
    figura022s()
    figura022t()
    figura022u()
    figura022v()
    figura022w()
    figura022x()
    figura023a()
    figura023b()
    figura023c()
    figura023d()
    figura023e()
    figura023f()
    figura023g()
    figura023h()
    figura023i()
    figura024a()
    figura024b()
    figura024c()
    figura024d()
    figura024e()
    figura024f()
    figura025a()
    figura025b()
    figura025c()
    figura025d()
    figura025e()
    figura025f()
    figura026a()
    figura026b()
    figura028a()
    figura028b()
    figura030a()
    figura030b()
    figura030c()
    figura031()    
