# Project: Create a Tebleau Story
### Matthew Dolder
### 8/5/2021


## Summary: 

Looking at flight delay data provided by Bureau of Transportaion Statistics from 2003 and 2021, I want to show 
which airports have the most security delays and within those airports, which airlines are most affected each year. 
I chose a map to show the top (5-20) airports and bubbles to show the airlines and year. My finding is that the following 5 airports have the most security delays:
- LAX
- PHX
- DFW
- ATL
- ORD

Withinin these cities, the airlines most affected vary over the years.  DFW is an exception as American Airlines is consistantly the most affected since 2003. 

## Design: 

### First Draft (slow)
https://public.tableau.com/views/SecurityDelaysbyAirport-Dashboard/FlightsDelayedbySecurity?:language=en-US&:retry=yes&publish=yes&:display_count=n&:origin=viz_share_link

The common feedback was performance.  It is painfully slow on Tableau Public with the Raw dataset.  I performed some data wrangling to reduce the number of records and fields.  See main.py.  This improved performance drastically. 

I made the 'Security Delay' field plural. 

I changed the position of the 5-20 slider

My youngest daughter didn't like that the same airline name shows up in multiple bubbles.  The fact that they were different years was not obvious. I changed the label to have year first and just the airline symbol second. 

### Final Version
https://public.tableau.com/views/SecurityDelaysbyAirport-DashboardpostFeedback/FlightsDelayedbySecurity?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link

## Feedback: 
My two teenage daughters provided feedback:

### Daughter 1

- Slider text is difficult to read
- Responds slowly
- Ensure that the keep only/exclude function on click works on the world map and not just the cities
- Define security delay (Also maybe change the 'Security Delay' text on hover to 'Security Delays')
- UI is smooth and enjoyable
- Lots of data (That's cool)

### Daughter 2

- very slow at the beginning when you start working with it
- put names onto the other airports?
- group actual security delays all together instead of apart?
- dont put same name on bubble, just put what year it occured so people might not be confused

## Resources: 

The raw data was downloaded from bts.gov.
I choose All carriers & All airports from June 2003 to May 2021.
https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp
 
### References:
- https://help.tableau.com/current/pro/desktop/en-us/sortgroup_sets_topn.htm
- https://www.tableau.com/learn/tutorials/on-demand/-dashboard-interactivity-using-actions
- https://docs.python.org/3/library/csv.html
- https://docs.python.org/3/library/sqlite3.html
- https://stackoverflow.com/questions/10522830/-how-to-export-sqlite-to-csv-in-python-without-being-formatted-as-a-list
- https://www.sqlite.org/inmemorydb.html

## Files:

### README.md
this file

### 418421584_52021_5443_airline_delay_causes.RAW.zip
Raw data dump from bts.org.  CSV format.

### 418421584_52021_5443_airline_delay_causes.zip
Wrangled data used for Tableau.  CSV format. Output from main.py.

### main.py
data wrangling

### bts_search_page.png
screenshot of query on bts.gov to download raw data. 