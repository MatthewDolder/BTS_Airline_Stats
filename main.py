#!/usr/bin/env python3.8
### Matthew Dolder
### 08/06/21
### Read BTS flight data from csv, modify and write. 

import csv
import sqlite3

def setupdb(dbname):
    #https://docs.python.org/3/library/sqlite3.html
    con = sqlite3.connect(dbname)

    cur = con.cursor()

    createtbl = '''create table flights (\
                year int,month int,carrier,carrier_name varchar(100),airport char(3),airport_name varchar(100),security_delay int)'''
    
    cur.execute(createtbl)

    createtbl = '''create table flights_tidy (\
                year int,carrier,carrier_name varchar(100),airport char(3),airport_name varchar(100),security_delay int, top_five varchar(5))'''

    cur.execute(createtbl)
    con.commit
    cur.close()

    return con

def importdata(infile,con):

    cur = con.cursor()
    sqlintro = 'insert into flights (year,month,carrier,carrier_name,airport,airport_name,security_delay) values ('
    sqloutro = ');'
    sql = ''

    #inflights = pd.read_csv(infile, header=0).to_dict()
    #print(inflights)
    #for f in inflights:
    #    print(f['year'])
    #"year"," month","carrier","carrier_name","airport","airport_name","arr_flights","arr_del15","carrier_ct"," weather_ct",
    # "nas_ct","security_ct","late_aircraft_ct","arr_cancelled","arr_diverted"," arr_delay"," carrier_delay","weather_delay",
    # "nas_delay","security_delay","late_aircraft_delay",

    with open(infile,newline='') as csvfile:
        inflights = csv.reader(csvfile,delimiter=',',quotechar='"')
        i = 0
        for f in inflights:
            security_delay = f[19]
            if (security_delay == 'NaN') or (security_delay == ''):
                security_delay = '0'
            
            if (i > 0): #skip header
                sql = f[0] + ',' + f[1] + ',\'' + f[2] + '\',\'' + f[3] + '\',\'' + f[4] + '\',\'' + f[5].replace('\'','') + '\',' + security_delay
                sql = sqlintro + sql + sqloutro
                #print (sql)
                cur.execute(sql)
            i += 1
        
    con.commit
    cur.close()

    
def squeezedata(con):

    #remove month and remove values which are zero
    cur = con.cursor()

    #Top 5 airports by delays
    sql = "insert into flights_tidy (year,carrier,carrier_name,airport,airport_name,security_delay,top_five) \
           select year,carrier,carrier_name,airport,airport_name,sum(security_delay),\'TRUE\' \
           from flights \
           where security_delay > 0 \
           and airport in ('LAX','PHX','DFW','ATL','ORD') \
           group by year,carrier_name,airport,airport_name"
    
    cur.execute(sql)

    #The rest
    sql = "insert into flights_tidy (year,carrier,carrier_name,airport,airport_name,security_delay,top_five) \
           select year,carrier,carrier_name,airport,airport_name,sum(security_delay),\'FALSE\' \
           from flights \
           where security_delay > 0 \
           and airport not in ('LAX','PHX','DFW','ATL','ORD') \
           group by year,carrier_name,airport,airport_name"

    cur.execute(sql)

    con.commit()
    cur.close()

def outputdata(outfile,con):

    #Write flights_tidy out to csv
    #https://stackoverflow.com/questions/10522830/how-to-export-sqlite-to-csv-in-python-without-being-formatted-as-a-list
    cur = con.cursor()
    cur.execute ('select year,carrier,carrier_name,airport,airport_name,security_delay,top_five from flights_tidy order by year,airport_name')

    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['year', 'carrier','carrier_name', 'airport', 'airport_name', 'security_delay','top_five'])
        for flight in cur.fetchall():
            writer.writerow([flight[0],flight[1],flight[2],flight[3],flight[4],flight[5],flight[6]])
    
    f.close()
            
def main():
    infile = '418421584_52021_5443_airline_delay_causes.RAW.csv'
    outfile = '418421584_52021_5443_airline_delay_causes.csv'        
    #db = 'security_delays_2003_2021.db'
    #https://www.sqlite.org/inmemorydb.html
    db = ":memory:"  
    
    #get database connection
    print("setting up database\n")
    con = setupdb(db)
    #import from csv into database
    print("import csv to database\n")
    importdata(infile,con)
    #select and group by
    print("Processing Data\n")
    squeezedata(con)
    #write the table out to csv
    print("Writing to CSV\n")
    outputdata(outfile,con)
    print("Bazinga.  See " + outfile + " for results\n")
    
                



if __name__ == "__main__":
    main()