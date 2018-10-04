#!/usr/bin/python3
from sklearn import tree

#apple_smooth = 0 and orange_bumpy = 1

#features of fruit --  [weight,texture]
features=[[130,0],[120,0],[110,0],[100,0],[140,0],[145,1],[150,1],[160,1],[170,1],[180,1]]

labels=[0,0,0,0,0,1,1,1,1,1,1]

#calling DecisionTreeClassifier function

clf=tree.DecisionTreeClassifier()
output=clf.fit(features,labels)

#testing data
print (output.predict[[130,0]])


