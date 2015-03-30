import md5

def md5checksum():
    checksum_file = open("checksum","r")
    line = checksum_file.readline()
    line = line.split()
    checksum = line[0]
    m=md5.new()
    file = open("passwd","r")
    plaintext = file.read()
    m.update(plaintext)
    new_checksum = m.hexdigest();
    print(checksum)
    print(new_checksum)
    if checksum == new_checksum:
        print('takie same')
    else:
        print('inne')

md5checksum()
