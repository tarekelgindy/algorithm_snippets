"""
 i.e. reduce ax =b (mod n) into x= ANSWER (mod n) if possible

 Works by solving ax+ny=gcd(n,a) using extended gcd algorithm and finding a value of x
 hence ax=1 (mod n) and x is the inverse of a IF a and n are coprime since ax+ny=1 iff a and n are coprime.
 if b is not divisible by the gcd of a and n, the equation has no solution 
 otherwise multiply through by b/gcd(a,n) to get the solution

 Use simplify(a,1,n) to find the modular inverse of a if and n are coprime
"""
def simplify(a,b,n):
    #print(a,b,n)
    a=a%n
    b=b%n
    g,k,h = xgcd(n,a) #here h is the co-efficient of a
    h=h%n
    if b%g!=0:
        print('infeasible')
        print(b,g)
        return None
    result=int(h*b/g)
    #print('solves to ',result%n)
    return result%n

"""
 Extended euclidean algorithm. For a,b find x and y s.t. ax+by=gcd(a,b)
 Retuns gcd,x,y s.t. the solution solves
 e.g. xgcd(13,7) returns 1,1,2 
 i.e. 13*-1 + 7*2 =1
"""
def xgcd(a,b):
    h1=1
    h0=0
    k1=0
    k0=1
    det=1
    while b!=0:
        q=int(a/b)
        r=a%b
        h = q*h1+h0
        k = q*k1+k0
        h0=h1
        k0=k1
        h1=h
        k1=k
        a=b
        b=r
        det*=-1
    return a,det*k0,-1*det*h0

#solve a set of simultaneous equations with coprime molulos
"""
    Solve a set of simulataneous modular equations with prime modulos
    Plug first equation into the second equation etc.
    If prime modulos, simplification to find modular inverse will always work
    If modulos are all coprime, chinese remainder theorm says that the solution is unique
    e.g. n = 1 (mod 3)
         n = 4 (mod 5)
         n = 2 (mod 7)
         n=1+3S
         1+3S = 4 (mod 5)
         3S = (4-1) (mod 5)  <- use simplify function here
         S = 1 (mod 5) 

   hence n = 1+ 3*(1+5T)
         n = 4+15T
         
         4+15T = 2 (mod 7)
         15T= -2 (mod 7) <- use simplify function here
         T = 5 (mod 7) 

   hence n = 4 + 15*(5+7U)
         n = 79 + 105U

"""
def simultaneous_mod_solve(all_modulos,all_rhs):
    results = []
    current_multiplier = 1
    current_rhs=0
    for i in range(len(all_rhs)):
        rhs=all_rhs[i]-current_rhs
        solution = simplify(current_multiplier,rhs,all_modulos[i])
        current_rhs=current_rhs+current_multiplier*solution
        current_multiplier*= all_modulos[i]
        results.append(current_rhs)
    return current_rhs

### Example usage simultaneous equation solver (as per example in documentation)

modulos = [3,5,7]
rhs = [1,4,2]
result = simultaneous_mod_solve(modulos,rhs)
print(result)

### Example equations of modular division

# Solve for x in  3x = 7 (mod 13) 
result = simplify(3,7,13)
print(result)

# Solve for x in  3x = 1 (mod 13) 
# i.e. modular inverse
result = simplify(3,1,13)
print(result)

### Example us of extended Euclidean Algorithm 

# find x and y s.t. ax+by = gcd(a,b)
# get gcd, x, y
result = xgcd(13,7)
print(result)
