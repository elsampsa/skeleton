#!/bin/bash
name=$(basename $PWD)
if [ $# -ne 1 ]; then
  # echo "Give version and release in quotation marks, like this:"
  # echo '"0" "1"'
  echo "Give version name in quotation marks, like this:"
  echo '"1.0"'
  exit
fi

# echo setting version $1 release $2
echo setting version $1

# exit

fs="MANIFEST.in README.md setup.py $name/* docs/*"
for f in $fs
do
  find $f -exec sed -i -r "s/version = '(.*)'/version = '$1'/g" {} \;
  find $f -exec sed -i -r "s/release = '(.*)'/release = '$1'/g" {} \;
done

# mod python files:
find -name "*.py" -exec sed -i -r "s/@version (.*)/@version $1 /g" {} \;

echo Dont forget to use ..
echo
echo "git tag -a "$version" -m 'my version "$version"'"
echo git push origin --tags
echo
echo .. this informs git about the new version number
echo
