import numpy
import pandas
myarray =numpy.array([[1,2,3],[4,5,6]])
rownames = ['a','b']
colnames =['one','two','three']
mydataFrame= pandas.DataFrame(myarray,index=rownames,columns=colnames)
print(mydataFrame)
