# ** Use __init__.py files only for API exposure, not for writing any code! **
from skeleton.greeters.base import BaseHelloWorld
from skeleton.greeters.fancy import FancyHelloWorld
# now API user can do: "from skeleton.greeters import BaseHelloWorld, FancyHelloWorld"
#
# when doing from skeleton.greeters import *, base and fancy are loaded
# into the current namespace:
__all__ = ["base", "fancy"]
# this has the effect that everything in namespaces "skeleton.greeters.fancy" and "skeleton.greeters.base" is accessible
