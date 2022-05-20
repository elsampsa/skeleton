# __init__.py files ONLY for exposing namespaces/APIs
# *** Define what can be seen in the main "skeleton." namespace (as this is skeleton/__init__.py) like this:
from skeleton.greeters import BaseHelloWorld, FancyHelloWorld

try:
    # load the cpp extension into skeleton. namespace:
    from skeleton_cpp import skeleton_cpp_module as cpp_module
    """now you can do elsewhere in the code:

    ::

        from skeleton import cpp_module
        t=cpp_module.Test()
        t.callme()

    """
    print("cpp extension loaded from", cpp_module.__file__,"and from", cpp_module._skeleton_cpp_module.__file__)
except ModuleNotFoundError:
    print("WARNING: cpp extension not available")
