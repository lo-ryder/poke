from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Poke, PokeManager
from ..logregapp .models import User

# Create your views here.
def pokes(request):
    context = {
        'activeUser': User.objects.get(id=request.session['id']),
        'distinctPokeList': User.objects.order_by('poked').exclude(id=request.session['id']),
        'whoPokedMe': Poke.objects.filter(personpoked_id=request.session['id']),
        'userList': User.objects.all().exclude(id=request.session['id']),
    }
    print '\n\nactiveUser->', context['activeUser']
    print 'distinctPokeList->', context['distinctPokeList']
    print 'whoPokedMe->', context['whoPokedMe']
    print 'userList->', context['userList'], '\n\n'
    print 'request.session id->', request.session['id']
    return render(request, 'pokeapp/pokes.html', context)

def pokebutton(request):
    print 'in pokebutton!!!!'
    Poke.objects.PokeButton(request.POST)
    print 'added a poke to +++++>', request.POST['personpoked_id']
    return redirect('pokeapp:pokes')
