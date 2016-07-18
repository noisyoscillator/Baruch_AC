# Name: Hongchao Pan
# Date: 7/18/2016
# This file contains code for numerical methods, including: Bisection method,
# Newton's methond, Secant method

from __future__ import division
# Get the reasonable approximation of x/y (true division), x//y(floor division)
import math

# Given fx
def f_x(x):
    return math.pow(x,4)-5*x*x+4-1/(1+math.exp(math.pow(x,3)))
def f_prime(x):
    return 4*math.pow(x,3)-10*x+3*x*x*math.exp(-x*x*x)/math.pow((1+math.exp(-x*x*x)),2)

def bisection_method(a,b,f,tol_int,tol_approx):
    x_left=a
    x_right=b
    x_result=0

    while(max(abs(f(x_left)),abs(f(x_right)))>tol_approx) or ((x_right-x_left)>tol_int):
        x_result=(x_left+x_right)/2
        if (f(x_left)*f(x_result))<0:
            x_right=x_result    # active interval [x_left, x_result]
        else:
            x_left=x_result     # active interval [x_result, x_right]

    return x_result

def newtons_method(x0,f,tol_approx,tol_consec):
    x_result=x0
    x_old=x0-1

    while (abs(f(x_result))>tol_approx) or (abs(x_result-x_old)>tol_consec):
        x_old=x_result
        x_result=x_old-f(x_old)/f_prime(x_old)

    return x_result

def secant_method(x00,x0,f,tol_approx,tol_consec):
    x_result=x0
    x_old=x00
    x_oldest=0

    while(abs(f(x_result))>tol_approx) or (abs(x_result-x_old)>tol_consec):
        x_oldest=x_old
        x_old=x_result
        x_result=x_old-f(x_old)*(x_old-x_oldest)/(f(x_old)-f(x_oldest))

    return x_result

if __name__ == "__main__":
    # Test the example in textbook P137-P143
    print bisection_method(-2,3,f_x,1e-6,1e-9)
    print newtons_method(-3,f_x,1e-9,1e-6)
    print newtons_method(-0.5,f_x,1e-9,1e-6)
    print newtons_method(3,f_x,1e-9,1e-6)
    print newtons_method(0.5,f_x,1e-9,1e-6)
    print secant_method(-3.01,-3,f_x,1e-9,1e-6)











