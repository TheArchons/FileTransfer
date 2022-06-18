#set shell := ["powershell.exe", "-c"] # uncomment to use powershell

startLocalWindows:
    z C:\Users\proga\Code\Github clones\FileTransfer
    git pull
    python manage.py runserver

migrateWindows:
    z C:\Users\proga\Code\Github clones\FileTransfer
    python manage.py makemigrations
    python manage.py migrate

startLocalFedora:
    cd /home/admin/FileTransfer
    git pull
    python3 manage.py runserver

startOnlineFedora:
    cd /home/admin/FileTransfer
    git pull
    nohup python3 -u manage.py runserver 0.0.0.0:8000 --insecure

migrateFedora:
    cd /home/admin/FileTransfer
    python3 manage.py makemigrations
    python3 manage.py migrate