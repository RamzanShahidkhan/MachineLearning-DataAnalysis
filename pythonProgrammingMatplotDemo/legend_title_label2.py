import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]
x1 =[1,2,3]
y1 =[10,14,12]

plt.plot(x,y, label="First Line")
plt.plot(x1,y1, label ="Second Line")
plt.xlabel('Plot Numbers')
plt.ylabel('important var')
plt.title("Interesting Graph\n check it out")
plt.legend()

plt.show()