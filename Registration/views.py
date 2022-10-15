from django.shortcuts import render
from django.http import HttpResponse
from Registration.models import Course, Batch , Student

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to Prime Intuit Registration form</h1>")
def Home(request):
    #return HttpResponse("<h1>Welcome to Prime Intuit Home Page</h1>")
    #my_dict = {'insert_me' : "I am a text from registration/views.py from sub template"}

    batch_list = Batch.objects.raw('select * from Registration_Batch where start_date > "2021-01-01" ')
    data_dict = {'access_record' : batch_list, 'insert_me' : "I am a text from registration/views.py from sub template"}



    return render(request,'Registration/index.html',context=  data_dict)

