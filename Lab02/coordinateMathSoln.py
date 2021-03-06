#!/usr/bin/env python3
# Name : Jude Joseph (jajoseph)
# Group Members : none


'''
    Given triad class
'''
import math

class Triad:
    """
 
    Author: David Bernick
    Date: March 21, 2013
    This class calculates angles and distances among a triad of points.
    Points can be supplied in any dimensional space as long as they are consistent.
    Points are supplied as tupels in n-dimensions, and there should be three
    of those to make the triad. Each point is positionally named as p,q,r
    and the corresponding angles are then angleP, angleQ and angleR.
    Distances are given by dPQ(), dPR() and dQR()
 
    Required Modules: math
    initialized: 3 positional tuples representing Points in n-space
             p1 = Triad( p=(1,0,0), q=(0,0,0), r=(0,1,0) )
    attributes: p,q,r the 3 tuples representing points in N-space
    methods:  angleP(), angleR(), angleQ() angles measured in radians
          dPQ(), dPR(), dQR() distances in the same units of p,q,r
 
    """

    def __init__(self, p, q, r):
        """ Construct a Triad.  
            p1 = Triad( p=(1,0,0), q=(0,0,0), r=(0,0,0) ). 
        """
        self.p = p
        self.q = q
        self.r = r

    # private helper methods
    def d2(self, a, b):  # calculate squared distance of point a to b
        return float(sum((ia - ib) * (ia - ib) for ia, ib in zip(a, b)))

    def dot(self, a, b):  # dotProd of standard vectors a,b
        return float(sum(ia * ib for ia, ib in zip(a, b)))

    def ndot(self, a, b, c):  # dotProd of vec. a,c standardized to b
        return float(sum((ia - ib) * (ic - ib) for ia, ib, ic in zip(a, b, c)))

    # calculate lengths(distances) of segments PQ, PR and QR
    def dPQ(self):
        """ Provides the distance between point p and point q """
        return math.sqrt(self.d2(self.p, self.q))

    def dPR(self):
        """ Provides the distance between point p and point r """
        return math.sqrt(self.d2(self.p, self.r))

    def dQR(self):
        """ Provides the distance between point q and point r """
        return math.sqrt(self.d2(self.q, self.r))

    def angleP(self):
        """ Provides the angle made at point p by segments pq and pr (radians). """
        return math.acos(
            self.ndot(self.q, self.p, self.r) / math.sqrt(self.d2(self.q, self.p) * self.d2(self.r, self.p)))

    def angleQ(self):
        """ Provides the angle made at point q by segments qp and qr (radians). """
        return math.acos(
            self.ndot(self.p, self.q, self.r) / math.sqrt(self.d2(self.p, self.q) * self.d2(self.r, self.q)))

    def angleR(self):
        """ Provides the angle made at point r by segments rp and rq (radians). """
        return math.acos(
            self.ndot(self.p, self.r, self.q) / math.sqrt(self.d2(self.p, self.r) * self.d2(self.q, self.r)))

'''
Taken input and manipulate string to get coordinates in floating point number format
'''
def transformInput(coord):
    coord = coord.replace("C", "")
    coord = coord.replace("N", "")
    coord = coord.replace("a", "")
    coord = coord.replace("(", "")
    coord = coord.replace(")", "")
    coord = coord.split("=")
    coordC = coord[1].split(",")
    coordN = coord[2].split(",")
    coordCa = coord[3].split(",")

    p = (float(coordC[0]), float(coordC[1]), float(coordC[2]))
    q = (float(coordN[0]), float(coordN[1]), float(coordN[2]))
    r = (float(coordCa[0]), float(coordCa[1]), float(coordCa[2]))

    return p, q, r


def main():
    coord = input("Enter coordinates : ")
    p, q, r = transformInput(coord)
    triad = Triad(p, q, r)

    '''
    take manipulated floating point tuples and access triad class function
    appropriately 
    '''
    print("N-C bond length = {0:0.2f}".format(triad.dPQ()))
    print("N-Ca bond length = {0:0.2f}".format(triad.dQR()))
    print("C-N-Ca angle length = {0:0.1f}".format(math.degrees(triad.angleQ())))


main()
