#!/bin/bash
## most of these should be done through .gitignore
## clean python bytecode
find . -name "__pycache__" -exec rm -rf {} \;
find . -name "*.pyc" -exec rm -rf {} \;
## python autodoc clean:
find . -name "*.pickle" -exec rm -rf {} \;
find . -name "dist" -exec rm -rf {} \;
find . -name "build" -exec rm -rf {} \;
find . -name "*.egg-info" -exec rm -rf {} \;
find . -name "*.so" -exec rm -f {} \;
find . -name "*.o" -exec rm -f {} \;
