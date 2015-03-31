import crypt
import string

def brute():
    file= open('passwd','r')
    line = file.readline()
    line = line[:-1]
    line = line.split(":")
    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            for k in string.ascii_lowercase:
                if crypt.crypt(i+j+k,line[1]) == line[1]:
                    print('haslo: ',i+j+k)
    
brute()
