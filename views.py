from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

name=""#declaring variables for storing user
pswrd=""
@csrf_exempt
def sample(req):
    return HttpResponse("app is working")



# @csrf_exempt
# def handle_use_login_form_data(req):
#     # print(req.method)
#     # print(req.body)
#     if req.method=="POST":
#         global name,pswrd
#         #post->form data submitted by client through request(it will be in dict)
#         name=req.POST.get("username")
#         pswrd=req.POST.get("password")
#         email=req.POST.get("email")
#         mobile=req.POST.get("mobile")
#         dob=req.POST.get("dob")
#         print(name,pswrd,email,mobile,dob)
#         return JsonResponse({"msg":"data submitted succesfully"})
#     else:
#         return JsonResponse({"msg":"invalid method"})



@csrf_exempt
def handle_user_login_form_data(req):
    print(req.body)
    user_data=json.loads(req.body)
    if user_data["username"] and user_data["password"]:
        return user_login(user_data["username"],user_data["password"])
    # print(user_data["username"])
    # print(user_data["password"])
        # return HttpResponse("data submitted")



def user_login(u,p):
    if u=="sumithra" and p=="sumi@123":
        return HttpResponse("login successful")
    else:
        return HttpResponse("invalid")
