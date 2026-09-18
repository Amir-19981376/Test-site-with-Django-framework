from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

users=[
    {
        'username':'amir',
        'name':'Amir',
        'last_name':'amiri',
        'phone':'1234',
        'city' : 'ahvaz'
    },
    {
        'username':'sara',
        'name':'kormi',
        'last_name':'alamasi',
        'phone':'12345',
        'city' : 'karaj'
    },
    {
        'username':'milad',
        'name':'alomi',
        'last_name':'alarei',
        'phone':'12345',
        'city' : 'karaj'
    }
]

def userslist(request):
    #users_list=users
    return render(request,'accounts_app/user_list.html',context={'users_list':users})

def profile(request,username):
    for user in users:
        if user['username'] == username:
            return render(request,'accounts_app/profile.html',{'user':user})
    raise Http404('this user does not exist')

def info(request):
    return render(request,'accounts_app/info.html')

