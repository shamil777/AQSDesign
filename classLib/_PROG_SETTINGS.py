import pya
from math import sqrt, cos, sin, atan2, pi, copysign
from pya import Point,DPoint,DSimplePolygon,SimplePolygon, DPolygon, Polygon,  Region
from pya import Trans, DTrans, CplxTrans, DCplxTrans, ICplxTrans

class PROGRAM:
    LAYER1_NUM = 70
    LAYER2_NUM = 80
    ARC_PTS_N = 20


class LAYERS:
    photo = pya.LayerInfo(0, 0, "photo")
    ebeam = pya.LayerInfo(2, 0, "ebeam")
    photo_neg = pya.LayerInfo(9, 0, "photo_neg")
    crystal = pya.LayerInfo(8, 0, "crystal")
    bridge_patches = pya.LayerInfo(20, 0, "bridge_patches")
    bridges = pya.LayerInfo(30, 0, "bridges")

  
class CHIP:
    dx = 10.1e6
    dy = 5.1e6
    L1 = 2466721
    gap = 150e3
    width = 260e3
    b = 2*gap + width
    origin = DPoint( 0,0 )
    box = pya.DBox( origin, origin + DPoint( dx,dy ) )
    # only 4 connections programmed by now
    connections = [box.p1 + DPoint( L1 + b/2,0 ), box.p1 + DPoint( dx - (L1+b/2),0 ), box.p2 - DPoint( L1 + b/2,0 ),  box.p1 + DPoint( L1 + b/2, dy )]

       
        

            
            








