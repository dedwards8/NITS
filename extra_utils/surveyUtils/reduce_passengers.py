"""
Takes survey data that is loaded in a reduces the count.
"""

from utils.variety_utils import log_traceback
from NITS.hermes import models
if __name__=='__main__':
    """

    """
      
    survey_passengers = models.SurveyPassenger.objects.all()
    count = survey_passengers.count()

    index = 0
    for passenger in survey_passengers:
        print index
        index += 1
        if not (((passenger.id+1) % 2) == 0):
            passenger.delete()
            print 'deleting'


    survey_passengers = models.SurveyPassenger.objects.all()  

    print 'The number of passengers was reduced from ' + str(count) + ' to ' + str(survey_passengers.count())


    
    
