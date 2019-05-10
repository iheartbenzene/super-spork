import math
import numpy as np

import drawSvg as draw
from drawSvg import Drawing
from hyperbolic import euclid, util
from hyperbolic.poincare.shapes import *
from hyperbolic.poincare import Transform
from hyperbolic.poincare.util import radialEuclidToPoincare, radialPoincareToEuclid, poincareToEuclidFactor, triangleSideForAngles
import hyperbolic.tiles as htiles

def drawTiles(drawing, tiles):
    for tile in tiles:
        d.draw(tile, hwidth=0.2, fill="white")
    for tile in tiles:
        d.draw(tile, drawVerts=True, hradius=0.3, hwidth=0.2, fill="black", opacity=0.6)

t1 = 4
t2 = 3
s = 3

theta1, theta2 = math.pi*2/t1, math.pi*2/t2
phiSum = math.pi*2/s

r1 = triangleSideForAngles((1/2)*(theta1, phiSum, theta2)
r2 = triangleSideForAngles((1/2)*(theta2, phiSum, theta1)

tile_generator1 = htiles.TileGen.makeRegular(t1, hr=r1, skip=1)
tile_generator2 = htiles.TileGen.makeRegular(t2, hr=r2, skip=1)

tile_layout = htiles.TileLayout()
tile_layout.addGenerator(tile_generator1, (1,)*t1)
tile_layout.addGenerator(tile_generator2, (0,)*t2)
starting_tile = tile_layout.defaultStartTile(rotateDeg=45)

tiles = tile_layout.tilePlane(starting_tile, depth=5)

d = Drawing(4, 4, origin='center')
d.draw(euclid.shapes.Circle(0,0,4), fill='blue')
drawTiles(d, tiles)

d.setRenderSize=(w=400)
d.saveSvg('images/tileTriangleSquare.svg')