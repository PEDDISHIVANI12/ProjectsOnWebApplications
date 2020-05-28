from django.shortcuts import render
#from django.http import HttpResponse
from .models import Laundry
# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
#from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

#def signup(request):
 #   if request.method == 'POST':
  #      form = UserCreationForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       username = form.cleaned_data.get('username')
      #      raw_password = form.cleaned_data.get('password1')
       #     user = authenticate(username=username, password=raw_password)
       #    return render(request, 'index.html')
 #   else:
  #      form = UserCreationForm()
   # return render(request, 'signup.html', {'form': form})
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
def index(request):
    return render(request,"index.html")
#def logout(request):
  # return render(request,"logout.html")
def again(request):
    return render(request,"again.html")
def track(request):
    return render(request,"track.html")
def AddService(request):
    return render(request, "softwash.html")
def Address(request):
    return render(request, "address.html")
#def login(request):
 #   return render(request, "login.html")
def cart(request):
    return render(request, "cart.html")
def AddService_submit(request):
    pickup_date = request.POST["pickup_date"]
    delivery_date = request.POST["delivery_date"]
    pickup_flat = request.POST["pickup_flat"]
    pickup_locality = request.POST["pickup_locality"]
    pickup_pincode = request.POST["pickup_pincode"]
    delivery_flat = request.POST["delivery_flat"]
    delivery_locality = request.POST["delivery_locality"]
    delivery_pincode = request.POST["delivery_pincode"]
    email = request.POST["email"]
    pay = request.POST["pay"]
    
    laundry = Laundry(pickup_date=pickup_date,delivery_date=delivery_date,email=email,pay=pay,pickup_flat=pickup_flat,pickup_locality=pickup_locality,pickup_pincode=pickup_pincode,delivery_flat=delivery_flat,delivery_locality=delivery_locality,delivery_pincode=delivery_pincode)
    laundry.save()
    all_orders = list(Laundry.objects.all())[-1]
    return render(request,"submit.html",{'service' : all_orders })

