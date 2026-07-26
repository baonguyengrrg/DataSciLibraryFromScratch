from typing import List
from typing import Tuple
from typing import Callable
import Algebra as lt
import math
# __________________
#|                  |
#|CENTRAL TENDENCIES|
#|__________________|

#mean
def mean(v:List[float])->float:
    return sum(v)/len(v)
#median odd
def median_odd(v:List[float])->float:
    v=sorted(v)
    return v[len(v)//2]
#median even
def median_even(v:List[float])->float:
    v=sorted(v)
    hi_mid=len(v)//2
    lo_mid=len(v)//2-1
    return (v[hi_mid]+v[lo_mid])/2
#general median
def median(v:List[float])->float:
    if (len(v)%2==0):
        return median_even(v)
    else:
        return median_odd(v)
#quantile
def quantile(v:List[float],p:float)->float:
    p_index=int(p*(len(v)))
    v=sorted(v)
    return v[p_index]

# __________
#|          |
#|DISPERSION|
#|__________|

#data range
def data_range(v:List[float])->float:
    return max(v)-min(v)
#deviation mean
def de_mean(v:List[float])->List[float]:
    v_bar=mean(v)
    return [v_i-v_bar for v_i in v]
#sum of squares
def sum_of_squares(v:List[float])->float:
    return lt.scalar_product(v,v)
#variance
def variance(v:List[float])->float:
    m=de_mean(v)
    n=len(v)
    return sum_of_squares(m)/(n-1)
#standard variance
def standard_deviation(v:List[float])->float:
    return math.sqrt(variance(v))
#interquartile range
def interquartile_range(v:List[float])->float:
    return quantile(v,0.75)-quantile(v,0.25)

# ___________
#|           |
#|CORRELATION|
#|___________|

#covariance
def covariance(a:List[float],b:List[float])->float:
    return lt.scalar_product(de_mean(a),de_mean(b))/(len(a)-1)

#correlation
def correlation(a:List[float],b:List[float])->float:
    stdev_x=standard_deviation(a)
    stdev_y=standard_deviation(b)
    if (stdev_x>0 and stdev_y>0):
        return covariance(a,b)/(stdev_x*stdev_y)
    else:
        return 0
