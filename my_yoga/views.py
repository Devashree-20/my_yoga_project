from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import TimetableEntry, SessionBooking
from .forms import BookingForm
from django.contrib import messages
from django.urls import reverse


def index(request):
    # Your index view logic goes here
    return render(request, 'my_yoga/index.html')

def trainings(request):
    # Your trainings view logic goes here
    return render(request, 'my_yoga/trainings.html')

def timetable(request):
    # Retrieve all timetable entries from the database
    timetable_entries = TimetableEntry.objects.all()
    
    # Pass the timetable entries to the template context
    return render(request, 'my_yoga/timetable.html', {'timetable_entries': timetable_entries})

def nutrition(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/nutrition.html')
    
def khichidi(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/khichidi.html')

def golden_milk(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/golden_milk.html')

def Sambar(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/Sambar.html')
    
def vegetable_soup(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/vegetable_soup.html') 

def side_plank_pose(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/side_plank_pose.html') 

def tree_pose(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/tree_pose.html') 
    
def warrior_pose1(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/warrior_pose1.html') 
    
def bridge_pose(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/bridge_pose.html') 

def bee_breath(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/bee_breath.html')
    
def contacts(request):
    # Your contacts view logic goes here
    return render(request, 'my_yoga/contacts.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')  # Replace 'index' with your desired URL after login
    else:
        form = AuthenticationForm()
    return render(request, 'my_yoga/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Replace 'index' with your desired URL after signup
    else:
        form = UserCreationForm()
    return render(request, 'my_yoga/signup.html', {'form': form})
    
    
    
    

@login_required
def book_session(request, timetable_entry_id):
    timetable_entry = TimetableEntry.objects.get(pk=timetable_entry_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.timetable_entry = timetable_entry  # Set the timetable entry
            booking.user = request.user  # Set the logged-in user
            booking.yoga_type = timetable_entry.yoga_type  # Set the yoga name
            booking.save()
            messages.success(request, 'Booking successful!')  # Provide feedback to the user
            return redirect('index')
        else:
            messages.error(request, 'Please correct the errors below.')  # Inform user about invalid form
    else:
        form = BookingForm()

    return render(request, 'my_yoga/book_session.html', {'form': form, 'timetable_entry': timetable_entry})



@login_required
def user_sessions(request):
    # Retrieve all sessions booked by the current user
    user_sessions = SessionBooking.objects.filter(user=request.user)
    return render(request, 'my_yoga/user_sessions.html', {'user_sessions': user_sessions})

@login_required
def delete_session(request, session_id):
    # Get the session object to be deleted
    session = get_object_or_404(SessionBooking, pk=session_id)
    
    # Check if the logged-in user owns the session
    if session.user == request.user:
        # Delete the session
        session.delete()
        messages.success(request, 'Session deleted successfully.')
    else:
        messages.error(request, 'You do not have permission to delete this session.')
    
    return redirect('user_sessions')