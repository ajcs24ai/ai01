import pandas as pd
t={'course':["python","java","dbms","mma","cn"],'fee':[300,600,21,350,67],'complexity':[100,56,32,10,67]}
d=pd.DataFrame(t)
print(d)
print("\n",d.pivot(columns='course',values='complexity'))
print("\n",d.melt())