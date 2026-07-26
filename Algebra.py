from typing import List
from typing import Tuple
from typing import Callable
import math
# ______
#|      |
#|VECTOR|
#|______|
#define Vector
Vector=List[float]

#cong vector
def add(v:Vector, w:Vector)->Vector:
    if(len(v)!=len(w)):
        raise ValueError("Vectors must be of the same length")
    else:
        return [v_i + w_i for v_i, w_i in zip(v,w)]
#tru vector
def substract(v:Vector, w:Vector)->Vector:
    if(len(v)!=len(w)):
        raise ValueError("Vectors must be of the same length")
    else:
        return [v_i - w_i for v_i, w_i in zip(v,w)]
#tong vector
def sumvector(vectors:List[Vector])->Vector:
    if (len(vectors)==0):
        raise ValueError("Vectors list must not be empty")
    return add(vectors[0],sumvector(vectors[1:])) if len(vectors) > 1 else vectors[0]
#nhan vector voi so
def multiply(v:Vector, scalar:float)->Vector:
    return [scalar*v_i for v_i in v]
#trung binh vector
def vector_mean(vectors:List[Vector])->Vector:
    if (len(vectors)==0):
        raise ValueError("Vectors list must not be empty")
    return (multiply(sumvector(vectors),(1/len(vectors))))
#tich vo huong
def scalar_product(v:Vector,w:Vector)->float:
    if (len(v)!=len(w)):
        raise ValueError("Vectors must be of the same length")
    else:
        return sum(v_i * w_i for v_i, w_i in zip(v,w))
#magnitude
def magnitude(v:Vector)->float:
    if (len(v)==0):
        raise ValueError("Vector must not be empty")
    else:
        return math.sqrt(scalar_product(v,v))
#distance
def distance(v:Vector, w:Vector)->float:
    return magnitude(substract(v,w))
# ______
#|      |
#|MATRIX|
#|______|
#define Matrix
Matrix=list[list[float]]

#get_row
def get_row(m:Matrix,i:int)->Vector:
    return m[i]
#get_column
def get_column(m:Matrix,j:int)->Vector:
    return [m_i[j] for m_i in m]  
#return size
def shape(m:Matrix)->Tuple[int, int]:
    return len(m), len(m[0]) if m else 0
#make matrix
def make_matrix(row:int, col:int, entry_fn:Callable[[int,int],float])->Matrix:
    return [[entry_fn(i,j)]
            for j in range(col)
            for i in range(row)
            ]
#identity_matrix
def identity_matrix(n:int)->Matrix:
    return make_matrix(n,n,lambda i, j:1 if i==j else 0)

