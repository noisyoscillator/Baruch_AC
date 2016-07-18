# Name: Hongchao Pan
# Date: 7/17/2016
# This file contains mid-point rule, Traprzoidal rule, and Simposon's rule
# and calculate approximate value of an integral with given tolerance

from __future__ import division
# Get the reasonable approximation of x/y (true division), x//y(floor division)
import math

# Define input evaluating function
def f_x(x):
    return math.exp(-x*x)

# a: left endpoint; b: right endpoint; n: number of partition intervals
def mid_point_rule(a,b,f,n):
    h=(b-a)/n
    result=0
    for i in xrange(1,n+1):
        result+=f(a+(i-0.5)*h)
       # print result

    return result*h

# a: left endpoint; b: right endpoint; n: number of partition intervals
def Trapezoidal_rule(a,b,f,n):
    h= (b-a)/n
    result=(f(a)+f(b))/2

    for i in xrange(1, n):
        result += f(a + i*h)

    return result*h

# a: left endpoint; b: right endpoint; n: number of partition intervals
def simpson_rule(a,b,f,n):
    h= (b-a)/n
    result=(f(a) + f(b))/6

    for i in xrange(1, n):
        result += f(a + i*h)/3
    for i in xrange(1, n+1):
        result += 2*f(a + (i-0.5)*h)/3

    return result*h

# f: mid_point/trape/simpson method, n: intervals
def approx_val_tol(f_med,a,b,f,n,tol):
    #tol=5e-7
    result_old=f_med(a,b,f,n)
    n=2*n
    result_new=f_med(a,b,f,n)

    while(abs(result_old-result_new)>tol):
        result_old=result_new
        n=2*n
        result_new=f_med(a,b,f,n)

    return result_new


# execute program from here
if __name__=="__main__":
    print mid_point_rule(0,2,f_x,4) # check answer with P49
    print mid_point_rule(0,2,f_x,512)   # check answer with P49
    print simpson_rule(0,2,f_x,4) # check answer with P49

    print approx_val_tol(mid_point_rule,0,2,f_x,4,5e-7)
    print approx_val_tol(simpson_rule,0,2,f_x,4,5e-7)