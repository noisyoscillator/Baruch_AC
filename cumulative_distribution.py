# Name: Hongchao Pan
# Date: 7/18/2016
# This file contains code for computing cumulative distribution corresponding to
# Advanced Calculus textbook P103

from __future__ import division
# Get the reasonable approximation of x/y (true division), x//y(floor division)
import math

def cum_dist_normal(t):
    z=abs(t)    # t is a real number
    y=1/(1+0.2316419*z)
    a1=0.319381530
    a2=-0.356563782
    a3=1.781477937
    a4=-1.821255978
    a5=1.330274429
    m=1-math.exp(-0.5*t*t)*(a1*y+a2*math.pow(y,2)+a3*math.pow(y,3)+
                            a4*math.pow(y,4)+a5*math.pow(y,5))/math.sqrt(2*math.pi)
    if t>0:
        return m
    else:
        return 1-m

if __name__ == "__main__":
    print cum_dist_normal(0.383206)