from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm

# Reference: https://djangopy.org/learn/step-up-guide-to-implement-ajax-in-django/
#FBV

def contactPage(request):
	form = ContactForm()
	return render(request, "contact.html", {"contactForm": form})

def postContact(request):
	if request.method == "POST" and request.is_ajax():
		form = ContactForm(request.POST)
		form.save()
		return JsonResponse({"success":True}, status=200)
	return JsonResponse({"success":False}, status=400)