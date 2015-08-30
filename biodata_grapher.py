#!/usr/bin/python2.7
"""
Biodata_grapher
2015-08-30
"""

import glob
import csv
import os
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
import traceback


for filename in glob.glob('*_biodatalogger_readings.csv'):
    filename_png = filename.replace('.csv', '.png')
    if os.path.exists(filename_png):
        print "Skipping:", filename, "since png file already exists"
        continue
    y_data = []
    x_data = []    
    with open(filename, 'r') as csvfile:
        tempreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        try:
            for row in tempreader:
                dateinfo, celsius, fahrenheit = row
                dateinfo = datetime.strptime(dateinfo, "%Y-%m-%d %H:%M:%S.%f")
                day = dateinfo.strftime("%Y-%m-%d")
                x_data.append(dateinfo)
                #y_data.append(fahrenheit)
                y_data.append(celsius)
        except:
            print "file:", filename
            print "row:", row 
            traceback.print_exc()
            
    #plt.plot(x_data, matplotlib.dates.date2num(y_data))
    matplotlib.pyplot.plot_date(x_data,y_data) 
    #plt.ylabel('Temp (F)')
    plt.ylabel('Temp (C)')
    plt.title('Temperature for ' + day)
    plt.xlabel('Time')
   
    plt.gcf().autofmt_xdate()
    plt.savefig(filename_png)
    plt.show()
