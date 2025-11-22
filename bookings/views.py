from django.shortcuts import render


# Create your views here.
def index(request):
  return render(request,'index.html')


def about(request):
  return render(request,'about.html')

def amenities(request):
  return render(request,'amenities.html')

def booking(request):
  return render(request,'booking.html')

def contact(request):
  return render(request,'contact.html')

def events(request):
  return render(request,'events.html')

def location(request):
  return render(request,'location.html')

def gallery(request):
  return render(request,'gallery.html')

def offers(request):
  return render(request,'offers.html')

def privacy(request):
  return render(request,'privacy.html')

def restaurant(request):
  return render(request,'restaurant.html')

def room_details(request):
   return render(request, 'room_details.html')

def rooms(request):
  return render(request,'rooms.html')



def terms(request):
  return render(request,'terms.html')


def notfound(request):
  return render(request,'notfound.html')