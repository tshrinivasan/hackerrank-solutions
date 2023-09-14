#Create a function which can take two lines of list as input, line one has the list of dates in the format DD:MM:YYY and the line two has list of days need to be added with dates. The function should perform addition between the days and the dates, then print the sorted list of dates in ascending order.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import datetime
def sortDate():
    #Write your code here
    s = sys.stdin
    result_date_list = []
    input_list = []
    for line in s:
        input_list.append(line.strip())
        
    #print(input_list)
    dates = input_list[0].split(" ")
    days=input_list[1].split(" ")
    #print(days)
    counter = 0
    for date in dates:
     #   print(date)
     #   print(days[counter])
        current_date_temp = datetime.datetime.strptime(date, "%d-%m-%Y")
        newdate = current_date_temp + datetime.timedelta(days=int(days[counter].strip()))
        result_date = datetime.datetime.strftime(newdate, "%d-%m-%Y")
      #  print(result_date)
        result_date_list.append(result_date)
        counter = counter + 1
        
   # result = result_date_list.sort(key = lambda date: datetime.datetime.strptime(date, '%d-%m-%Y'))
   
    sortedDates = sorted([datetime.datetime.strptime(item, '%d-%m-%Y') for item in result_date_list])
    #print(sortedDates)
    for item in sortedDates:
        print(item.strftime('%d-%m-%Y'))
    #print(result)
    

if __name__ == "__main__":
    sortDate()
