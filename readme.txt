For installation and function in Python: Windows os 
install Postgresql.
postgresql,will come with "pdAdmin4". open it. pgAdmin will ask for your master password
when you installed posgresql.  
right click on databases, create new data base. Prompt for database name, localhost(connection), password port"5432".

install VScode.
install: pip install psycopg2. (if pip not installed, complete pip installation).

open VScode.
open terminal to prompt. verify you are in the right folder.
install postgresql exstention in vs code.
connect postgresql database by using  command pallet, or + sign on exsteinsion , add new connection .
follow prompts. 
open folder - postgres.py(after unzipping) This folder has a file like a new query(conect.py)
--If code executed here, the included files will create a working TABLE. 
or-
adjust variables in code to add or (to) data base.
run python code in the connect.py file.
If no errors show, you are connected and table will populate
watch print calls for errors in terminal window.

Now in pgAdmin, use the query tool to access table.
type the following script in query tool.
SELECT * FROM eployees;    --will show table in lower window. CONGRATULATIONS! :) . 
