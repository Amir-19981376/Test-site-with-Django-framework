from django.shortcuts import render
from .models import Course
from django.shortcuts import redirect


def courses_list(request):
    print('amir from list')
    courses = Course.objects.all()

    return render(request, 'courses_app/courses_list.html',context={'courses_list':courses})

def course_detail(request,id):
    course = Course.objects.get(id=id)
    course.views +=1
    if course.situation==True:
        course.situation=False
    else:
        course.situation=True

    course.save()
    return render(request, 'courses_app/course_detail.html',context={'course':course})

def add_course(request):
    t= request.GET.get('title')
    d=request.GET.get('description')
    # print(t,d)
    if t and d:
        Course.objects.create(title=t, description=d)
        # return redirect('/course/list')


    if request.method == 'POST':
        t=request.POST.get('title')
        d=request.POST.get('description')
        Course.objects.create(title=t, description=d)



    return render(request, 'courses_app/add_course.html')