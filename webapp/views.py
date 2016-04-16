from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    context = {'pagename': 'Welcome'}
    return render(request, 'home.html', context)

def dashboard(request):
    context = {'pagename': 'Dashboard'}
    #return render(request, 'dashboard.html', context)
    return redirect('matches')

def rec(request):
    context = {'pagename': 'Recipients', 'list': ''}
    return render(request, 'recipients.html', context)

def addrec(request):
    context = {'pagename': 'Recipients', 'list': ''}
    return render(request, 'recipients.html', context)

def recipient(request):
    context = {'pagename': 'Recipients', 'list': ''}
    return render(request, 'recipients.html', context)

def org(request):
    context = {'pagename': 'Organs', 'list': ''}
    return render(request, 'organs.html', context)

def addorg(request):
    context = {'pagename': 'Organs', 'list': ''}
    return render(request, 'organs.html', context)

def organ(request):
    context = {'pagename': 'Recipients', 'list': ''}
    return render(request, 'recipients.html', context)

def matches(request):
    context = {'pagename': 'Matches', 'list': ''}
    return render(request, 'matches.html', context)
