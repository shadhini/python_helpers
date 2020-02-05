gfs_run=$1

for VARIABLE in "2020-02-01" "2020-02-02" "2020-02-03" "2020-02-04"
do
	date="$VARIABLE 05:00:00"
	echo $date
	echo "Params passed:: gfs_run=$gfs_run, date=$date"
  python cl_datetime_args.py -r $gfs_run -D "$date" >> cl_datetime_args.log 2>&1
done