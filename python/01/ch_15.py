"""Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
Your printTable() function would print the following:


  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose"""

def printTable(table_data):
    col_widths = []
    for row in table_data:
      col_widths.append(len(max(row, key=len)))
    # print(col_widths)
    tx =[[row[i] for row in table_data] for i in range (len(table_data[0]))]
    # print (tx)
    
    for row in tx:
      res = ""
      for i,item in enumerate(row):
        res += item.rjust(col_widths[i]) + " "
      print(res)
    print()

table_data_01 = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(table_data_01)


