#!/bin/bash

a=$((10 + 5));
b=$((10 - 5));
c=$((10 * 5));
d=$((10 / 5)); # Division always returns an integer
e=$((10 % 5));
f=$((10 ** 5));
g=$((a + b));
h=$(( (a - b) / d ));

# put all above variables into an array
declare -a arr=($a $b $c $d $e $f $g $h);


# loop through the array and print the variables
for i in "${arr[@]}"
do
    echo '    ' $i;
done


# create a tuple of a and b
declare -a apair=('a' $a);
declare -a bpair=('b' $b);
declare -a all=("${apair[@]}" "${bpair[@]}");

# loop through nested array
counter=1
for i in "${all[@]}"
do
    echo "$counter: $i";
    ((counter++));
done