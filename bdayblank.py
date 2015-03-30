import sys
import math

def bdayblank(o,f):
    original = [o]
    fake = [f]
    originalhash=[trivial_hash(o)]
    fakehash=[trivial_hash(f)]
    iteration=0
    blanks = [chr(0),chr(7),chr(8),chr(9),chr(10),chr(13),chr(32),chr(255)]
    while True:
        longest=int(math.pow(len(blanks),iteration))
        iteration+=1
        temporig = original[-longest:]
        tempfake = fake[-longest:]
        for char in blanks:
                for string in temporig:
                    original.append(string+char)
                    result = search(fakehash, originalhash, string+char)
                    if not result==None:
                        result[0]=fake[result[0]]
                        return result
                for string in tempfake:
                    fake.append(string+char)
                    result = search(originalhash, fakehash, string+char)
                    if not result==None:
                        result[0]=original[result[0]]
                        return result

        
def search(hashes1, hashes2, word):
    wordhash=trivial_hash(word)
    hashes2.append(wordhash)
    for i in range(len(hashes1)):
        if hashes1[i]==wordhash:
            return [i, word]

def trivial_hash(dane):
        hash = 0
        for znak in dane:
                hash += ord(znak)
        return hash % 999

result = bdayblank(sys.argv[1],sys.argv[2])
print(result)
print(trivial_hash(result[0]), trivial_hash(result[1]))
