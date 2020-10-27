find /mnt/disks/wrf_nfs/ -name "*.nc" -type f -mtime +90 -exec rm -v {} \;
