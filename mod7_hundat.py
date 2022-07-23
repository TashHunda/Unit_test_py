import unittest
import datetime

def fetchSymbol():
    userChoice = input.isalpha("Enter the stock symbol you are looking for: ")
    if userChoice.isalpha() == True and len(userChoice) == 7 and userChoice.isupper() == True: # symbol check 
        return userChoice.upper()
    else:
        print("Invalid Symbol Try Again") 
def chartType():
    try:
        chart_type = int(input("Chart Type 1 or 2: ")) 
        if chart_type == 1 or chart_type == 2:  
         print("Valid Chart Type") 
        else:
         print("Invaild Chart Type")  
    except ValueError:
         print("\nError: Please only enter 1 or 2\n") 

def get_time_series():
 try:
      time_series = int(input("Select the Time Series of the chart you want to Generate: ")) # Ask user for input
      if time_series > 0 and time_series < 5:  
       print("Valid Time Series") 
      else:
       print("This is an unacceptable response, enter a valid value")  
 except ValueError:
     print("This is an unacceptable response, enter a valid value") 

#begin date
def beginDates():    
    try:
        beginDate = input(" Please enter start date (YYYY-MM-DD) format: ") 
        date_format = '%Y-%m-%d'

        beginDate = datetime.datetime.strptime(beginDate, date_format) #date format check 
        print("Date format is accepted") 
    except ValueError:
        print("Date format not accepted, please enter date (YYYY-MM-DD) format: ") 

#end date
def endDates():
    try:
        endDate = input("Please Enter end date in (YYYY-MM-DD) format: ") 
        date_format = '%Y-%m-%d'
        
        endDate = datetime.datetime.strptime(endDate, date_format) #date format check
    except ValueError:
        print("Invaild date format, please enter date in (YYYY-MM-DD) format: ") 

class Teststock_visualizer(unittest.TestCase):

 def test_fetchSymbol(self):
      self.assertRaises(Exception, fetchSymbol, True)

 def test_chartType(self):
      self.assertRaises(Exception, chartType, 1 or 2)

 def  test_get_time_series(self):
      self.assertRaises(Exception, get_time_series, 0-5)

 def  test_beginDates(self):
      self.assertRaises(Exception, beginDates, True)

 def  test_endDates(self):
      self.assertRaises(Exception, endDates, True)
    

if __name__ == '__main__':
    unittest.main()