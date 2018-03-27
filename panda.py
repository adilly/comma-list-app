import pandas as pd

# Execution python -c 'import panda; panda.convertsql(1)'

def convertsql(dataType):
    wb = (pd.read_clipboard(header=None))

    for ind, values in wb.iteritems():
        print(values)

    #print(wb.values)

    

