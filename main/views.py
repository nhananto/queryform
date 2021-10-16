from django.shortcuts import render
from .models import Post


def createpost(request):
    return render(request, 'create.html')
        

def result(request):

    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content') and request.POST.get('sex') and request.POST.get('vehicle1') and request.POST.get('vehicle2') and request.POST.get('vehicle3'):
            post = Post()
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.sex = request.POST.get('sex')
            post.vehicle1 = request.POST.get('vehicle1')
            post.vehicle2 = request.POST.get('vehicle2')
            post.vehicle3 = request.POST.get('vehicle3')
            # post.vehicle4 = request.POST.get('vehicle4')
            post.save()

    # if request.method=='POST':
    #     lis2 = request.POST.getlist('title')
    #     lis = request.POST.getlist('veh')
    #     lis5 = request.POST.getlist('sex')
    #     lis3 = request.POST.getlist('content')
    #     lis4 = lis2 + lis3 +lis5 + lis 
    #     print (lis)

    lis = []
    lis.append(request.POST['title'])
    lis.append(request.POST['content'])
    lis.append(request.POST['sex'])
    lis.append(request.POST['vehicle1'])
    lis.append(request.POST['vehicle2'])
    lis.append(request.POST['vehicle3'])

    print(lis)

    return render(request, 'result.html',{'lis':lis})










































# lis2 = []
    # lis2.append(request.GET['title'])
    # print (lis2)
# lis3 = []
    # lis3.append(request.GET['content'])
    # print (lis3)

    # lis4 = lis2 + lis + lis3
    # print (lis4)
    # lis.append(request.GET['vehicle1'])
    # lis.append(request.GET['vehicle2']) 

# def createpost(request):
#     return render(request, 'create.html')

# def result(request):
#     if request.method == 'POST':
#         if request.POST.get('title') and request.POST.get('content') and request.POST.get('sex') and request.POST.get('vehicle1') and request.POST.get('vehicle2') and request.POST.get('vehicle3'):
#             post = Post()
#             post.title = request.POST.get('title')
#             post.content = request.POST.get('content')
#             post.sex = request.POST.get('sex')
#             post.vehicle1 = request.POST.get('vehicle1')
#             post.vehicle2 = request.POST.get('vehicle2')
#             post.vehicle3 = request.POST.get('vehicle3')
#             # post.vehicle4 = request.POST.get('vehicle4')
#             post.save()

#             return render(request, 'result.html')

#     else:
#         return render(request, 'create.html')

#     if request.method == "GET":
#         return render(request, 'create.html')

#     elif request.method == "POST":
#         post = Post()
#         post.title = request.POST["title"]
#         post.content = request.POST["content"]
#         post.vehicle1 = request.POST["vehicle1"]
#         post.vehicle2 = request.POST["vehicle2"]
#         post.save()
        
#         return render(request, 'create.html')
#         #password1 = request.POST["password1"]
#         #password2 = request.POST["password2"]

#         from django.shortcuts import render
# from django.utils.datastructures import MultiValueDictKeyError


        
        