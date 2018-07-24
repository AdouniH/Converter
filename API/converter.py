# -*- coding: utf-8 -*-
"""
@author: Houssem ADOUNI
"""

from pyproj import Proj,transform

class Point:
    def __init__(self,coord,srid_from):
        self.coord=coord
        self.srid_from=srid_from
    def get_Point(self):
        return self.coord
    def get_x(self):
        return self.coord[0]
    def get_y(self):
        return self.coord[1]
    def get_srid(self):
        return self.srid_from
    def convert_to(self,srid_to):
        p1 = Proj(init='epsg:%s'%self.srid_from)
        p2 = Proj(init='epsg:%s'%srid_to)
        x,y= transform(p1,p2,self.get_x(),self.get_y())
        return Point((x,y),srid_to)
if __name__=='__main__':
    pass