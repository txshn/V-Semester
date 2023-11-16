import csv
import math
def read_data_from_csv(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append([float(row[0]), float(row[1])])
    return data

data = read_data_from_csv('data.csv')
x = [i[0] for i in data]
y = [i[1] for i in data]


def dist(center, point):
    d = 0.0
    for i in range(0, len(point)):
        d += (center[i]-point[i])**2
    return math.sqrt(d)


def assignCenters(centers, dataset):
    clusters = []
    for i in range(len(dataset)):
        distances = []
        for center in centers:
            distances.append(dist(center, dataset[i]))
        temp = [z for z, val in enumerate(distances) if val == min(distances)]
        clusters.append(temp[0])
    return clusters


def mean_center(k, dataset, clusters):
    nCenters = []
    for i in range(k):
        x = 0.0
        y = 0.0
        count = 0
        for j in range(len(clusters)):
            if (i == clusters[j]):
                x += dataset[j][0]
                y += dataset[j][1]
                count += 1
        x = x/count
        y = y/count
        nCenters.append([x, y])
    return nCenters


print("enter k")
k = int(input())
centers = []
for i in range(k):
    print("enter center "+str(i))
    temp = [int(x) for x in input().split()]
    centers.append(temp)

print("Initial centers: ")
print(centers)
print("Initial clusters: ")
clusters = assignCenters(centers, data)
for i in range(k):
    print("cluster "+str(i))
    for j in range(len(clusters)):
        if (i == clusters[j]):
            print(data[j], end=' ')
    print()
print()
for itr in range(10):
    print("Iteration "+str(itr))
    centers = mean_center(k, data, clusters)
    print("Updated centers: ")
    print(centers)
    clusters = assignCenters(centers, data)
    print("Updated clusters: ")
    for i in range(k):
        print("cluster "+str(i))
        for j in range(len(clusters)):
            if (i == clusters[j]):
                print(data[j], end=' ')
        print()
    print()