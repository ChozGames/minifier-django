from django.shortcuts import render, redirect, get_object_or_404
from minifier.forms import UrlForm, CodeForm
from minifier.models import Url
from .services import utils

def convert(request):
    check = False
    newcode = ""
    form = UrlForm(request.POST or None)
    formredirection = CodeForm(request.POST or None)

    if form.is_valid(): 

        url = Url() 
        url.url = form.cleaned_data["url"]
        url.pseudo = form.cleaned_data["pseudo"]
        url.code = utils.generer(4)
        url.save()

        check = True
        newcode = url.code
        url.save()

        form = UrlForm()
        formredirection = CodeForm()

    

    urls = Url.objects.all()
    return render(request, 'minifier/convert.html', locals())

def redirectcode(request):
    formredirection = CodeForm(request.POST or None)

    if formredirection.is_valid():
        code = formredirection.cleaned_data["code"]

        try:
            url = Url.objects.get(code=code)
            url.access += 1
            url.save()
            return redirect(url.url)

        except Url.DoesNotExist:
            return redirect(convert)

    return redirect(convert)

def urlredirect(request, code):
    try:
        url = Url.objects.get(code=code)
        url.access += 1
        url.save()
        return redirect(url.url)

    except Url.DoesNotExist:
        return redirect(convert)