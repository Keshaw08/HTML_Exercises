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