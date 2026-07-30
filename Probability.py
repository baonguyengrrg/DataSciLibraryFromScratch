import math 
from matplotlib import pyplot as plt

#Normal distribution 
def normal_distribution(x:float,muy:float=0,sigma:float=1)->float:
    return (1/(sigma*math.sqrt(2*math.pi)))*(math.exp((-(x-muy)**2)/(2*sigma**2)))
#CDF for normal distribution
def normal_cdf(x:float,muy:float=0,sigma:float=1)->float:
    return (1+math.erf((x-muy)/(sigma*math.sqrt(2))))/2
