# you can also use with clause, it will close cursor.



import psycopg2                        # import modules (install psycopg2)
import psycopg2.extras

hostname = "localhost"                 #connection variables
database = 'employees'
username = 'postgres'
pwd = '123456'
port_id = 5432
conn = None
cur = None

try:                                   # try connection with error handling
    conn = psycopg2.connect(           # connection variable reassign
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port= port_id
    )
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)     # open cursor
    
    cur.execute('DROP TABLE IF EXISTS employee')                     # replaces existing table 
    
                                                                     # column variables
    create_script = ''' CREATE TABLE  IF NOT EXISTS employee (       
                            id     int PRIMARY KEY,
                            name   varchar(40) NOT NULL,
                            skills varchar(200) NOT NULL,
                            salary int NOT NULL )'''
    cur.execute(create_script)                                       # run function
                                            
                                                                     # inserting rows / data into dictionary
    insert_script = 'INSERT INTO employee (id,name,skills, salary) VALUES (%s, %s, %s, %s)' 
    insert_values = [(1, 'jay', 'Python', 20000),(2, 'Lee', 'solidity', 25000),(3, 'JLT', 'typescript', 30000)]
    for record in insert_values:                   
        cur.execute(insert_script, record)
        
    # update_script ='UPDATE employee SET salary = salary + (salary * 0.5)'
    # cur.execute(update_script) 
    
    # delete_script = 'DELETE FROM employe WHERE name = %s'
    # delete_record = ('',)
    # cur.execute(delete_script, delete_record)   
           
    cur.execute('SELECT * FROM EMPLOYEE')              # calling data from table to terminal display         
    for record in cur.fetchall():                      # data fetch, could use fetchone() ect
        print(record['name'], record['salary'])        # print calls
        #print(record[1], record[2])
        #print(record)
        #print(record["id"], record['name'], record['skills'])
        
        conn.commit()                            # runs new data instance into tables
        
except Exception as error:                       # error handling
    print("Function not completed")
finally:
    if cur is not None:                          # closing cusor and connection
        cur.close()
    if conn is not None:   
        conn.close()