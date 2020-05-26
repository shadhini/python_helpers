######### simple guide ########################
# https://cloud.google.com/storage/docs/gcs-fuse
mkdir /path/to/mount
gcsfuse --implicit-dirs example-bucket /path/to/mount/
ls /path/to/mount

# --implicit-dirs ==> https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/semantics.md#implicit-directories
##################################################

# Create directory to mount the bucket
cd /mnt/disks
sudo mkdir curwsl_nfs

sudo chown uwcc-admin:uwcc-admin curwsl_nfs

# installing gcsfuse ----------------------------------------------------

# If gcsfuse isn’t installed on the vm install it as follows,
export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s`

echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | sudo tee /etc/apt/sources.list.d/gcsf

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt-get update

sudo apt-get install gcsfuse

# installing gcsfuse END----------------------------------------------------

# Then mount the previously created bucket as follows,
gcsfuse --implicit-dirs curwsl_nfs curwsl_nfs/

# if above gives errors like
# touch: cannot touch 'some.txt': Input/output error
# then use the following command
gcsfuse --key-file=/home/uwcc-admin/uwcc-admin.json --implicit-dirs curwsl_nfs curwsl_nfs/


