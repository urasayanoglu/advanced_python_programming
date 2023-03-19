'''create initialized sample database'''

import sqlite3


example_db = "devicecontrol.db" 

schema = '''    
    CREATE TABLE IF NOT EXISTS measurements (
        fpath TEXT,
        device INTEGER,
        treatment TEXT,
        amplitude REAL)'''

conn = sqlite3.connect(example_db) #  create and connect
conn.execute(schema) # create data
conn.commit()
conn.close()

########################################################
#  initial data

conn = sqlite3.connect(example_db) #  reconnect
res = conn.execute("SELECT * from measurements").fetchall()
if not res:
    data1 = [
          {
              "fpath": "path/to/file/one.dat",
              "device": 1,
              "treatment": "Control",
              "amplitude": 50.5,
          },
          {
              "fpath": "path/to/file/two.dat",
              "device": 2,
              "treatment": "Control",
              "amplitude": 76.5,
          },
          {
              "fpath": "path/to/file/three.dat",
              "device": 1,
              "treatment": "Experimental",
              "amplitude": 5.5,
          },
      ]

    data2 = [
          (
              "path/to/file/four.dat",
              1,
              "base",
              0.05,
          ),
          (
              "path/to/file/five.dat",
              2,
              "Control",
              80.2,
          ),
          (
              "path/to/file/six.dat",
              2,
              "base",
              0.7,
          ),
      ]

    #  fill in initial data
    #  one row
    conn.execute('''
        INSERT INTO measurements (fpath, device, treatment, amplitude)
            values ("path/to/file/one.dat", 0, "base", 0.002)''')

    #  several rows using :par 
    conn.executemany(
        '''
        INSERT INTO measurements (fpath, device, treatment, amplitude)
            VALUES(:fpath, :device, :treatment, :amplitude)''', data1)

    #  several rows using ?
    conn.executemany(
        '''
        INSERT INTO measurements (fpath, device, treatment, amplitude)
            VALUES(?, ?, ?, ?)''', data2)

    conn.commit()
conn.close()

##########################################################
conn = sqlite3.connect(example_db) #  reconnect
conn.row_factory = sqlite3.Row #  use rowfactory for connection

result = conn.execute("SELECT * from measurements").fetchall()

# using rowfactory to create a list of rows as a dictionaries
resultlist = [{k : item[k] for k in item.keys()} for item in result]

for item in resultlist:
    for key, value in item.items():
        print(f'{key}: {value}')
    print()
    
conn.close()
                


