from django.shortcuts import render
from minifier.forms import UrlForm
from minifier.models import Url

import random
import string

def generer(nb_caracteres):
    caracteres = string.ascii_letters + string.digits
    aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]
    
    return ''.join(aleatoire)

def convert(request):
    check = False
    newcode = ""
    form = UrlForm(request.POST or None)

    if form.is_valid(): 

        url = Url() 
        url.url = form.cleaned_data["url"]
        url.pseudo = form.cleaned_data["pseudo"]
        url.code = generer(4)
        url.save()

        check = True
        newcode = url.code
        url.save()
    

    return render(request, 'minifier/convert.html', locals())
