def fileExists(file):
    try:
        f = open(file,'r')
        f.close()
    except FileNotFoundError:
        return False
    return True

def isLineEmpty(line):
    return len(line.strip()) < 1

def removeEmptyLines(file):
    lines = []
    if not fileExists(file):
        print ("{} does not exist ".format(file))
        return
    out = open(file,'r')
    lines = out.readlines()
    out.close()
    out = open(file,'w')
    t=[]
    for line in lines:
        if not isLineEmpty(line):
            t.append(line)
    out.writelines(t)
    out.close()
def key(arr, N, K):
    listofintprint = []
    m = []
    arr.sort()

    # loop over first (N - K) elements
    # of the array only
    if(K+K<=len(arr)):
        for i in range(K,2*K):
            m = listofintprint.append(arr[i])
        return listofintprint
    else:
        for i in range((K*2)//10,K+1):
            m = listofintprint.append(arr[i])
        return listofintprint
def value(val, N, K):
    listofvalprint = []
    m = []

    # loop over first (N - K) elements
    # of the array only
    if(K+K<=len(val)):
        for i in range(K,2*K):
            m = listofvalprint.append(val[i])
        return listofvalprint
    else:
        for i in range((K*2)//10,K+1):
            m = listofvalprint.append(arr[i])
        return listofvalprint


def minDifferenceAmongMaxMin(arr, N, K):
    arr.sort()

    res = 2147483647

    for i in range((N - K) + 1):
        curSeqDiff = arr[i + K - 1] - arr[i]
        res = min(res, curSeqDiff)

    return res


def Sort(sub_li):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    sub_li.sort(key=lambda x: int(x[1]))
    return sub_li




f = "input1.txt"
removeEmptyLines(f)
file = open(f, "r")
arr = []
val = []
nest = []
lines = [line.rstrip() for line in file]
for i in range(0,1):
    kl = lines[i].split(":")
    K = kl[len(kl)-1]
for i in range(2,len(lines)):
    c = lines[i].split(":")
    n = nest.append(c)

    #arr.append(c[len(c)-1])
    #val.append(c[0])
print(K)
nest = Sort(nest)
for i in nest:
    val.append(i[0])
    arr.append(i[1])
#print(arr)
#print(val)
arr = list(map(int,arr))

N = len(arr)
K = int(K)


mint = key(arr,N,K)
nstr = value(val,N,K)

zip_iterator = zip(nstr,mint)
a_dict = dict(zip_iterator)
last = minDifferenceAmongMaxMin(arr,N,K)
print(a_dict)
print(last)
try:

    finall = open('Output1.txt', 'a')
    finall.write("The goodies selected for distribution are:\n")
    finall.write(str(a_dict))
    finall.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is \n")
    finall.write(str(last))
    finall.close()

except:
    print("Unable to append to file")
