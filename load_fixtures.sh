source env/bin/activate

for FILE in ./fixtures/*; do python -Xutf8 manage.py loaddata $FILE; done;