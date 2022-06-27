from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import Trainer_Register, CityInfo, Trainer_Assign, CourseInfo


def home(request):
    return render(request, 'login.html')


# Geting data from login template and authenticate
def logread(request):
    UserName = request.POST['txtname']
    Password = request.POST['psw']
    user = authenticate(username=UserName, password=Password)
    print(user)
    try:
        if user is not None:
            if user.is_superuser:
                login(request, user)
                request.session['AdminId'] = user.id
                request.session['AdminUsername'] = str(user.username).upper()
                return render(request, 'AdminHome.html', {'AdminUsername': request.session['AdminUsername']})
        else:
            t1 = Trainer_Register.objects.get(Trainer_Name=UserName, Trainer_Password=Password)
            if t1 is not None:
                request.session['tid'] = t1.id
                request.session['tname'] = str(t1.Trainer_Name).upper()
                return render(request, 'TrainerHtml\Trainer_Home.html', {'data': request.session['tname']})
    except ObjectDoesNotExist:
        return HttpResponse('Invalid Credentials')


def logout_view(request):
    """""  User_Name = request.POST["txtname"]
    user = authenticate(request, username=User_Name)"""
    logout(request)
    return redirect('home')


# --------------------------------------------------------------------------------------------------------------------------------------------------------
#        Trainer
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


def trainer_home(request):
    return render(request, 'templates\\TrainerHtml\\Trainer_Home.html')


# TRainer  Registration
# To bind cities from Data base table
# To retrive data from database to Register template
def trainerGet(request):
    city = CityInfo.objects.all()
    return render(request, 'Register_Form.html', {'Citylist': city})


# to saving Register template data to Data_base
def trainerSet(request):
    t1 = Trainer_Register()
    t1.Trainer_Name = request.POST['t_txt']
    t1.Trainer_Age = request.POST['age']
    t1.Trainer_Phone = request.POST['ph']
    t1.Trainer_Password = request.POST['psw']
    t1.Trainer_Email = request.POST['email']
    t1.Trainer_city = CityInfo.objects.get(City_Name=request.POST['ddlCity'])
    t1.save()

    return redirect('home')


def batch_details(request):
    b1 = Trainer_Assign.objects.all()
    return render(request, 'TrainerHtml\\Batch_details.html', {'batch': b1})


# --------------------------------
#          Admin
# ---------------------------------
# ------------------------------------
# Admin will assign batch for trainer
# ------------------------------------

def admin_home(request):
    return render(request, 'AdminHome.html')


# Retriving Data from Database to Trainer_details template
def trainer_details(request):  # Trainer details
    t1 = Trainer_Register.objects.all()
    query = request.POST.get('q','')
    if query:
        t1 = Trainer_Register.objects.filter(Trainer_Name__icontains=query)
    # listAllTrainerDetailes = Trainer_Assign.objects.filter(tn)
    return render(request, 'Trainer_details.html', {'data': t1})


# Saving Data from AssignDetails template
def dataAssignget(request):
    c1 = Trainer_Assign()
    c1.tname = Trainer_Register.objects.get(Trainer_Name=request.POST['ddlt'])
    c1.tbatch_no = request.POST['btc']
    c1.course = CourseInfo.objects.get(Course_Name=request.POST['ddlc'])
    c1.date = request.POST['date']
    c1.save()
    return redirect('assign')


# Retriving Data from database to template
def dataAssignset(request):  # assigned batch details
    tname = Trainer_Register.objects.all()
    course = CourseInfo.objects.all()
    return render(request, 'AssignDetails.html', {'Namelist': tname, 'courselist': course})


def delete_batch(request, id):
    t1 = Trainer_Assign.objects.get(id=id)
    t1.delete()
    return redirect('batchd')


def update_batch(request, id):  # update the batch details
    t1 = Trainer_Assign.objects.get(id=id)
    t2 = Trainer_Register.objects.all()
    c1 = CourseInfo.objects.all()

    if request.method == 'POST':
        t1.tname = Trainer_Register.objects.get(Trainer_Name=request.POST['ddlt'])
        t1.tbatch_no = request.POST['btc']
        t1.course = CourseInfo.objects.get(Course_Name=request.POST['ddlc'])
        t1.date = request.POST['date']
        t1.save()
        return redirect('batchd')

    return render(request, 'Update_Batch.html', {'Namelist': t2, 'Courselist': c1, 'data': t1})

# Sorting data
