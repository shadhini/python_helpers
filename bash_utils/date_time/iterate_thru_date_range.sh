d=2015-01-01
while [ "$d" != 2015-02-20 ]; do
  echo $d
  d=$(date -I -d "$d + 1 day")
done