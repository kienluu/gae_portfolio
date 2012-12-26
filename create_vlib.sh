#!/bin/bash



# Make the vlib folder if it does not exist
export vlib="vlib"
test -d $vlib || mkdir $vlib

# FIXME: Virtualenv check may not be necessary anymore as we are just looking
# for package's path anywhere in the sys.path list now
#
# Check we are in a virtual environment
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Please load your virtual environment first"
    exit 1
fi

export VLIB_FILE='vlib_requirements.txt'
if [ ! -e $VLIB_FILE ]; then
    echo "$VLIB_FILE does not exist"
    exit 1
fi

for lib_name in $(cat vlib_requirements.txt); do
    if [ ! -h "$vlib/$lib_name" ]; then
        echo "Creating new symbolic link @ "`./findpath.py $lib_name`" ..."
        ln -s "`./findpath.py $lib_name`" "$vlib/$lib_name"
    fi
done
