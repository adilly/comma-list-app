from openpyxl import load_workbook, workbook

def convertsql(dataType):
    #dataType from manual? 
    # Can you pull dataType based on column value? 
    wb = load_workbook("D:\Git\sql-convert-file.xlsx")
    # parm file name from clip baord
    # source from xlsx or txt or made copy command???
    ws = wb.active
    firstColumn = ws['A']

# if dataType = string 
    """ for x in range(len(firstColumn)):
        print(firstColumn[x].value) +"" """
# else dataType = number
    for x in range(len(firstColumn)):
        print(firstColumn[x].value)
# else dataType = junk
    # then junk

    

