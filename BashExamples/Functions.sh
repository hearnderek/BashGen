#!/bin/bash

# A simple function
function hello() {
    echo "Loves me!";
}

function goodbye() {
    echo "Loves me not...";
}

for i in {1..10}
do
    if [ $(( i % 2 )) -eq 0 ]; then
        hello;
    else
        goodbye;
    fi
done