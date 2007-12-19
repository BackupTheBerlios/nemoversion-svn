#!/bin/bash

export NEMOVERSION_HOME="`pwd`";

#copy nemoversion plugin to $HOME/.nautilus/python-extensions/
function copy_nemoversion_plugin
{
    if [ -e "${HOME}/.nautilus/python-extensions/" ]; then
        echo "copying nemoversion plugin to ${HOME}/.nautilus/python-extensions/"
        cp $NEMOVERSION_HOME/src/nemoversion.py ${HOME}/.nautilus/python-extensions/
    else
        echo "Cannot find ${HOME}/.nautilus/python-extensions/"
        exit
    fi
}

#make python bytecode for nemoversion (default to $NEMOVERSION_HOME/bin)
function make_nemoversion_bytecode
{
    #TODO:
}

#launch a new nautilus instance (with nemoversion)
function new_nautilus_instance
{
    $mkdir /tmp/nemoversion
    export TMPDIR=/tmp/nemoversion
    nautilus --no-desktop
}