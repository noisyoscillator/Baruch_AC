# Name: Hongchao Pan
# Date: 7/17/2016
# This file contains method to compute bond price with given zero rate curve
# and given the instantaneous interest rate curve

from __future__ import division
# Get the reasonable approximation of x/y (true division), x//y(floor division)
import math
from Numerical_integration_methods import simpson_rule,approx_val_tol

# Compute bond price with given zero rate curve
# Define the zero rate curve
def zero_rate_func(t):
    return 0.0525 + math.log(1+2*t)/200 # function in P67

# Get the cash flow date and value
def calculate_flow(coupon, frequency, maturity):
    """
    :param coupon: in dollars
    :param frequency: is an int
    :param maturity: in months
    :return: intervals scaled by years
    """
    "This functon calculates cash flow dates and values."
    flow_date=range(maturity,0,int(-12/frequency))
    flow_date.reverse()
    flow_date=[t/12 for t in flow_date]   # Convert the date

    flow_value=[coupon/frequency for i in flow_date[:-1]]+[100+coupon/frequency]
    # flow_date[:-1] remove the last elements in the list
    return flow_date, flow_value

# Calculate discount factor
def calculate_df(r,t):
    return math.exp(-r*t)
# r is zero rate curve function corresponding to time t

def bond_price_zero_rate(coupon,frequency,maturity,zero_rate_function):
    bond_price=0
    flow_date,flow_value=calculate_flow(coupon,frequency,maturity)
    for i in xrange(len(flow_date)):
        cash_flow_date=flow_date[i]
        cash_flow_value=flow_value[i]
        discout_factor=calculate_df(zero_rate_function(cash_flow_date),cash_flow_date)
        bond_price +=cash_flow_value*discout_factor

    return bond_price

# Compute bond price with given instantaneous rate curve
# Define instantaneous rate curve
def instan_rate_func(t):
    return 0.0525+1/(100*(1+math.exp(-t*t)))

def bond_price_instan_rate(coupon,frequency,maturity,instan_rate_function):
    bond_price=0
    flow_date,flow_value=calculate_flow(coupon,frequency,maturity)
    tol=[5e-4 for i in flow_date[:-1]]+[5e-6]
    for i in xrange(len(flow_date)):
        cash_flow_date=flow_date[i]
        cash_flow_value=flow_value[i]
        discount_factor=math.exp(-approx_val_tol(simpson_rule,0,cash_flow_date,
                                       instan_rate_func,4,tol[i]))
        bond_price +=cash_flow_value*discount_factor
    return bond_price


if __name__=="__main__":
    print bond_price_zero_rate(6,2,20,zero_rate_func)
    print bond_price_instan_rate(6,2,20,instan_rate_func)