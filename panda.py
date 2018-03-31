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

def convertsql():
    wb = (pd.read_clipboard(header=None).values)

    if wb.dtype == 'int64':
        for x in wb:
            print(x,"test")

    elif wb.dtype == 'str':
            for x in wb:
                print("test",x,"test")
    else:
        print('This is not a valid SQL type.')
        return None
            
        #print(wb.values)

    

