from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
# Create your views here.

#function based view

def myview(request):
	return HttpResponse("<h1>FUNCTION BASED VIEW</H1>")

#Class based view

class MyView(View):
  name ="<h1>my name is yagnesh and i create class based View</h1>"
  def get(self,request):
   return HttpResponse(self.name)
 	#return HttpResponse("<h1>CLASS BASED VIEW</H1>")
class MyViewchild(MyView):
  myname ="<h1>child class</h1>"	
  def get(self,request):
    return HttpResponse(self.name +"**"+ self.myname)

