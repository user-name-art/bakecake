from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegistrationForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Level, Berry, Shape, Topping, Decor, CustomCake, Order


def index(request):
    levels = Level.objects.all().order_by('cake_level')
    shapes = Shape.objects.all().order_by('price')
    berries = Berry.objects.all().order_by('price')
    toppings = Topping.objects.all().order_by('price')
    decors = Decor.objects.all().order_by('price')

    all_levels = [level.cake_level for level in levels]
    level_prices = [int(level.price) for level in levels]

    all_shapes = [shape.shape_name for shape in shapes]
    shape_prices = [int(shape.price) for shape in shapes]

    all_berries = [berry.berry_name for berry in berries]
    berry_prices = [int(berry.price) for berry in berries]

    all_toppings = [topping.topping_name for topping in toppings]
    topping_prices = [int(topping.price) for topping in toppings]

    all_decors = [decor.decor_name for decor in decors]
    decor_prices = [int(decor.price) for decor in decors]

    context = {
        'vue_data': {
            'costs': {
                'Levels': level_prices,
                'Forms': shape_prices,
                'Toppings': topping_prices,
                'Berries': berry_prices,
                'Decors': decor_prices,
                'Words': 500
            },
            'DATA': {
                'Levels': all_levels,
                'Forms': all_shapes,
                'Toppings': all_toppings,
                'Berries': all_berries,
                'Decors': all_decors
            },
        }
    }
    return render(request, 'index.html', context)


@login_required
def profile(request):
    user = request.user

    levels = Level.objects.all().order_by('cake_level')
    shapes = Shape.objects.all().order_by('price')
    berries = Berry.objects.all().order_by('price')
    toppings = Topping.objects.all().order_by('price')
    decors = Decor.objects.all().order_by('price')

    all_levels = [level.cake_level for level in levels]
    level_prices = [int(level.price) for level in levels]

    all_shapes = [shape.shape_name for shape in shapes]
    shape_prices = [int(shape.price) for shape in shapes]

    all_berries = [berry.berry_name for berry in berries]
    berry_prices = [int(berry.price) for berry in berries]

    all_toppings = [topping.topping_name for topping in toppings]
    topping_prices = [int(topping.price) for topping in toppings]

    all_decors = [decor.decor_name for decor in decors]
    decor_prices = [int(decor.price) for decor in decors]

    if request.GET.get('LEVELS'):
        selected_level = int(request.GET.get('LEVELS', ''))
        selected_shape = int(request.GET.get('FORM', ''))
        selected_topping = int(request.GET.get('TOPPING', ''))
        selected_berries = int(request.GET.get('BERRIES', '0'))
        selected_decor = int(request.GET.get('DECOR', '0'))
        selected_text = request.GET.get('WORDS', '0')
        selected_comment = request.GET.get('COMMENTS', '')
        selected_address = request.GET.get('ADDRESS', '')
        selected_date = request.GET.get('DATE', '')
        selected_time = request.GET.get('TIME', '')

        cake = CustomCake.objects.create(
            level_count=levels.filter(cake_level=all_levels[selected_level])[0],
            shape=shapes.filter(shape_name=all_shapes[selected_shape])[0],
            topping=toppings.filter(topping_name=all_toppings[selected_topping])[0],
            berry=berries.filter(berry_name=all_berries[selected_berries])[0],
            decor=decors.filter(decor_name=all_decors[selected_decor])[0],
            text=str(selected_text),

        )
        print(cake)

        order_price = level_prices[selected_level] + shape_prices[selected_shape] + berry_prices[selected_berries] + topping_prices[selected_topping] + decor_prices[selected_decor]
        if selected_text:
            order_price += 500

        order = Order.objects.create(
            user=user,
            cost=order_price,
            comment=str(selected_comment),
            custom_cake=cake,
            address=str(selected_address),
        )

    orders = user.orders.all().order_by('delivery_date')
    user_data = {
            'Name': user.name,
            'Phone': str(user.phone_number),
            'Email': user.email,
        }

    order_list = []
    for order in orders:
        order_list.append(
            {
                'pk_order': order.id,
                'price_order': order.cost,
                'levels': order.custom_cake.level_count,
                'shape': order.custom_cake.shape,
                'topping': order.custom_cake.topping,
                'berries': order.custom_cake.berry,
                'decor': order.custom_cake.decor,
                'text': order.custom_cake.text,
                'status_order': order.status,
                'time_order': order.delivery_date,
            }
        )

    context = {
        'vue_data': user_data,
        'cakes': order_list,
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
                user, created = User.objects.get_or_create(phone_number=phone_number)
                if created:
                    user.set_password(password1)
                    user.save()
                    return redirect('user_login')
                else:
                    messages.error(request, 'User with this phone number is already registered.')
                    return redirect('user_signup')
            else:
                messages.error(request, 'Password mismatch. Please try again.')
                return redirect('user_signup')


def user_logout(request):
    logout(request)
    return render(request, 'index.html')
