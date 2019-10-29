A=$1
B=$2
C=$3
echo $A $B $C

if [ -z $C ] # check whether an external argument has been passed for the given param  or not (empty)
then
  echo "No value for C"
fi