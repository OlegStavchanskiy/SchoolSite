from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from authorization.forms import LoginForm, PublishNews
from mainpage.models import Article




def doLogout(request):
    logout(request)
    return redirect('login')


def profile(request):
    if request.method=="POST":
        title = request.POST.get('title')
        text = request.POST.get('text')
        Article.objects.create(title=title, text=text, user=request.user)
    first_name = request.user.first_name
    last_name = request.user.last_name
    form = PublishNews()
    return render(request, 'lk.html', {'name': first_name, 'l_name': last_name, 'form': form})


def loginPage(request):
    if not request.user.is_authenticated:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('login')
                else:
                    form.add_error(None, 'Неверные данные!')
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile')
