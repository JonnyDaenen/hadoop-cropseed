


def id_1(i):
    return str(i)

def id_2(i):
    return str(i) + "," + str(i)




def generate_keyvalue(i):
    return i
 
 
def seq4(i):
    ct = 4
    list = [ 1 + i*ct + j for j in range(0,ct)]
    return tuple2string(list)
    
def plus4(i):
    return i *  4 + 1
    
def plus2_6(i):
    if (i % 2) == 0:
        return (i/2)*8 + 2
    else:
        return (i * 4)
    
def seqclone4(i):
    return tuple2string([i,i,i,i])
    
def seqclone4R(i):
    return "R("+tuple2string([i,i,i,i])+")"
            
        
def non_mod_2(i):
    return non_mod(2,i)

def non_mod_2_100x(i):
    return non_mod(2,i/100);
    
def non_mod_3(i):
    return non_mod(3,i)
    
def non_mod_4(i):
    return non_mod(4,i)

def non_mod_5(i):
    return non_mod(5,i)
    
    
    
def non_mod_2S2(i):
    return "S2("+str(non_mod(2,i))+")"
    
def non_mod_3S3(i):
    return "S3("+str(non_mod(3,i))+")"
    
def non_mod_4S4(i):
    return "S4("+str(non_mod(4,i))+")"

def non_mod_5S5(i):
    return "S5("+str(non_mod(5,i))+")"


    
def non_mod(n,i):
    return n*(i/(n-1)) + 1 + i % (n-1) 
    
    
def tuple2string(list):
    return reduce(lambda x,y: str(x) + "," + str(y), list)
    
def tuple2string2(list, name):
    return name + "(" + reduce(lambda x,y: str(x) + "," + str(y), list) + ")"

def test_1mil(i):
    list = [i,1000000-i,i]
    return tuple2string(list)
