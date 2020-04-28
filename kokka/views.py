from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Konten, Pesan, Barang, Comment, Desc
from .forms import PesanForm, CommentForm

def home(request):
    # Comment Form
    cmtform     = CommentForm()
    if request.method == 'POST':
        cmtform = CommentForm(request.POST)
        if cmtform.is_valid():
            cmtform.save()
            return HttpResponseRedirect(reverse("home"))
    # Pesan Form
    psnform     = PesanForm()
    if request.method == 'POST':
        psnform = PesanForm(request.POST)
        if psnform.is_valid():
            psnform.save()
            return HttpResponseRedirect(reverse("home"))
    
    # Desc Value 
    desc = Desc.objects.all()
    # Comment Value
    cmt = Comment.objects.order_by('-waktu')
    # Barang Value
    brg = Barang.objects.all()
    # Konten Value
    content = Konten.objects.order_by('-waktu')
    context = {
        'content': content,
        'cmt': cmt,
        'brg': brg,
        'psnform': psnform,
        'cmtform': cmtform,
        'desc': desc,
        }
    return render(request, 'home.html', context)
