# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:12:53 2017

@author: npanwar
"""
def sortData(table1, column1):
    query='\nproc sort data = '+table1+';\nby '+column1+'; \nrun; \n'
    return query

def sampleJoin(table1,column,table2):
    query='\ndata dummy;\nmerge '+table1+' (in=x) '+table2+'(in=y);\nby '+column+';\n'
    return query

def joinTable(table1, column,join,table2):
    query= sortData(table1,column)+sortData(table2,column)+sampleJoin(table1,column,table2)
    if join=='merge':
        query=query+'if x or y;\nrun;\n'
    elif join=='innerJoin':
        query=query+'If x and y;\nrun;\n'
    elif join=='leftJoin':
        query=query+'If x;\nrun;\n'
    elif join=='rightJoin':
        query=query+'If y;\nrun;\n'
    elif join=='fullJoin':
        query=query+'run;\n'        
    return query

