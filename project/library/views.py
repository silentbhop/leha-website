from django.shortcuts import render, redirect
from .models import MediaFiles
from .forms import MediaFilesForm

def library(request):
    files = MediaFiles.objects.order_by('date')
    return render(request, 'library/library.html', {'files': files})

def upload(request):
    if request.method == 'POST':
        form = MediaFilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('library')
    else:
        form = MediaFilesForm()
    return render(request, 'library/upload.html', {'form': form})
