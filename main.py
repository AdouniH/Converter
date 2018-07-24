# -*- coding: utf-8 -*-
"""
@author: Houssem ADOUNI
"""

from API.converter import Point

if __name__=="__main__":
    p1=Point((0,3.5),4326)
    p2=p1.convert_to(32632)
    print p2.get_Point()
