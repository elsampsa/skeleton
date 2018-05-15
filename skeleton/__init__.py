__all__=["greeters"]

# ***
# *** Use __init__.py to expose different parts of the submodules in the desired namespace
# ***

# *** Define what can be seen in the main "skeleton." namespace (as this is skeleton/__init__.py) like this:

# from .greeters.fancy import *  # now you can do: from skeleton import FancyHelloWorld
from skeleton.greeters.fancy import * # relative imports are evil, so use this instead

# *** Be aware that that in "skeleton.greeters" a list __all__ has been defined.  It declares what is exposed to the API user when calling "fro skeleton.greeters.fancy import *"
# *** We could declare the API exposure here as well, by being more explicit:

# from skeleton.greeters.fancy import FancyHelloWorld

# *** If you want to keep FancyHelloWorld under the "greeters.fancy." namespace, don't add ".. import *" statements to this file
# *** The idea is, that the submodules have "internal hierarchies" that the API user is not supposed to worry with
# *** and he/she access them simply with "from skeleton import ClassName"

from skeleton.greeters.cool.cool1 import *
from skeleton.greeters.cool.cool2 import *
