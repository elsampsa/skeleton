import numpy as np
from skeleton_cpp_module import Test, TestNumpy

t=Test()
t.callme()

img=np.ones((10,10), dtype=np.float)
print("input", img)
t=TestNumpy()
line=t.doodle2D(img)
print("output",line)
