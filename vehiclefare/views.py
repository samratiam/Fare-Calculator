from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def calculate(request):
    
    # Creating list for each group of rows with similar surge and service charge
    list1 = ['05:00','06:00']
    list2 = ['07:00','08:00','08:30','09:00','09:30','10:00','10:30','11:00','12:00','13:00','14:00',
             '15:00','16:00','16:30','17:00','18:00','19:00','19:30','20:00']
    list3 = ['21:00','22:00']
    list4 = ['23:00']
    list5 = ['24:00','01:00','02:00','03:00','04:00'] # last 5am part row isn't included as it was already in first row
    
    
    if request.method == 'POST':
        distance = request.POST['distance']
        time = request.POST['time']
        
        # Converting time to str format to compare with lists
        time = str(time)
        distance = float(distance)
        
        # Initial fare and km rate from the table is fixed for all
        initial_fare = 25
        km_rate = 14
        
        # Comparing the time with each list and calculating final price
        if time in list1:
            surge_charge = 10
            service_charge = 0
        
        elif time in list2:
            surge_charge = 0
            service_charge = 0
        
        elif time in list3:
            surge_charge = 15
            service_charge = 0
        
        elif time in list4:
            surge_charge = 20
            service_charge = 0
        
        elif time in list5:
            surge_charge = 50
            service_charge = 5
        
        else:
            # If input value doesn't include in any list raise the exception
            raise Exception("Invalid Input")
        
        rate_after_surge = km_rate + (surge_charge/100)*km_rate
        without_service_charge = initial_fare + rate_after_surge * distance 
        final_price = without_service_charge + (service_charge/100) * without_service_charge
                
        context = {'final_price':final_price}
        return render(request,'calculate.html',context)
        
    return render(request,'calculate.html')