from features import Feature
from cal_sys import que_creation
def create(path,total,index):
    list = []
    counter = 0
    '''
    zero = Feature("(1*2+3)*4","5*4")
    one = Feature("(2*1+3)*4","5*4")
    list.append(zero)
    if check(one, list):
        list.append(one)
    else:
        counter +=1
    '''
    for i in range(total):
        string,symble = que_creation(index)
        a = Feature(string,symble)
        if check(a,list) :
            list.append(a)
        else:
            counter +=1
            continue
    print("counter:%d" %counter)


    for i in range(counter):
        string, symble = que_creation(index)
        a = Feature(string, symble)
        if check(a, list):
            list.append(a)
        else:
            counter += 1
            continue

    with open(path, 'w', encoding='utf-8') as x:
        line = 0
        for i in list:
            line += 1
            x.write(str(line) + '. ' + i.problem + '\n')


def check(Feature,list1=[]):
    b = Feature
    for i in list1:
        if b.num ==i.num and b.sym ==i.sym and b.op == i.op:
            print("题目重复")
            return False
        else:
            continue
    return True



