from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'pagename': 'Welcome'}
    return render(request, 'home.html', context)

def dashboard(request):
    context = {'pagename': 'Dashboard'}
    return render(request, 'dashboard.html', context)
