# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:12:53 2017

@author: npanwar
"""
from PROC_SQL import join
from joinMerge import *
from transpose import *
table1= 'A'
table2= 'B'
column1= 'ID1'
column2= 'ID2'
#'union,intersect,minus,transpose'

#x=tableJoins(table1, table2, join, column1, column2)
#print x

#x=sortData(table1,column1)
#print x

#x=joinTable(table1,column1,'merge',table2)
#print x
#x=joinTable(table1,column1,'innerJoin',table2)
#print x
#x=joinTable(table1,column1,'rightJoin',table2)
#print x
#x=joinTable(table1,column1,'fullJoin',table2)
#print x
#x=transposeTable(table1)
#print x
#x= join.joinTables(table1,column1,'inner join',table2,column2,'newTable')
#print x
#x= join.joinTables(table1,column1,'left join',table2,column2,'newTable')
#print x
#x= join.joinTables(table1,column1,'right join',table2,column2,'newTable')
#print x
x= join.unionTables(table1,table2,'UNION','newTable')
print x
x= join.unionTables(table1,table2,'UNION ALL','newTable')
print x
x= join.intersectTables(table1,table2,'INTERSECT','newTable')
print x

