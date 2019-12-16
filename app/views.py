from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


# def index(request):
#     return render(request, 'app/index.html')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'app/signup.html'


def join(request):
    if request.method == 'POST':
        # Instantiate the user creation form with POST data
        form = CustomUserCreationForm(request.POST)

        # Check if the form submission is valid
        if form.is_valid():
            # Save the information to the database by creating the user
            # and hashing the passoword
            form.save()

            # Get the validated form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Authenticate the user, which returns a user object
            user = authenticate(username=username, password=password)

            # Login user and send them to the home page
            login(request, user)
            return redirect('home')
    else:
        # Instantiate an empty user creation form
        form = CustomUserCreationForm()
    return render(request, 'app/signup.html', {'form': form})
