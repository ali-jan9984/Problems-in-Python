from datetime import date,datetime,timedelta
GIGASECONDS = 1e9
def add(moment):
    if isinstance(moment,date) and not isinstance(moment,datetime):
        dt = datetime(moment.year,moment.month,moment.day,0,0,0)
    else:
        dt = moment
    return dt + timedelta(seconds=GIGASECONDS)
    
