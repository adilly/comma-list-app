import pandas as pd

# Execution python -c 'import panda; panda.convertsql()'
"""
100010
20
452
1245
45254
24245
"""
"""
test1
test2
"""

def convertsql():
    wb = (pd.read_clipboard(header=None).values)
    count = 1
    if wb.dtype == 'int64':
        for x in wb:
            if count < len(wb):
                print(int(str(x).replace("[","").replace("]","")),",")
                count+=1
            else :
                print(int(str(x).replace("[","").replace("]","")))
    elif wb.dtype == 'object':
            for x in wb:
                print(int(x.replace("[","").replace("]","")),",")
    else:
        print('This is not a valid SQL type.')
        return None
            
        #print(wb.values)

    

