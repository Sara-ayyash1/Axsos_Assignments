from django.shortcuts import render
from time import gmtime, strftime
# Create your views here.
    
# def index(request):
#     context = {
#         #"time": strftime("%Y-%m-%d %H:%M %p", gmtime())
#         #"time": strftime("%b %d, %Y %I:%M %p", gmtime()),
#         "time": strftime("%A, %d %b %Y %H:%M:%S", gmtime())
#     }
#     return render(request,'index.html', context)

#---------------------------

# from datetime import datetime  
# def index(request):
#     now = datetime.now()
#     current_time = now.strftime("%b %d, %Y %I:%M %p")
    
#     context = {
#         "time": current_time
#     }
#     return render(request, 'index.html', context)



#---------------------------

from django.utils import timezone  

def index(request):
    local_time = timezone.now()
    
    context = {
        "time": local_time.strftime("%b %d, %Y %I:%M %p")
    }
    return render(request, 'index.html', context)










#---------------------------

# from datetime import datetime
# date_string = "Jun 1 2005  1:33PM"

# strptime => String Parse Time
# date_object = datetime.strptime(date_string, "%b %d %Y %I:%M%p")

# print(date_object)

#---------------------------

# %b: اسم الشهر المختصر (مثل: Jun, Jan, Feb).
# %d: اليوم بالشهر كرقمن (01 أو 1).
# %Y: السنة بأربع أرقام (2005).
# %I: الساعة بنظام 12 ساعة (من 01 لـ 12).
# %M: الدقائق (من 00 لـ 59).
# %p: مؤشر الوقت (AM أو PM).