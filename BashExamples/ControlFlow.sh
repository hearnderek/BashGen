#!/bin/bash

# If

a=1;
b=1;
if [ $a -eq $b ]; then
    echo "$a is equal to $b";
fi


# If-Else
a=1;
b=1;
if [ $a -ne $b ]; then
    echo "nop";
else
    echo "$a is not equal to $b";
fi

# If-Else-If
if [ $a -ne $b ]; then
    echo "nop";
elif [ $a -eq $b ]; then
    echo "$a is equal to $b";
else
    echo "nop";
fi

# switch
case $a in
    1) echo "a is 1";;
    2) echo "a is 2";;
    *) echo "a is not 1 or 2";;
esac

# for loop
for i in {1..10}
do
    echo $i;
done

# while loop
i=1;
while [ $i -le 10 ]
do
    echo $i;
    ((i++));
done

# until loop
i=1;
until [ $i -gt 10 ]
do
    echo $i;
    ((i++));
done

# break -- 1 2 3 4 5
for i in {1..10}
do
    if [ $i -gt 5 ]; then
        break;
    fi
    echo $i;
done

echo " "

# continue -- 6 7 8 9 10
for i in {1..10}
do
    if [ $i -le 5 ]; then
        continue;
    fi
    echo $i;
done
