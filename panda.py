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
    for x in wb:
        print(isinstance(x,str))
        print(type(x))
        print(x,"test")
    """ elif isinstance(wb,int):
        for x in wb:
            print("test",x,"test")
        return
    else:
        print('This is not a valid SQL type.')
        return None """
        
    #print(wb.values)

    

