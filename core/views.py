from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import User
from .forms import SignUpForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active = False
            new_user.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return render(request, 'registration/waiting_for_activation.html')
    else:
        form = SignUpForm()
    return render(request, 'utilities/_generic_form.html', {'form': form})


def landingpage(request):
    return render(request, 'landingpage.html')


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user_detail.html', {'user': user})
