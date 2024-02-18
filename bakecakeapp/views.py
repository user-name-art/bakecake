from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegistrationForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model


def index(request):
    context = {
        'vue_data': {
            'costs': {
                'Levels': [0, 400, 750, 1100],
                'Forms': [0, 600, 400, 1000],
                'Toppings': [0, 200, 180, 200, 300, 350, 200],
                'Berries': [0, 400, 300, 450, 500],
                'Decors': [0, 300, 400, 350, 300, 200, 280],
                'Words': 500
            },
            'DATA': {
                'Levels': ['не выбрано', '1', '2', '3'],
                'Forms': ['не выбрано', 'Круг', 'Квадрат', 'Прямоугольник'],
                'Toppings': ['не выбрано', 'Белый соус', 'Карамельный',
                             'Кленовый', 'Черничный', 'Молочный шоколад',
                             'Клубничный'],
                'Berries': ['нет', 'Ежевика', 'Малина', 'Голубика',
                            'Клубника'],
                'Decors': ['нет', 'Фисташки', 'Безе', 'Фундук', 'Пекан',
                           'Маршмеллоу', 'Марципан']
            },
        }
    }
    return render(request, 'index.html', context)


@login_required
def profile(request):
    levels = request.GET.get('LEVELS', '1')
    shape = request.GET.get('FORM', 'круг')
    topping = request.GET.get('TOPPING', '1')
    berries = request.GET.get('BERRIES', '0')
    decor = request.GET.get('DECOR', '0')
    text = request.GET.get('WORDS', '')
    comment = request.GET.get('COMMENTS', '')
    name = request.GET.get('NAME', '')
    phone = request.GET.get('PHONE', '')
    email = request.GET.get('EMAIL', '')
    address = request.GET.get('ADDRESS', '')
    date = request.GET.get('DATE', '')
    time = request.GET.get('TIME', '')

    context = {
        'vue_data': {
            'Name': 'Ирина',
            'Phone': '8 909 000-00-00',
            'Email': 'nyam@gmail.com',
        },
        'cakes': [
            {
                'pk_order': '2239400223',
                'name': 'Свадебный торт “VIP”',
                'levels': '1',
                'shape': 'круг',
                'topping': 'белый соус',
                'berries': 'нет',
                'decor': 'нет',
                'text': 'Без надписи',
                'price_order': '1000',
                'status_order': 'В доставке',
                'time_order': '?',
            },
            {
                'pk_order': '45575879537',
                'name': 'Торт “Черепаха”',
                'levels': '2',
                'shape': 'квадрат',
                'topping': 'белый соус',
                'berries': 'нет',
                'decor': 'безе',
                'text': 'С днём рождения',
                'price_order': '2550',
                'status_order': 'Выполнен',
                'time_order': '?',
            },
        ]
    }
    return render(request, 'lk-order.html', context)


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            mobile_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(username=mobile_number, password=password)
            if user is not None:
                login(request, user)
            else:
                messages.error(request, 'Invalid login or password. Please, try again.')
                return redirect('user_login')

        return render(request, 'index.html', {'phone_number': mobile_number})


class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                User = get_user_model()
                user = User.objects.create(phone_number=phone_number)
                user.set_password(password1)
                user.save()
                return redirect('user_login')
            else:
                messages.error(request, 'Password mismatch. Please try again.')
                return redirect('user_signup')


def user_logout(request):
    logout(request)
    return render(request, 'index.html')
