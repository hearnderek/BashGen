#!/bin/bash


# strict mode
set -euo pipefail

# create string variable
str="Hello World!";

# split string into array
arr=($str);

echo "String: $str";

# loop through array and print each element
echo "String: ${arr[@]}";

# first element... etc
echo "String1: ${arr[0]}";
echo "String2: ${arr[1]}";
#echo "String2: ${arr[2]}" || echo "<- silent error unless we set -euo pipefail";


# concat strings
combined="${arr[0]}, ${arr[1]}";
echo "Combined: $combined";


# remove 'l's from string
noels="${str//l/}"
echo $noels;

# replace 'l's with 'L's
bigels="${str//l/L}"
echo $bigels;

# substring 4-7
echo "${str:4:7}";