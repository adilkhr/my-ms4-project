from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse

# Create your views here.
def contact(request):
    """ A view to return the contact page """
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return render(request, 'contact/thankyou.html')
    return render(request, 'contact/contact.html')