from django.shortcuts import render, redirect
from webapp.models import *

# Create your views here.
def home(request):
    context = {'pagename': 'Welcome'}
    return render(request, 'home.html', context)

def dashboard(request):
    context = {'pagename': 'Dashboard'}
    #return render(request, 'dashboard.html', context)
    return redirect('matches')

def rec(request):
    rec_list = Person.objects.filter(person_type__name='recipient')
    context = {'pagename': 'Recipients', 'rec_list': rec_list}
    return render(request, 'recipients.html', context)

def addrec(request):
    if(request.POST):
        name = request.POST['name']
        hla = request.POST['hla']
        age = request.POST['age']
        weight = request.POST['weight']
        blood = request.POST['blood']
        contact = request.POST['contact']
        organ = Organ.objects.get(id = request.POST['organ'])
        person_type = PersonType.objects.get(name='recipient')
        Person.objects.create(name = name, hla = hla, age = age, weight = weight, blood = blood, contact = contact, organ = organ, person_type = person_type)
        return redirect('rec')
    context = {'pagename': 'Recipients', 'organs': Organ.objects.all()}
    return render(request, 'newrecipient.html', context)

def addorg(request):
    if(request.POST):
        name = request.POST['name']
        hla = request.POST['hla']
        age = request.POST['age']
        weight = request.POST['weight']
        blood = request.POST['blood']
        contact = request.POST['contact']
        organ = Organ.objects.get(id = request.POST['organ'])
        person_type = PersonType.objects.get(name='donor')
        Person.objects.create(name = name, hla = hla, age = age, weight = weight, blood = blood, contact = contact, organ = organ, person_type = person_type)
        return redirect('org')
    context = {'pagename': 'Organs', 'organs': Organ.objects.all()}
    return render(request, 'newdonor.html', context)

def person(request, person_id):
    context = {'pagename': 'View Recipient', 'item': Person.objects.get(id = person_id), 'organs': Organ.objects.all()}
    return render(request, 'person.html', context)

def org(request):
    org_list = Person.objects.filter(person_type__name='donor')
    context = {'pagename': 'Organs', 'org_list': org_list}
    return render(request, 'organs.html', context)

def organ(request):
    context = {'pagename': 'Recipients', 'list': ''}
    return render(request, 'recipients.html', context)

def matches(request):
    matches = Matcher.getMatches()
    context = {'pagename': 'Matches', 'list': matches}
    return render(request, 'matches.html', context)

def notify(request, id):
    #post to chikka API
    matches = Matcher.getMatches()
    context = {'pagename': 'Matches', 'list': matches, 'sent': sent}
    return render(request, 'matches.html', context)
