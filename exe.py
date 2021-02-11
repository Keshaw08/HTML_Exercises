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