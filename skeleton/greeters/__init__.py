# when doing from skeleton.greeters import *, base and fancy are loaded into the current namespace
__all__=["base","fancy","cool"]

# this has the effect that everything in namespaces "skeleton.greeters.fancy" and "skeleton.greeters.cool" is accessible also in "skeleton.greeters" namespace
from .fancy import *
from .cool import *
 