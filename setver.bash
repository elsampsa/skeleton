#!/bin/bash
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

find * -exec sed -i -r "s/version = '2.1'/g" {} \;
find * -exec sed -i -r "s/release = '2.1'/g" {} \;


