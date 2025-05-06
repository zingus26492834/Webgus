from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member
from django.urls import reverse
from datetime import date
from django.contrib.auth.decorators import login_required

@login_required
def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

@login_required
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  a = request.POST['first']
  b = request.POST['last']
  c = request.POST['phoneno']
  d = request.POST['emailad']
  e = date.today()
  member = Member(firstname=a, lastname=b, phone=c, email=d, joined_date=e)
  member.save()
  return HttpResponseRedirect(reverse('zinguses'))

@login_required  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

@login_required  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

@login_required
def search(request):
  query = request.GET.get('q')
  if query:
    results = Member.objects.filter(firstname__icontains=query)
  else:
    results = Member.objects.all()
  template = loader.get_template('search.html')
  context = {'results': results}

  return HttpResponse(template.render(context, request))

@login_required
def cool(request):
  template = loader.get_template('cool.html')
  return HttpResponse(template.render())

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))