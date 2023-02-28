#!/bin/bash
name=$(basename $PWD)
if [ "$name" == "skeleton" ]
then
  echo will not overwrite default skeleton directory!
  exit
fi
echo initializing project $name
# rename python module directory

fr="skeleton"
to=$name

fr2="Skeleton"
to2=$(python3 -c 'import sys; print(sys.argv[1].capitalize())' $name)

echo
echo "renaming all ocurrences of '"$fr"' to '"$to"'"
echo "renaming all ocurrences of '"$fr2"' to '"$to2"'"
echo "renaming directories & files having '"$fr"' into '"$to"'"
echo
echo "Are you sure?"
echo "Be sure that *this* script is not being modified..!"
read -n1 -r -p "Press q to quit, space to continue..." key
echo

## decouple from git
echo "Remove git stuff"
rm -rf .git
echo "Cleanup eggs and builds etc."
find . -name "__pycache__" -exec rm -rf {} \;
find . -name "*.pyc" -exec rm -rf {} \;
find . -name "*.pickle" -exec rm -rf {} \;
find . -name "dist" -exec rm -rf {} \;
find . -name "build" -exec rm -rf {} \;
find . -name "*.egg-info" -exec rm -rf {} \;
find . -name "*.so" -exec rm -f {} \;
find . -name "*.o" -exec rm -f {} \;

if [ "$key" = '' ]; then
    for dep in 1 2 3 4
    do
        echo "DEPTH"$dep
        # find all filenames & dirs with name skeletonXXXXX
        # "if True:" only to achieve ok intendation. :)
        find . -maxdepth $dep -name "skeleton*" | xargs -I {} python3 -c 'if True:
            import sys, os
            fname=sys.argv[1]
            fr=sys.argv[2]
            to=sys.argv[3]
            fname_new=fname.replace(fr, to) # i.e. replace filename skeletonXXXX to newnameXXXX
            print("renaming", fname, "to", fname_new)
            os.rename(fname, fname_new)
        ' {} $fr $to
    done
    echo "next running sed"
    find * -type f -exec sed -i -r "s/$fr/$to/g" {} \;
    find * -type f -exec sed -i -r "s/$fr2/$to2/g" {} \;
else
  echo
  echo "CANCELLED"
  echo
  exit 2
fi

# recompile documentation
echo "Cleaning up docs at" $name/docs
cd $name/docs
mkdir -p _static
./clean.bash
# ./compile.bash # we can compile documentation only after this module is on the pythonpath!
cd ../..

if [ "$#" -eq 2 ]; then
    echo "Initializing to namespace "$1"."$2
    mkdir -p $1
    mv $name $1/$2
fi
echo
echo DONE!
echo
