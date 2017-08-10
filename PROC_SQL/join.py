start = 'PROC SQL;\n'
end= 'Quit;\n'

'''
minus, transpose
'''

# Fuction to fetch the table
def getTable(table,observations=None):
	query=start+'select * from '+table+';\n'+end
	return query

# Function for joining the tables
def joinTables(table1,column1,join,table2,column2,newTable=None):
        query=start+'Create table '+newTable+' as\n'+\
                    'Select * from '+table1+' as x '+join+' '+table2+' as y\nwhere '\
                    +table1+'.'+column1+'='+table2+'.'+column2+';\n'+end
        return query
    
# Function for union of two tables
def unionTables(table1,table2,union,newTable):
    query=start+'Create table '+newTable+' as\n'+\
                    'select * from '+table1+'\n'\
                    +union+'\n'\
                    +'select * from '+table2+';\n'+end
    return query

# Function for intersection of two tables
def intersectTables(table1,table2,inersect,newTable):
    query=start+'Create table '+newTable+' as\n'+\
                    'select * from '+table1+'\n'\
                    +inersect+'\n'\
                    +'select * from '+table2+';\n'+end
    return query

                    
