

def myanimals():
    '''List sorting with python'''
animals = ['Thor', 'Ophlia', 'Odin', 'Tigger', 'Opal' ]
'''sorts in alphabetical order'''
animals.sort()

print(animals) 
'''below is self explantory'''
animals.reverse() 
print(animals)

'''for loops'''
for animals in animals:
    print(animals + ": I love you")

'''Numbers '''

def numbers():
    mynumbers = [1, 3, 73, 92, 11, 22, 23, 12, 0, 4]
    inorder = sorted(mynumbers)
    print(inorder)
