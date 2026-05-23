from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from Users.models import SendMailModel, UserRegister_Model, FeedbackModel, Phishing_Model


def login_page(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('username')
            pswd = request.POST.get('password')
            if usid == 'admin' and pswd == 'admin':
                return redirect('admin_page')
    return render(request,'admins/login_page.html')

def admin_page(request):
    obj=UserRegister_Model.objects.all()
    return render(request,'admins/admin_page.html',{'objects':obj})

def analysis_page(request):
    obj=SendMailModel.objects.all()

    return render(request,'admins/analysis_page.html',{'obj':obj})

def analysisdelete(request,pk):

    obj = get_object_or_404(SendMailModel, pk=pk)
    obj.delete()
    return redirect('analysis_page')
def categoryanalysis_chart(request,chart_type):
    chart = SendMailModel.objects.values('category').annotate(dcount=Count('category'))
    return render(request,'admins/chart.html',{'objects':chart,'chart_type':chart_type})

def viewfeedback(request):
    obj = FeedbackModel.objects.all()
    return render(request,'admins/viewfeedback.html',{'object':obj})


def attactdetails(request):
    obj=Phishing_Model.objects.all()
    return render(request,'admins/attactdetails.html',{'obj':obj})
