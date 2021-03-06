"""
Loads in survey data to the db
"""

from hermes import models
from utils.variety_utils import log_traceback
import datetime
from django.db import connection

@log_traceback
def insert_values(file_path):
    """
    """
    cursor = connection.cursor()
    fp = open(file_path)
    line = fp.readline()
    index_str = ''
    insert_str = "insert into hermes_surveypassenger(survey_id, start_lat, start_lng, end_lat, end_lng, time_of_request) values "
    values_str = '(%s,"%s","%s","%s","%s",%s),'

    cnt = 0
    values = ''
    while line:
        line = fp.readline()
        if line:
            cnt += 1
            line = line.strip("\r\n").replace('"', '').split(",")

            start_hour = int(line[1])
            start_minute = int(line[2])
            second = (start_hour - 7)*3600 + start_minute*60
            values += values_str % (line[0], line[4], line[5], line[7], line[8] ,second)
            
            if cnt >= 100:
                try:
                    if insert_str:
                        cursor.execute(insert_str + values.rstrip(",")+";")
                        
                except Warning:
                    pass
                cnt = 0
                values = ""
        else:
            try:
                if insert_str:
                    cursor.execute(insert_str + values.rstrip(",")+";")    
            except Warning:
                pass
    print 'Survey Passenger Data is Loadad'
   
    cursor.close()
    fp.close()
    return



if __name__=='__main__':
    """
    Loads in Survey Passenger Data
    """
      
    insert_values("./35xupSampleForBigScript1Miles.csv")
    
