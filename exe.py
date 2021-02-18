z = df["Female"]
r = df["Education"]
plt.pie(z,labels = r,explode = (0.3,0.3,0.3,0.3,0.3,0.5,0.5,0.5,0.5),startangle = 60)
figsize = plt.figure(figsize = (10,7))
plt.show()

dict1 = {"Education":["Not Literate","Below Primary","Primary","Middle","Secondary","Higher Secondary","Diploma","Graduate","Postgraduate"],
        "Male":[234,98,154,192,138,75,14,68,21],
        "Female":[529,93,128,110,54,27,7,31,15]}
import pandas as pd
ed = pd.DataFrame(dict1)
print(ed)

listA = [234,98,154,192,138,75,14,68,21]
listB = [529,93,128,110,54,27,7,31,15]
listA_R = [1,5,3,2,4,6,9,7,8]
listB_R = [1,4,2,3,5,7,9,6,8]
listC = []
for i in range(len(listA)):
    listC.append(listA_R[i] - listB_R[i])
    dict1 = {"Education":["Not Literate","Below Primary","Primary","Middle","Secondary","Higher Secondary","Diploma","Graduate","Postgraduate"],
            "Male":listA,
            "Rank_M":listA_R,
            "Female":listB,
            "Rank_F":listB_R,
            "d": listC}
    
import pandas as pd
ed = pd.DataFrame(dict1)
print(ed)

df.plot(kind = "barh", x = "Education" , y = "Male",figsize = (9,5),width = 0.7,color = "Magenta", alpha = 0.5)
plt.show()

#import library
import numpy as np
import math

#values of the formula
sam_prop = np.round(mean,2)
pop_prop = int(input("Tell me your hypothesis population proportion(P) --> "))
n = len(lt["State"])

#z_alpha calculated from the table
zα = float(input("Tell me your Z-alpha(zα) --> "))

#formula 
z = (sam_prop - pop_prop)/math.sqrt((pop_prop*(100 - pop_prop))/n)
print("The value of Z is --> ",np.round(z,3))

#comparing the value of calculated z with z_alpha
if(float(z) < zα/2):
    print("Since z is less than zα we will reject the null hypothesis")
else:
    print("Since z is greater than zα we failed to reject the null hypothesis")

A = lt.iloc[:,1:].to_numpy().reshape(17,4)
print("Matrix : ")
print(A)

rank1 = np.linalg.matrix_rank(A)
print("The rank is --> ",rank1)

eig = np.linalg.eig(A)
print("The eign value --> ",eig)

import matplotlib.pyplot as plt

lit.plot(kind="bar",x = "State",y = "01 to 2011(%)",figsize=(15,7),color="cyan",title="Literacy rate in India from 2001 to 2011",width=0.5)
plt.xlabel("States of India")
plt.ylabel("Range of literacy rate")
plt.show()