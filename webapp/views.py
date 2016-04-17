from django.shortcuts import render, redirect
from webapp.models import *
import urllib2, urllib

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
        antibody = request.POST['anti']
        print "ANTI " + request.POST['anti']
        print "PREV " + str(request.POST['prev'])
        if request.POST['prev'] == '1':
            print "TRUE" 
            prev = True
        else:
            prev = False
        Person.objects.create(name = name, hla = hla, age = age, weight = weight, blood = blood, contact = contact, organ = organ, person_type = person_type, reactiveAntibodies = antibody, prevKidneyDonor = prev)
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
    matcher = Matcher()
    matches = matcher.getMatches()
    context = {'pagename': 'Matches', 'list': matches}
    return render(request, 'matches.html', context)

def notify(request, person_id):
    recipient = Person.objects.get(id = person_id)
    sent = False
    #post to chikka API
    post_data = [('message_type', 'send'), ('mobile_number', recipient.contact), ('shortcode', '29290469148'), ('message_id', person_id), ('message', 'Hello! You already have a donor.'), ('client_id', 'f3be0f5b7d2abc0ce6fc0dccf7ecc049272af5679fbf5a547429cbaddb0391ff'), ('secret_key', '757f94e11c41b07a8eb846c20ad1db7fcb98b07a57b85ebe7092c3e4c457f87b')]
    try:
        result = urllib2.urlopen('https://post.chikka.com/smsapi/request', urllib.urlencode(post_data))
        result.read()
        sent = True
    except urllib2.HTTPError as e:
        print e
        sent = False
    matcher = Matcher()
    matches = matcher.getMatches()
    context = {'pagename': 'Matches', 'list': matches, 'sent': sent}
    return render(request, 'matches.html', context)
