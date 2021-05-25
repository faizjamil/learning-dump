#! /bin/bash

# echo command
echo Hello World!

# VARiABLE
# Uppercase by convention
# Letters, numbers and underscores
NAME="Jack"
echo "My name is ${NAME}"

# USER INPUT

# read -p "Enter your name: " INPUT_NAME

# echo "Hello $INPUT_NAME nice to meet you"

# CONDITIONALS
# IF

# if [ "$NAME" == "Brad" ]
# then
#     echo "Your name is Brad"
# fi
# ELSE
# if [ "$NAME" == "Brad" ]
# then
#     echo "Your name is Brad"
# else 
#     echo "Your name is not Brad"
# fi
# ELSE-IF
# if [ "$NAME" == "Brad" ]
# then
#     echo "Your name is Brad"
# elif [ "$NAME" == "Groundpound69" ]
# then
#     echo "Your name is Airforceproud95"
# else 
#     echo "Your name is not Brad"
# fi

# COMPARISON OPERATORS
NUM1=31
NUM2=5
if [ "$NUM1" -gt "$NUM2" ]
then
    echo "$NUM1 is greater than $NUM2"

else
    echo "$NUM1 is less than $NUM2"
fi

# read NUMBER1
# read NUMBER2
# read NUMBER3

# if [ "$NUMBER1" -eq "$NUMBER2" ] && [ "$NUMBER2" -eq "$NUMBER3" ]
# then
#     echo "EQUILATERAL"
# elif [ "$NUMBER1" -eq "$NUMBER2" ] || [ "$NUMBER2" -eq "$NUMBER3" ]
# then
#     echo "ISOSCELES"
# else
#     echo "SCALENE"
# fi
########
# val1 -eq val2 Returns true if the values are equal
# val1 -ne val2 Returns true if the values are not equal
# val1 -gt val2 Returns true if val1 is greater than val2
# val1 -ge val2 Returns true if val1 is greater than or equal to val2
# val1 -lt val2 Returns true if val1 is less than val2
# val1 -le val2 Returns true if val1 is less than or equal to val2
########

# FILE CONDITIONS
# FILE="test.txt"
# if [ -e "$FILE" ]
# then
#     echo "$File is a file"
# else
#     echo "$FILE is not a file"
# fi

########
# -d file   True if the file is a directory
# -e file   True if the file exists (note that this is not particularly portable, thus -f is generally used)
# -f file   True if the provided string is a file
# -g file   True if the group id is set on a file
# -r file   True if the file is readable
# -s file   True if the file has a non-zero size
# -u    True if the user id is set on a file
# -w    True if the file is writable
# -x    True if the file is an executable
########

# CASE STATEMENTS
# read -p "Are you 21 or older? Y/N " ANSWER
# case "$ANSWER" in 
#     [yY] | [yY][eE][sS])
#         echo "You can have a beeer :)"
#         ;;
#     [nN] | [nN][oO])
#         echo "Sorry no drinking"
#         ;;
#     # default case
#     *)
#         echo "PLease enter Y/Yes or N/No"
#     ;;  
# esac

# SIMPLE FOR LOOP
# NAMES="Brad Kevin Alice Mark"

# for NAME in $NAMES
#     do
#         echo "Hello $NAME"
# done

# FOR LOOP TO RENAME FILES
# FILES=$(ls *.txt)
# NEW="new"
# for FILE in $FILES
#     do 
#         echo "Renaming $FILE to new=$FILE"
#         mv $FILE $NEW-$FILE

# done

# WHILE LOOP - READ THROUGH A FILE LINE BY LINE
# LINE=1
# while read -r CURRENT_LINE
#     do 
#         echo "$LINE: $CURRENT_LINE"
#         ((LINE++))
# done < "./new-1.txt"

# FUNCTION
# function sayHelloWorld() {
#     echo "Hello World!"
# }
# sayHelloWorld

# FUNCTION WITH PARAMS
# function greet() {
#     echo "Hello I am $1 and I am $2"
# }

# greet "Brad" "36"

# CREATE FOLDER AND WRITE TO FILE
mkdir hello
touch "hello/world.txt"
echo "Hello World" >> "hello/world.txt"
echo "Created hello/world.txt"

# No prob, also note that with bash, if you have a read only file system you need to chmod 777 not just chmod +rx
# For whatever reason +rx isn’t enough lol