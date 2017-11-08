# print("importing skeleton.greeters.base")

# when doing from skeleton.greeters import *, base and fancy are loaded into the current namespace
__all__=["base","fancy"]

# this has the effect that everything in namespace "skeleton.greeters.base" is accessible also in "skeleton.greeters" namespace
from .base import * 
from .fancy import *

 