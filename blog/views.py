from django.shortcuts import render

posts = [
    {
        'author':'CoreyMS',
        'title':'Blog Post 1',
        'content':'First Post content',
        'date_posted':'February 23, 2020'
    },
    {
        'author':'Jane doe',
        'title':'Blog Post 2',
        'content':'Second Post content',
        'date_posted':'February 24, 2020'
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)  

# Create your views here.

def about(request):
    return render(request,'blog/about.html',{'title':'About'})  