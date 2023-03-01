from matplotlib import pyplot as plt

# Define the features and classes
features = [[1,1],[3,1],[2,2],[4,2],[2,1],[4,1],[5,1],[6,1],[7,1],[8,1],[1,2],[3,2],[5,2],[6,2],[7,2],[8,2]]
classes = ['T','T','T','T','S','S','S','S','S','S','S','S','S','S','S','S']

# plot the points 
for feature,clas in zip(features,classes):
    if clas == 'T':
        plt.scatter(feature[0],feature[1],color = 'red')
    else:
        plt.scatter(feature[0],feature[1],color = 'blue')

#add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Triangle and square classes")

#show the plot
plt.show()