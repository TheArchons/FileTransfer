cd /home/admin/FileTransfer
git stash
git pull
nohup python3 -u manage.py runserver 0.0.0.0:8000 --insecure