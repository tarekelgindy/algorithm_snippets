Code for extended Euclidean Algorithm, Modular division and Simultaneous Equation Solving

# Extended Euclidean Algorithm:
For a,b find x and y s.t. ax+by=gcd(a,b)

 Retuns gcd,x,y s.t. the solution solves

 e.g. xgcd(13,7) returns 1,1,2 

 i.e. 13*-1 + 7*2 =1

# Modular Division:
 i.e. reduce ax =b (mod n) into x= ANSWER (mod n) if possible

 Works by solving ax+ny=gcd(n,a) using extended gcd algorithm and finding a value of x
 hence ax=1 (mod n) and x is the inverse of a IF a and n are coprime since ax+ny=1 iff a and n are coprime.
 if b is not divisible by the gcd of a and n, the equation has no solution 
 otherwise multiply through by b/gcd(a,n) to get the solution

 Use simplify(a,1,n) to find the modular inverse of a if and n are coprime

# Simultaneous Equation Solver:
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

