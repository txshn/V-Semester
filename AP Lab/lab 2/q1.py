string = input("Please enter any String : ")
words = []

words = string.split()
n = [words.count(i) for i in words]

myDict = dict(zip(words, n)
print("Dictionary Items  :  ",  myDict)
