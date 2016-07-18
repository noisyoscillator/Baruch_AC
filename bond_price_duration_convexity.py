# Name: Hongchao Pan
# Date: 7/17/2016
# This file contains code for computing bond price, duration and convexity with
# a given yield of the bond

from __future__ import division
# Get the reasonable approximation of x/y (true division), x//y(floor division)
import math
from bond_price import calculate_flow
# Make sure including bond_price.py and Numerical_integration_method.py

def bond_duration_convexity(coupon,frequency,maturity,yid):
    bond_price=0
    duration=0
    convexity=0
    flow_date,flow_value=calculate_flow(coupon,frequency,maturity)
    for i in range(len(flow_date)):
        cash_flow_date=flow_date[i]
        cash_flow_value=flow_value[i]
        discount_factor=math.exp(-cash_flow_date*yid)
        bond_price +=cash_flow_value*discount_factor
        duration +=cash_flow_date*cash_flow_value*discount_factor
        convexity +=math.pow(cash_flow_date,2)*cash_flow_value*discount_factor
    duration /=bond_price
    convexity /=bond_price
    return bond_price,duration,convexity

if __name__ == "__main__":
    price,duration,convexity=bond_duration_convexity(6,2,20,0.065)
    print price,duration,convexity