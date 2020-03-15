#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
#
# Generador de figures vectorials per l'article:
#
#       "El Tangram Egipci: Diari de Disseny"
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
THIN       = [style.linewidth.normal]
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
                              path.lineto(*C)), BASE+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E)), BASE+THIN))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F)), BASE+THIN))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.lineto(*D)), BASE+THIN))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I)), BASE+THIN))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THIN))

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
                              path.closepath()), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK))
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
                              path.closepath()), BASE+THICK))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*J),
                              path.lineto(*H),
                              path.closepath()), BASE+THICK))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*H),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK))
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
                              path.closepath()), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK))
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

################################################################################

if __name__ == "__main__":

    figura017()
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
