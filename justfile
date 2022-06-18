#set shell := ["powershell.exe", "-c"] # uncomment to use powershell

startOnlineFedora:
    cd /home/admin/FileTransfer
    git pull
    nohup python3 -u manage.py runserver 0.0.0.0:8000 --insecure

startLocalFedora:
    cd /home/admin/FileTransfer
    git pull
    python3 manage.py runserver

migrateFedora:
    cd /home/admin/FileTransfer
    python3 manage.py makemigrations
    python3 manage.py migrate

startLocalWindows:
    z C:\Users\proga\Code\Github clones\FileTransfer
    git pull
    python manage.py runserver

migrateWindows:
    z C:\Users\proga\Code\Github clones\FileTransfer
    python manage.py makemigrations
    python manage.py migrate