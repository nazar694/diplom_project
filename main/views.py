from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Parking, Parking_Place, Account
from .forms import CreateUserForm, EnterForm, ExitForm, ReservedForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def index(request):
    parkings = Parking.objects.all()
    parking_place = Parking_Place.objects.all()
    key = 'AIzaSyBa_kjOEyd8oH8N15GI8V80gmEAz5vSFbU'
    form = ReservedForm()
    if request.method == 'POST':
        if request.POST['form_action'] == 'reserve':
            filters = {'parking_id': int(request.POST.get('parking_id')),
                       'is_invalid': bool(request.POST.get('is_invalid')),
                       'is_electric': bool(request.POST.get('is_electric')),
                       }

            time = request.POST.get('parking_time')

            if posible_place := Parking_Place.objects.filter(parking=filters['parking_id'], status='PF',
                                                             is_place_for_electric=filters['is_electric'],
                                                             is_place_for_disable=filters['is_invalid']):

                free_place = posible_place.first()
                if time == 'is_short_time':
                    free_place = posible_place.order_by('distance_to_exit').first()
                elif time == 'is_long_time':
                    free_place = posible_place.order_by('distance_to_exit').last()

                free_place.status = 'PR'
                free_place.reserved_by = request.user
                free_place.start_time_reserved = request.POST.get('start')
                free_place.end_time_reserved = request.POST.get('end')
                free_place.save()

                return render(request, 'main/payment_check.html', {'free_place': free_place})

            else:
                context = {
                    'name': 'no_place',
                    'parking': parkings.filter(id=filters['parking_id']).first(),
                }
                return render(request, 'main/check.html', context)

        if request.POST['form_action'] == 'payment':
            if request.POST['payment'] == 'true':
                return redirect('reserved')
            else:
                id = request.POST.get('free_place')
                place = Parking_Place.objects.get(id=id)
                place.status = 'PF'
                place.reserved_by = None
                place.start_time_reserved = None
                place.end_time_reserved = None
                place.save()

                context = {
                    'name': 'no_payment',
                }
                return render(request, 'main/check.html', context)

    contex = {
        'form': form,
        'parkings': parkings,
        'parking_place': parking_place,
        'key': key,
    }

    if request.user.is_authenticated:
        contex['user_reserved'] = []
        for place in parking_place.filter(reserved_by=request.user):
            contex['user_reserved'].append(place.parking)

    return render(request, 'main/index.html', contex)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Невіний користувач або пароль!')

    context = {

    }
    return render(request, 'main/login.html', context)


def logout_page(request):
    if request.method == 'GET':
        return render(request, 'main/logout.html', {})

    if request.method == 'POST':
        logout(request)
        return redirect('index')


def registration_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            phone_number = form.cleaned_data.get('phone_number')
            user = User.objects.get(username=username)
            acc = Account.objects.create(user=user, phone_number=phone_number)
            acc.save()
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, 'main/registration.html', context)


def reserved_page(request):
    if request.user.is_authenticated:
        parking_place = Parking_Place.objects.all()
        context = {}
        if place := parking_place.filter(reserved_by=request.user):
            context['places'] = place
            context['has_place'] = True
        else:
            context['has_place'] = False

        if request.method == 'POST':
            place = parking_place.filter(reserved_by=request.user, id=int(request.POST.get('parking_id')))[0]
            place.status = 'PF'
            place.reserved_by = None
            place.start_time_reserved = None
            place.end_time_reserved = None
            place.save()
            return redirect('reserved')

        return render(request, 'main/reserved.html', context)

    else:
        return redirect('login')


def check_page(request):
    if request.user.is_authenticated:
        parking_place = Parking_Place.objects.all()
        context = {}
        if place := parking_place.filter(reserved_by=request.user):
            context['place'] = place[0]
            context['has_place'] = True
        else:
            context['has_place'] = False
        return render(request, 'main/check.html', context)
    else:
        return redirect('login')


def enter_page(request):
    form = EnterForm()
    context = {'form': form}
    if request.method == 'POST':
        finging_place = Parking_Place.objects.filter(id=request.POST.get('place'))[0]
        finging_place.status = 'PT'
        finging_place.reserved_by = None
        finging_place.start_time_reserved = None
        finging_place.end_time_reserved = None
        finging_place.save()

    return render(request, 'main/enter.html', context)


def exit_page(request):
    form = ExitForm()
    context = {'form': form}
    if request.method == 'POST':
        finging_place = Parking_Place.objects.filter(id=request.POST.get('place'))[0]
        finging_place.status = 'PF'
        finging_place.reserved_by = None
        finging_place.start_time_reserved = None
        finging_place.end_time_reserved = None
        finging_place.save()

    return render(request, 'main/exit.html', context)


def reserved_save_page(request):
    places = Parking_Place.objects.filter(status='PR')
    context = {
        'places': places,
    }
    if request.method == 'POST':
        with open('reserved_info.txt', 'w') as file:
            for place in places:
                file.writelines(f'Зарезервоване місце користувачем {place.reserved_by} | ')
                file.writelines(f'{place.parking} #{place.number} | ')
                file.writelines(f'{place.parking.street} | ')
                file.writelines(f'Зарезервовано з {place.start_time_reserved} по {place.end_time_reserved} |')
                file.writelines('\n')

    return render(request, 'main/reserved_save.html', context)
