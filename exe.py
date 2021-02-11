z = df["Female"]
r = df["Education"]
plt.pie(z,labels = r,explode = (0.3,0.3,0.3,0.3,0.3,0.5,0.5,0.5,0.5),startangle = 60)
figsize = plt.figure(figsize = (10,7))
plt.show()