# -*- coding: utf-8 -*-
"""
Created on Thu Aug 03 15:50:53 2017

@author: npanwar
"""

def transposeTable(table1):
    query='proc transpose data='+table1+' out=outdata;\nrun;'
    return query


