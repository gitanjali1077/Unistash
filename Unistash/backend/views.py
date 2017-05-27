from Unistash.settings import SENDER,PASS
import smtplib
from django.shortcuts import render
from django.conf import settings
from django import forms
from django.views.generic import View
from django.views.generic.edit import FormView
from django.views import generic
from .forms import UserForm ,ContactForm
# Create your views here.
from django.http import HttpResponse


def index(request,string=None):
  msgs=''
  a=string 
  template = a+'.html'


  if a=='index': 
   if request.method == 'GET':
      user_form = UserForm(request.GET)
      
      return render(request, template, {
           'user_form': user_form  , 'msgs' : msgs       })

      
   if request.method == 'POST':
      user_form = UserForm(request.POST)
       
      if  user_form.is_valid()  :
           
           user1= user_form.save(commit=False)
           #prof= profile_form.save()
           username = user_form.cleaned_data['username']
           college = user_form.cleaned_data['college']
           email = user_form.cleaned_data['email']
           user1.save()
           msg="Hello , \n Welcome here"
           smtp= smtplib.SMTP('smtp.gmail.com')
           smtp.ehlo()
           smtp.starttls()
           smtp.ehlo()
           smtp.login(SENDER,PASS)
           smtp.sendmail(SENDER,email,msg)
           smtp.quit()
           #profile=profile_form.save(commit=False)
           #profile.user_id=user1.id+1
           #profile.college=profile_form.cleaned_data['college']
           #profile.save()
         
          
           #profile_form.save()
            #return redirect('settings:profile')
           msgs='Thanks for joining us..'
           user_form = UserForm(request.GET)
      
      return render(request, 'index.html', {
           'user_form': user_form  , 'msgs' : msgs       })

   else:
           msgs='not sent'
           return render(request,template , {  'user_form': user_form  ,
                                               'msgs' : msgs })
	

  elif a=='contactUs':

   if request.method == 'GET':
      user_form = ContactForm(request.GET)
      
      return render(request, template, {
           'user_form': user_form  , 'msgs' : msgs       })

      
   if request.method == 'POST':
      user_form = ContactForm(request.POST)
       
      if  user_form.is_valid()  :
           
           user1= user_form.save(commit=False)
           #prof= profile_form.save()
           email = user_form.cleaned_data['email']
           subject = user_form.cleaned_data['subject']
           message = user_form.cleaned_data['message']
           
           msg=email +' '+ subject+' ' + message
           smtp= smtplib.SMTP('smtp.gmail.com')
           smtp.ehlo()
           smtp.starttls()
           smtp.ehlo()
           smtp.login(SENDER,PASS)
           smtp.sendmail(SENDER,SENDER,msg)
           smtp.quit()
           #profile=profile_form.save(commit=False)
           #profile.user_id=user1.id+1
           #profile.college=profile_form.cleaned_data['college']
           #profile.save()
         
          
           #profile_form.save()
            #return redirect('settings:profile')
           msgs='Thanks for contacting us..'
           user_form = ContactForm(request.GET)
      
      return render(request, 'ContactUs.html', {
           'user_form': user_form  , 'msgs' : msgs       })

   else:
           msgs='not sent'
           return render(request,template , {  'user_form': user_form  ,
                                               'msgs' : msgs })
	
# this is the last one for all the pages
  else:

     return render(request,template )
	
	

       
def file1(request,string=None):
        #try:
        # return FileResponse(open('C:\Users\HCL\Unistash\unistash\Unistash\media\hass.pdf', 'rb'), content_type='application/pdf')
        #except FileNotFoundError:
         #raise Http404()
         q=string
         with open('D:/Unistash/media/'+q+'.pdf', 'rb') as pdf:
            response = HttpResponse(pdf.read(),content_type='application/pdf')
            response['Content-Disposition'] = 'filename=hass.pdf'
            return response


