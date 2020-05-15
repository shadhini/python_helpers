# method 1
strings=(
    string1
    string2
    "string with spaces"
    stringN
)
for i in "${strings[@]}"; do
    echo "$i"
done

echo "########"
# method 2
for i in \
    string1 \
    string2 \
    "ncj jkbsdjk " \
    stringN
do
   printf '%s\n' "$i"
done

echo "########"
# method 3
strings=(
    string1
    string2
    stringN
)

printf '%s\n' "${strings[@]}"


