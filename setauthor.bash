#!/bin/bash
if [ $# -ne 1 ]; then
  echo "Give a author name inside quotation marks"
  exit
fi

echo "Setting author to "$1
echo "Are you sure?"
read -n1 -r -p "Press q to quit, space to continue..." key

if [ "$key" = '' ]; then
  echo "running sed"
  find * -exec sed -i -r "s/Janne Jannunen/$1/g" {} \;
  
else
  echo
  echo "cancelled"
fi

