# __init__.py files ONLY for exposing namespaces/APIs
# *** Define what can be seen in the main "skeleton." namespace (as this is skeleton/__init__.py) like this:
from skeleton.greeters import BaseHelloWorld, FancyHelloWorld

"""The cpp module has been installed either as a separate python package "skeleton_cpp"
or as a separate module "skeleton_cpp" (pertaining to this same package "skeleton")

either way, we attach it to the "skeleton." namespace in here:
"""
cpp_imported = True
try:
    # as a separate module "skeleton_cpp" of this package:
    from skeleton_cpp.skeleton_cpp import skeleton_cpp_module as cpp_module
except Exception as e1:
    try:
        # as a separate python package "skeleton_cpp"
        from skeleton_cpp import skeleton_cpp_module as cpp_module    
    except Exception as e2:
        print((
            "WARNING: could not load the cpp extension neither from the "
            "module 'skeleton_cpp' nor from a separate python package "
            "'skeleton_cpp'\n",
            f"exceptions were: '{e1}' and '{e2}'\n"
            ))
        cpp_imported = False

if cpp_imported:
    """now you can do elsewhere in the code:

    ::

        from skeleton import cpp_module
        t=cpp_module.Test()
        t.callme()

    """
    print("NOTE: cpp extension loaded from", 
        cpp_module.__file__,"and from", 
        cpp_module._skeleton_cpp_module.__file__,
        "FEEL FREE TO REMOVE THIS MESSAGE\n"
        )
