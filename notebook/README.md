Put notebooks using your module here & run in this dir:
```
jupyter notebook
```

When doing interactive development, these should be the first lines for your dev notebook:
```
%reload_ext autoreload
%autoreload 2
```

This is my favorite:
```
# use these magic spells to update your classes methods on-the-fly as you edit them:
%reload_ext autoreload
%autoreload 2
from pprint import pprint
from IPython.core.display import display, HTML, Markdown
import ipywidgets as widgets
# %run includeme.ipynb # include a notebook from this same directory
display(HTML("<style>.container { width:100% !important; }</style>"))
```
