# Name: Hongchao Pan
# Date: 7/17/2016
# This file contains method to compute implied volatility of BS model

from __future__ import division
# Get the reasonable approximation of x/y (true division), x//y(floor division)
import math
from black_scholes import vega_BS,black_scholes

def implied_vol(t,S,K,T,r,q,P,option_type=None):
    """
    :param t: initial time
    :param S: stock price
    :param K: stock strike
    :param T: maturity
    :param r: constant rate
    :param q: dividend rate
    :param P: option market price
    :param option_type: None for CALL, CALL, PUT
    :return: implied volatility
    """
    x0=0.25 # Initial guess: 25% volatility
    x_new=x0
    x_old=x0-1
    tol=1e-6    # Tolerance for declaring convergence of Newtown's method
    # f_x and f_prime is given here

    while abs(x_new-x_old)>tol:
        x_old=x_new
        V_BS=black_scholes(t,S,K,T,x_new,r,q,option_type)
        V_vega=vega_BS(t,S,K,T,x_new,r,q)
        x_new=x_new-(V_BS-P)/V_vega

    return x_new

if __name__ == "__main__":
    # Test the example in textbook P153
    print implied_vol(0,25,20,1,0.05,0,7,"CALL")