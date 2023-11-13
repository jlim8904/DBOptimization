###############
# Salt = 1242 #
###############

def hash(string, num):
    hash = 0
    s = 1242
    for i in range(len(string)):
        hash += s**(len(string)-(i+1))*ord(string[i])
    return (hash % num)