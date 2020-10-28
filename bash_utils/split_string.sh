d='18'

date=$1
if [ -z $date ]
then
  date=$(date -u -d '-1 day' '+%F')
fi

# split string by delimiter '-'
IFS='-' read -ra DATELIST <<< "$date"
echo $DATELIST


session_id=""
for i in "${DATELIST[@]}"; do
    session_id="$session_id$i"
done
session_id="$session_id$d"
echo $session_id

