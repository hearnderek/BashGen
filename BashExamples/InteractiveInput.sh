#!/bin/bash

# ask yes no question
function askYesNo() {
    # set state to tru
    state=true;
    while $state; do
        read -p "$1 [y/n] " yn
        
        case $yn in
            [Yy]* ) state=true;;
            [Nn]* ) state=false;;
            * ) echo "Please answer yes or no.";;
        esac
    done
}

askYesNo "Do you want to continue?"
