def missing1():
    
    myList = [1,2,3,4,6,8,9]
    size = len(myList)
    for i in range(0,size-1):
        new_num = myList[i] +1
        if new_num == myList[i+1]:
            continue
        else:
            print(new_num)

def missing2():
    myList = [1,2,3,4,6,8,9]
    size = len(myList) +2
    sum_1 = sum(myList)
    print(size)
    print(sum_1)

def zero_one():
    one = 0
    zero = 0
    myList = [1,0,2,0,1,2,0,0,1,1]
    for i in range(len(myList)):
        if myList[i] == 0:
            zero = zero +1
        elif myList[i] == 1:
            one = one +1
    print("zero "+str(zero))
    print("one "+str(one))
    
def zero_one_2():
    myList = [1,0,2,0,1,2,0,0,1,1]
    zero = myList.count(0)
    one = myList.count(1)
    print("zero "+str(zero))
    print("one "+str(one))

#equilibrium problem --> print number where sum of left and right are equal
def equilibrium():
    #myList = [1,0,2,0,1,2,0,0,1,1]
    myList = [-7, 1, 5, 2, -4, 3, 0]
    size = len(myList)
    #print(myList[3:])
    for i in range(size):
        left = sum(myList[:i])
        right = sum(myList[i:])
        if left == right:
            print("found equilibrium: " +str(i))
            break
def number():
    myList = [-7, 1, 5, 2, -4, 3, 0]
    print(myList[::-2])

#dictionary=sumit kumawat

def name_dict():
    name = "sumit kumawat"
    name_set = set(name)
    my_dict = {}
    for i in name_set:   # -->n
        count = name.count(i)
        #print(str(i) + str(count))
        my_dict[i] = count
    print(my_dict)
    for i in my_dict: # -->n*n
        myList = []
        for j in range(int(my_dict[i])):
            myList.append(i)
        print(str(my_dict[i])+":"+",".join(myList))

#min-max
#second highest
def second_highest():
    myList = [-12,1,3,5,13,9,2,6,10,11]
    h1 = myList[0]
    for i in range(len(myList)):
        #print(myList[i])
        if h1 < myList[i]:
            h1 = myList[i]
    print("First Highest: " +str(h1))
    h2 = myList[0]
    for i in range(len(myList)):
        if h2 < myList[i] and myList[i] != h1:
            h2 = myList[i]
    print("Second highest: " +str(h2))

def second_highest_pop():
    myList = [-12,1,3,5,13,9,2,6,10,11]
    pos1 = 2
    h1 = myList[0]
    for i in range(len(myList)):
        #print(myList[i])
        if h1 < myList[i]:
            h1 = myList[i]
    def pop_func():
        for i in range(len(myList)):
        #print(myList[i])
          if h1 < myList[i]:
            h1 = myList[i]
    


second_highest_pop()
