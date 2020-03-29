#!/usr/bin/python
# -*- coding: utf-8 -*-

#
#The solution is pretty simple folks.
#Create a .htaccess file in the directory where the calendar files are located.
#
#include this line:
#
#AddType 'text/calendar; charset=UTF-8' .ics
#
#works like charm :) btw this problem was nagging me for quite a while, too.
#


import sys
import codecs
import textwrap
import collections

from icalendar import Calendar, Event

crscode="DM559";


def where_is_room(r):
    if r=="IMADA terminalrum":
        return "http://www.sdu.dk/Information_til/Studerende_ved_SDU/Campusguide/It/Software/NAT/imada"
    elif r=="IMADA Terminalrum":
        return "http://www.sdu.dk/Information_til/Studerende_ved_SDU/Campusguide/It/Software/NAT/imada"
    else:
        return "http://imada.sdu.dk/api/locations/"+r


infile = codecs.open(sys.argv[1], mode='r',encoding='utf-8')
outfile = codecs.open(sys.argv[2], mode='w',encoding='utf-8')


#dic=collections.defaultdict(dict)
dic=collections.OrderedDict()

max_w=0
min_w=56
for line in infile:
    
    pieces = map(lambda x: x.strip(), line.rstrip().split("\t"))
    print pieces
    intervals = pieces[5].split(",")
    weeks=[]
    for i in intervals:
        w=i.split("-")
        if len(w)>1:
            weeks+=range(int(w[0]),int(w[1])+1)
        else:
            weeks+=[int(w[0])]
    if max(weeks)>max_w:
        max_w=max(weeks)
    if min(weeks)<min_w:
        min_w=min(weeks)

    k=pieces[2][:3]+", "+pieces[3] #+", "+pieces[4]
    for w in weeks:
        what={}
        what[w]=[pieces[0], pieces[1], pieces[3], pieces[4], pieces[2]]   
        if k not in dic:
            dic[k]=what
        else:
            print "problems"
            dic[k].update(what)

max_w=max_w+1

s = textwrap.dedent("""\
<table  class="Schedule" id="collapse">
<caption></caption>
<colgroup><col class="c1" />
""")
s=s.replace("collapse",sys.argv[2][:-5],3)

for w in range(min_w,max_w):
    s+=textwrap.dedent("""<col class="left" />""")
s+="<thead>"

s+=textwrap.dedent("""<tr><th scope="col" >Week</th>""")
for w in range(min_w,max_w):
    s+=textwrap.dedent("""<th scope="col" >""")
    s+=str(w)+"</th>"

s+="</tr></thead><tbody>"
outfile.write(s)



day2num = {
    u'Mandag': 0,
    u'Tirsdag': 1,
    u'Onsdag': 2,
    u'Torsdag': 3,
    u'Fredag': 4,
    u"Lørdag".encode("utf-8"): 5,
    u'Sondag': 6
    }

shortday2num = {
    u'Man': 0,
    u'Tir': 1,
    u'Ons': 2,
    u'Tor': 3,
    u'Fre': 4,
    u"Lør".encode("utf-8"): 5,
    u'Son': 6
    }



#print min_w,max_w;
ks=dic.keys()
#print dic.items()
ks_sorted = sorted(ks,key=lambda x : (shortday2num[x.split(",")[0]], x.split(",")[1]) )

for k in ks_sorted:
    line=""
    line= textwrap.dedent("""\
    <tr><td class="slot"><b>""")
    line+=k
    line+="</b></td>"
    #        Man, 10-12,  <a href="http://vejviser.sdu.dk/opslag?lid=1131" class="Schedule">U27A</a>
    
    #        <td class="left"></td><td class="left">Lecture</td>
    #        <td class="left">Lecture</td><td class="left">Lecture</td><td class="left">Lecture</td><td class="left">Lecture</td><td class="left">Lecture</td><td class="left"></td></tr>
        
    for w in range(min_w,max_w):
        tmp=textwrap.dedent("""<td class="left">""")
        if w in dic[k]:
            tmp+=dic[k][w][1]+" ("+dic[k][w][0]+")"+"<br>"
            tmp+="<a style=\"font-size:smaller;align:right\" href=\""+where_is_room(dic[k][w][3])+"\">"
            tmp+="("+dic[k][w][3]+")</a>" #.encode("utf-8")
        tmp+="</td>"
        line+=tmp
    line+="</tr>"
    outfile.write(line)
