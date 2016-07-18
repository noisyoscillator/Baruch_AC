# Name: Hongchao Pan
# Date: 7/17/2016
# This file contains method to compute bond yield with given bound price

from __future__ import division
# Get the reasonable approximation of x/y (true division), x//y(floor division)
import math
from bond_price import calculate_flow

def bond_yield(coupon,frequency,maturity,B):
    x0=0.1  # Initial guess: 10% yield
    x_new=x0
    x_old=x0-1
    tol=1e-6    # Tol for declaring convergence of Newton's method
    flow_date,flow_value=calculate_flow(coupon,frequency,maturity)
    print x_new,x_old

    while abs(x_new-x_old)>tol:
        x_old=x_new
        sum_numerator=0
        sum_denominator=0
        for i in xrange(len(flow_date)):
            cash_flow_date=flow_date[i]
            cash_flow_value=flow_value[i]
            sum_numerator +=cash_flow_value*math.exp(-x_old*cash_flow_date)
            sum_denominator +=cash_flow_value*cash_flow_date*math.exp(-x_old*cash_flow_date)

        x_new=x_old+(sum_numerator-B)/sum_denominator

    return x_new



if __name__ == "__main__":
    print bond_yield(8,2,34,105)