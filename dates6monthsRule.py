
#%%

import datetime
import matplotlib.pyplot as plt



string_date_list = [
			["2013-08-02",  "2013-08-31"], 
			["2014-07-14",  "2014-09-15"],
	  	    ["2014-11-12",  "2014-11-28"],
	        ["2014-12-21",  "2015-01-25"],
	     	["2015-06-23",  "2015-08-23"],
			["2015-10-17",  "2015-11-06"],			
			["2016-04-24",  "2016-05-14"],
			["2016-07-12",  "2016-08-15"],
			["2017-07-25",  "2017-08-28"],
			["2017-09-10",  "2017-09-18"]
]

myTrip=[ [datetime.date]]

def subtract_years(dt, years):
    try:
        dt = dt.replace(year=dt.year-years)
    except ValueError:
        dt = dt.replace(year=dt.year-years, day=dt.day-1)
    return dt

def checkDatInDatesRange(x, sDate, eDate):
	sDate=datetime.datetime.strptime(sDate, "%Y-%m-%d")
	eDate=datetime.datetime.strptime(eDate, "%Y-%m-%d")
	
	if x>= sDate and x<=eDate:
		return (1)
	else:
		return (0)

def checkDayInTrip(day):
	
	for i, trp in zip(range(0, len1), string_date_list):
		
		res =checkDatInDatesRange(day, trp[0], trp[1])

		# print(day, olDay, res)		
		
		if res==1:
			# print(res)

			return(res)
	return(0)
		
		
def numTripDaysInRange(lfDay, rtDay):
	day=lfDay
	numDy=0
	while day <= rtDay:
		numDy += checkDayInTrip(day)				
		day += datetime.timedelta(days=1)	
	return(numDy)


#%%

totDays=0

for day in string_date_list:
	sDate=datetime.datetime.strptime(day[0], "%Y-%m-%d")
	eDate=datetime.datetime.strptime(day[1], "%Y-%m-%d")

	delta = eDate-sDate
	
	totDays+=delta.days

	print("date=", day, "TotNumDays=", totDays)


#%%

now=datetime.datetime.now()

res=checkDatInDatesRange(now, string_date_list[0][0], string_date_list[0][1])

len1=len(string_date_list)
olDay=subtract_years(now, 5)

print("OlDay = ", olDay)

#%%

# olDay=now - datetime.timedelta(days=188)

lDay=olDay
rDay=lDay+datetime.timedelta(days=188)

day=rDay

# olDay = day - datetime.timedelta(days = 188)
# day = now-datetime.timedelta(days=688)

numDy = 0
maxDay=0

time =[]
y = []

# while day <= rDay+ datetime.timedelta(days=10):
while day <= now:
	
	numDy = numTripDaysInRange(lDay, day)	

	maxDay = max(maxDay, numDy)

	y.append(numDy)
	time.append(day)

	lDay += datetime.timedelta(days=1)
	day  += datetime.timedelta(days=1)		
	
	# print(y,time)
	print(numDy, maxDay, lDay.date(),day.date())
	numDy=0

print(time)
print(y)

plt.plot(y, y)
# plt.plot_date(x=time, y=y)
plt.show()	
	

# res = numTripDaysInRange(now-datetime.timedelta(days=688), now)
# print("tot = ", res)

#print("olday=", olDay, "\n", "now=", now,"\n", 
#	now - datetime.timedelta(days=1))
