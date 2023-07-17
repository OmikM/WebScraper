import pandas as pd

df = pd.read_csv('data.csv')

while True:
    opt = int(input("type option: \n 1 - delate user \n 2 - add user \n 3 - print df \n 4 - to escape and save \n"))
    if opt ==1:
        Name = input("type name: ")
        i = df[df['Name'] == Name].index[0]
        df = df.drop(i)
        
    elif opt ==2:
        row = [0]*3
        row.insert(0,input("Name: "))
        row.insert(1,input("url: "))
        a = input("email (dont type enything if you dont want to recive emails)): ")
        if a=="":
            row.append(None)
        else:
            row.append(a)
        print(df.columns)
        print(row)
        df.loc[df.index.max() + 1] = row

    elif opt == 3:
        print(df)
    elif opt==4:
        break
df.to_csv('data.csv', index=False)