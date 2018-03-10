import pandas as pd

# Execution python -c 'import panda; panda.convertsql(1)'

def convertsql(dataType):
    
    wb = (pd.read_clipboard())
    print(type(wb))
    print(wb.iloc[0])
    print(type(wb.iloc[0]))

    data = []
    print(data)
    data.insert(0,2131321)
    print(data)

    pd.concat([pd.DataFrame(data),wb], ignore_index=True)


    print(wb)
    
    #print(list(wb.index)[0])
    #print(wb.parse(1))

    #print(wb.pd.DataFrame(index=2))
    #print(type(wb))


    

