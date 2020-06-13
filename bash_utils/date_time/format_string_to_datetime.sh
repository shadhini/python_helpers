input="2020-06-11_02-00-00"

IFS='_' read -r -a array <<< $input
date=${array[0]}

IFS='-' read -r -a array2 <<< ${array[1]}
time="${array2[0]}:${array2[1]}:${array2[2]}"

formatted_fgt="\"${date} ${time}\""

echo $date
echo $time
echo $formatted_fgt