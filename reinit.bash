#!/bin/bash
name=$(basename $PWD)
if [ "$name" == "skeleton" ]
then
  echo will not overwrite default skeleton directory!
  exit
fi
echo initializing project $name
# rename python module directory
mv skeleton $name
# replace project names
find * -exec sed -i -r "s/skeleton/$name/g" {} \;
find * -exec sed -i -r "s/Skeleton/$name/g" {} \;
find * -exec sed -i -r "s/your_package_name/$name/g" {} \;
# recompile documentation
cd docs
mkdir _static
./clean.bash
# ./compile.bash # we can compile documentation only after this module is on the pythonpath!
cd ..
# decouple from git
cd $name
rm -rf .git .gitignore
cd ..