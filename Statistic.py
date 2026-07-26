from typing import List
from typing import Tuple
from typing import Callable
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
#variance
def variance(v:List[float])->float:
    m=mean(v)
    return (sum((v_i-m)**2 for v_i in v)*(1/len(v)))
#standard variance
def standard_variance(v:List[float])->float:
    return math.sqrt(variance(v))
#interquartile range
def interquartile_range(v:List[float])->float:
    return quantile(v,0.75)-quantile(v,0.25)

