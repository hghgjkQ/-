#a为源，b为果(1)
import os

def to2(x):
    x=bin(x)[2:]
    while len(x)<8:
        x='0'+x
    return x
def split_string_by_length(string, length):
    return [string[i:i+length] for i in range(0, len(string), length)]

def a_to_b(path):
    code='1'
    with open(path,'rb') as f:
        while 1:
            a=f.read(1024**2) #1MB
            if not a:
                break
            a=list(a)
            code+=''.join([to2(i) for i in a])
    
    return int(code,2)

def a_t_b(x):
    a=list(x.encode('utf-8'))
    code='1'+''.join([to2(i) for i in a])

    return int(code,2)

def b_to_a(path):
    b=os.path.getsize(path)
    b=bin(b)[3:]
    a = split_string_by_length(b, 8)
    a=[int(i,2) for i in a]
    a=bytes(a)
    return a

while 1:
    c=input('>>>')
    c=c.split(' ')
    if c[0]=='python':
        print(exec(c[1]))
        print('done!')
    if c[0]=='class':
        exec(b_to_a(c[1]))
        print('done!')
    if c[0]=='get':
        b=a_t_b(c[1])
        a=input(f'size：{b/(1024**2)}MB，Y/N?')
        if a=='Y':
            with open(c[2],'w',encoding='utf-8') as f:
                f.write('1'*b)
            print('done!')

    
