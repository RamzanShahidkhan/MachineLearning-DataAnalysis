import matplotlib.pyplot as plt

# histogram
population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,
                   115,112,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages,bins,histtype='bar', rwidth=0.6, label='histogram')
#ids =[ x for x in range(len(population_ages))]
#plt.bar(ids,population_ages)
"""
#bar chart graph
x = [2,4,6,8,10]
y = [6,7,8,2,4]
x1 =[1,3,5,9,11]
y1 =[7,8,2,4,2]

plt.bar(x,y, label='Bar1', color='r')
plt.bar(x1,y1, label="Bar2", color='c')

"""
plt.xlabel('x')
plt.ylabel('y')
plt.title("Interesting Graph\n check it out")
plt.legend()
plt.show()