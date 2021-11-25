
year=1918
mm='09'
    
if(year>=1700 and year<=1917):
    if(year % 4 == 0):
        dd=256-244
        print("{0}.{1}.{2}".format(dd,mm,year))
    else:
        dd=256-243
        print("{0}.{1}.{2}".format(dd,mm,year))
        
if(year == 1918):
    dd=256-230
    print("{0}.{1}.{2}".format(dd,mm,year))        
    
if(year>=1919 and year<=2700):
    if(year%4==0 and year%100!=0):
        dd=256-244
        print("{0}.{1}.{2}".format(dd,mm,year))
    else:
        dd=256-243
        print("{0}.{1}.{2}".format(dd,mm,year))