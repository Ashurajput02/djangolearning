from django.http import HttpResponse
# abhi mein iss line se response de sakta hoon
from django.shortcuts import render
# idhar iska arth hai ki mein django shortcuts se render ko import karliya hai
# jiska prime use aata hain html pages / templates jinmhe bolte hain unko render karne ke liye


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return HttpResponse("Contact Ashu Rajput for further updates")
