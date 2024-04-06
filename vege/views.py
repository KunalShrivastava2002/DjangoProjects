from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required(login_url='/login/')
def reciepe(request):
    if request.method == "POST":

        data= request.POST

        reciepe_image= request.FILES.get('reciepe_image')
        reciepe_name= data.get('reciepe_name')
        reciepe_description= data.get('reciepe_description')

        Reciepe.objects.create(reciepe_image= reciepe_image,
                               reciepe_name= reciepe_name,
                               reciepe_description= reciepe_description)
        
        return redirect('/reciepe/')
    
    queryset= Reciepe.objects.all()

    if request.GET.get('search'):
        print(request.GET.get('search'))
        queryset = queryset.filter(reciepe_name__icontains=request.GET.get('search')) 

    
    context= {'reciepes':queryset}

        

    return render(request,'reciepe.html',context)

def update_reciepe(request,id):
    queryset= Reciepe.objects.get(id=id)

    if request.method == "POST":
        data= request.POST

        reciepe_image= request.FILES.get('reciepe_image')
        reciepe_name= data.get('reciepe_name')
        reciepe_description= data.get('reciepe_description')

        queryset.reciepe_name = reciepe_name
        queryset.reciepe_description =reciepe_description

        if reciepe_image:
            queryset.reciepe_image =reciepe_image

        queryset.save()

        return redirect('/reciepe/')


    context= {'reciepe':queryset}
    return render(request,'update_reciepe.html',context)


def delete_reciepe(request,id):
    queryset= Reciepe.objects.get(id=id)
    queryset.delete()

    return redirect('/reciepe/')

def login_page(request):

    if request.method== "POST":
        username =request.POST.get('username')
        password =request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Inavalid username')
            return redirect('/login/')
        user= authenticate(username=username, password= password)

        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/reciepe/')


    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    if request.method =="POST":
        first_name =request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        username =request.POST.get('username')
        password =request.POST.get('password')

        user= User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'Username alredy exists, try another username')
            return redirect('/register/')

        user = User.objects.create(first_name=first_name,
                                    last_name=last_name,
                                        username=username,
                                            )
        
        user.set_password(password)
        user.save()
        messages.info(request,'Account created successfully')


        return redirect('/register/')

    return render(request, 'register.html')

from django.db.models import Q,Sum

def get_student(request):
    queryset= Student.objects.all()
    


    if request.GET.get('search'):
        search= request.GET.get('search')
        queryset= queryset.filter(
            Q(student_name__icontains=search)|
            Q(department__department__icontains=search)|
            Q(student_id__student_id__icontains=search)|
            Q(student_email__icontains=search)|
            Q(student_address__icontains=search)|
            Q(student_age__icontains=search)
            )


    paginator = Paginator(queryset, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    return render(request, "report/students.html", {'queryset':page_obj})

# from .seed import generate_report_card
def see_marks(request, student_id):
    
    # Filter Subject_marks based on student_id
    queryset = Subject_marks.objects.filter(student__student_id__student_id=student_id)
    
    # Aggregate total marks
    total_marks = queryset.aggregate(total_marks=Sum('marks'))
    
    # Retrieve student details
    student = get_object_or_404(Student, student_id__student_id=student_id)
    student_name = student.student_name
    
    return render(request, "report/see-marks.html", {'queryset':queryset,'total_marks':total_marks,'student_name':student_name,})

