# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 23:37:28 2017

@author: npanwar
"""

'''
Data readin;
Input ID Q1-Q3;
cards;
85 1 2 3
90 3 4 6
95 5 5 6
100 6 6 4
105 5 5 6
110 6 6 5
;

Data readin1;
Set readin;
IF ID GT 100 THEN DELETE;
run; 
WHERE CALCULATED NEWWEIGHT > 5;
'''

def transformSingleColumns(column, condition, value=None, gate=None, braces=None):
    query=''+column+' '+condition
    if value:
        query+=' '+str(value)
    if gate:
        query+=' '+gate
    if braces:  
        query+=braces
    else:
        query+=' '
    return query

def transformAllColumns(conditions):
    query=''
    for condition in conditions:
        query= query+ transformSingleColumns(condition['column'],condition['condition'],condition['value'],condition['gate'],condition['braces'])
    query+=';'
    return query