outfile.write("</tbody></table>")
outfile.close()





## check is_dst there is still an issue: +1 always instead of +2 when daylight
def ical():

    cal = Calendar()
    from datetime import datetime, timedelta
    cal.add('prodid', '-//My calendar product//mxm.dk//')
    cal.add('version', '2.0')

    import pytz
    ## write here first Monday of the year
    cph=pytz.timezone('Europe/Copenhagen')
    #d1=datetime(2013,12,30,0,0,0,tzinfo=pytz.utc)
    d1=datetime(2013,12,30,0,0,0,tzinfo=cph)
    #d2.strftime("%A %d. %B %Y")

    for k in dic:
        for w in dic[k]:
            event = Event()
            event.add("CHARSET","utf-8")
            event.add('summary','DM545 '+dic[k][w][1]+' '+dic[k][w][3])
            setime = dic[k][w][2].split("-")
            day=dic[k][w][4].encode("utf-8")
            dts=timedelta(weeks=w-1, days=day2num[day.rstrip()], hours=int(setime[0]))
            dte=timedelta(weeks=w-1, days=day2num[day.rstrip()], hours=int(setime[1]))
            print k,w,setime,dts,(d1+dts)
            event.add('dtstart', (d1+dts))
            event.add('dtend', (d1+dte))
            event.add('dtstamp', datetime.now())
            #event['uid'] = k+", "+str(w) # '20050115T101010/27346262376@mxm.dk'
            event.add('uid', k+"+"+str(w)) # '20050115T101010/27346262376@mxm.dk'
            event.add('priority', 1)
    
            cal.add_component(event)

    
    calfile=sys.argv[2][:-5]+'.ics'
    print calfile
    f = open(calfile, 'wb')
    f.write(cal.to_ical())
    f.close()



# Handles in a different way the daylight time issue (should be more secure but the
# number of weeks may have to be adapted
def ical2():
    cal = Calendar()
    from datetime import datetime, timedelta
    cal.add('prodid', '-//My calendar product//mxm.dk//')
    cal.add('version', '2.0')

    import pytz
    ## write here first Monday of the year
    d1=datetime(2017,1,2,0,0,0,tzinfo=pytz.utc)
    cph=pytz.timezone('Europe/Copenhagen')
    #d2.strftime("%A %d. %B %Y")

    
    for k in dic:
        for w in dic[k]:
            if w<=13 or w>=44:
                offset=1
            else:
                offset=2
            event = Event()
            #event.add("CHARSET","UTF-8")
            event.add('summary',crscode+' '+dic[k][w][1]+dic[k][w][0][0:2]+' '+dic[k][w][3])
            setime = dic[k][w][2].split("-")
            day=dic[k][w][4].encode("UTF-8")
            dts=timedelta(weeks=w-1, days=day2num[day.rstrip()], hours=int(setime[0])-offset)
            dte=timedelta(weeks=w-1, days=day2num[day.rstrip()], hours=int(setime[1])-offset)
            print k,w,setime,dts,(d1+dts).astimezone(cph)
            event.add('dtstart', (d1+dts).astimezone(cph))
            event.add('dtend', (d1+dte).astimezone(cph))
            event.add('dtstamp', datetime.now())
            uid = k+", "+str(w) # '20050115T101010/27346262376@mxm.dk'
            uid = uid.replace(' ', '_').replace(',', '_')
            event['uid'] = uid
            event.add('priority', 1)
    
            cal.add_component(event)
    
    calfile=sys.argv[2][:-5]+'.ics'
    print calfile
    f = open(calfile, 'wb')
    f.write(cal.to_ical())
    f.close()

ical2()
