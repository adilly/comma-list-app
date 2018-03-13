import pandas as pd

# Execution python -c 'import panda; panda.convertsql(1)'

def convertsql(dataType):
    wb = (pd.read_clipboard())

    header = list(wb)

    #REMOVE value from list
    print(header)

    #APPEND value to dataframe
    wb.append(header)

    
    print(wb.values)

    

