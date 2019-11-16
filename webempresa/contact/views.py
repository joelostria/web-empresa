from django.shortcuts import render,redirect
from .forms import ContactForm
from django.urls import reverse

# Create your views here.
def contact(request):
	#print("tipo de peticion: {}",format(request.method))
	if request.method == "POST":
		contactform = ContactForm(data=request.POST)
		if contactform.is_valid():
			name=request.POST.get('name','')
			email=request.POST.get('email','')
			content=request.POST.get('content','')
			return redirect(reverse('contact')+"?ok")
	contactform=ContactForm()
	return render(request,'contact/contact.html',{'form':contactform})

