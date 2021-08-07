# Project: Create a Tebleau Story
### Matthew Dolder
### 8/7/2021


## Summary: 

Looking at flight delay data provided by Bureau of Transportaion Statistics from 2003 and 2021, I want to show 
which airports have the most security delays and within those airports, which airlines are most affected.  I also want to show if the situation is 
improving year over year.
 

## Design: 

### First Draft Dashboard
https://public.tableau.com/views/SecurityDelaysbyAirport-Dashboard/FlightsDelayedbySecurity?:language=en-US&:retry=yes&publish=yes&:display_count=n&:origin=viz_share_link

1. The common feedback was performance.  It is painfully slow on Tableau Public with the Raw dataset.  I performed some data wrangling to reduce the number of records and fields.  See main.py.  This improved performance drastically. 
2. I made the 'Security Delay' field plural. 
3. I removed the 5-20 slider and focused on just the top 5 airports. 
4. My youngest daughter didn't like that the same airline name shows up in multiple bubbles.  The fact that they were different years was not obvious. I removed the year scale from the bubbles and color coded them 
based on airline. 

### First Draft Story
https://public.tableau.com/views/AirportSecurityDelays-Story/SecurityDelays?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link

Based on second round feedback and my own observations, I made the following changes:
1. I added a field in the source data called top_five (true, false) and removed the Top N in/out calculation.  This makes the story perform better on Tableau public. 
2. I displayed all airports on the map with top 5 legend and a list to the right.  It makes the map more cluttered, but gives a sense of scale. It also allows some interactivity if you want to compare several airports, you can multi-select and the table on the right will adjust.  
3. I finally gave up on the bubbles.  The size of the bubble is confusing, the position of small bubbles if confusing, and the colors conflict with the True/False legend.  I switched to a treemap instead. 

### Final Draft Story
https://public.tableau.com/views/AirportSecurityDelays-StorySecondDraft/SecurityDelays?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link


## Feedback: 
My two teenage daughters provided feedback first on a single dashboard:

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

I asked for second round of feedback on the story draft:

### Daughter 1
- Splitting the data up into differeng graphs was really helpful
- Everything runs smoothly and responds on click now!
- Colors :)
- The last graph only displays ATL when viewing the world map, not every airport collectively
- Clicking outside a point (both on the map and in the data graphs) to deselect and return to world view works on the third graph, but neither of the others. You have to reclick points to deselect them in the first two.

### Wife
- on first page, I clicked a city and expected something to happen and nothing happened except the city was highlighted.
- on the second page, I understand the bubbles with the airline names on them, but I don't understand what the purpose of the smaller bubbles is.
- why does Southwest not show up with any security delays out of DFW?
- why are the biggest airports the ones with the worst track record for delays?
- why was the worst year 2006 and not 2003?

### Myself
- I see some script errors and wonky behavior on the Tableau public site which does not occur in the desktop version.  I suspect the TOP N in/out filter combined with the actions are a bit much for the free public website.   

## Resources: 

The raw data was downloaded from bts.gov.
I choose All carriers & All airports from June 2003 to May 2021.
https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp
 
### References:
- https://help.tableau.com/current/pro/desktop/en-us/sortgroup_sets_topn.htm
- https://kb.tableau.com/articles/howto/creating-dynamic-titles-based-on-filters
- https://kb.tableau.com/articles/howto/removing-abc-placeholder-text
- https://www.tableau.com/learn/tutorials/on-demand/-dashboard-interactivity-using-actions
- https://docs.python.org/3/library/csv.html
- https://docs.python.org/3/library/sqlite3.html
- https://stackoverflow.com/questions/10522830/-how-to-export-sqlite-to-csv-in-python-without-being-formatted-as-a-list
- https://www.sqlite.org/inmemorydb.html

## Files:

| File        | Description |
| ----------- | ----------- |
| README.md   | This document  |
| main.py     | Data Wrangling |
| 418421584_52021_5443_airline_delay_causes.zip    | Contains a single CSV file. Used by Final Draft Tableau story.  Output of main.py |

