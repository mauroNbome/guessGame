def digital_root(n):
    result = 0
    if len(str(n)) == 1:
        print(n)
    else:
        
        while len(str(n)) != 1:
            l = list(map(int,str(n)))    
            for i in l:
                result += i #acá tiene la suma de la lista.
            n = result
            if len(str(n)) > 1:
                return digital_root(n)
        print(n)

digital_root(94255)
#https://www.codewars.com/kata/541c8630095125aba6000c00/train/python