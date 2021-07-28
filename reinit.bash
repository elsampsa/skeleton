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

fs="MANIFEST.in README.md setup.py docs/* debian/*"
for f in $fs
do
  find $f -exec sed -i -r "s/skeleton/$name/g" {} \;
  find $f -exec sed -i -r "s/Skeleton/$name/g" {} \;
  find $f -exec sed -i -r "s/your_package_name/$name/g" {} \;
done

find . -name "*.py" -exec sed -i -r "s/skeleton/$name/g" {} \;

# recompile documentation
cd docs
mkdir _static
./clean.bash
# ./compile.bash # we can compile documentation only after this module is on the pythonpath!
cd ..
## decouple from git
#rm -rf .git .gitignore
rm -rf .git
rm -rf *.egg-info

if [ "$#" -eq 2 ]; then
    echo "Initializing to namespace "$1"."$2
    mkdir -p $1
    mv $name $1/$2
fi
