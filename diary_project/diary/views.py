from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DiaryEntry
from .forms import DiaryEntryForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def diary_home(request):
    entries = DiaryEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'diary/home.html', {'entries': entries})

@login_required
def add_entry(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('diary_home')
    else:
        form = DiaryEntryForm()
    return render(request, 'diary/add_entry.html', {'form': form})

@login_required
def delete_entry(request, entry_id):
    entry = DiaryEntry.objects.get(id=entry_id, user=request.user)
    if entry:
        entry.delete()
    return redirect('diary_home')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after signup
    else:
        form = UserCreationForm()
    return render(request, 'diary/signup.html', {'form': form})