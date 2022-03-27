from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import All_equipment
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, UserRegistrationForm, EquipmentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
#Home
@login_required
def home(request):
    return render(request, 'home.html', {'section': 'home'})



#Registration
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'itequipments/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            
            # Save the User object
            new_user.save()
            return render(request,'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'registration/register.html', {'user_form': user_form, 'error': 'Incorect data'})



############################################-APPLICATION-###########################################
@login_required
def all_equipment(request):
    equipment = All_equipment.objects.filter(in_service=True)

    paginator = Paginator(equipment, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    eq_search = request.GET.get('searchMovie')
    return render(request,'itequipments/all_equipment.html', {'equipment':equipment,'eqlist':page_obj})


def all_equipment_search(request):
    if request.method == "POST":
        search_equipment = request.POST['search_equipment']
        searchList = All_equipment.objects.filter(asset_no__contains = search_equipment)
        return render(request,'itequipments/all_equipment_search.html', {'search_equipment':search_equipment, 'searchList':searchList})

@login_required
def not_used_equipment(request):
    equipment = All_equipment.objects.filter(in_service=False)
    return render(request,'itequipments/not_used_equipment.html', {'equipment':equipment})

@login_required
def add_equipment(request):
    if request.method == 'GET':
        equipment_no = All_equipment.objects.all().count()
        return render(request,'itequipments/add_equipment.html', {'form': EquipmentForm, 'count': equipment_no})
    else:
        try:
            form = EquipmentForm(request.POST,request.FILES)
            new_equipment= form.save(commit=False)
            new_equipment.user = request.user
            new_equipment.save()
            return redirect('all_equipment')
    
        except ValueError:
                return render(request, 'itequipments/add_equipment.html', {'form': EquipmentForm(), 'error': 'Bad data, Please try again'})

@login_required
def view_equipment(request,log_pk):
    equipment_detail= get_object_or_404(All_equipment, pk=log_pk)
    return render(request,'itequipments/view_equipment.html', {'equipment':equipment_detail})


@login_required
def edit_equipment(request, log_pk):
    equipment_edit= get_object_or_404(All_equipment, pk=log_pk)

    if request.method =='GET':
        form = EquipmentForm(instance=equipment_edit)
        return render(request,'itequipments/edit_equipment.html', {'equipment':equipment_edit, 'form':form})

    else:
        if request.method =='POST':
            try:
                form = EquipmentForm(request.POST, instance=equipment_edit)
                form.save()
                return redirect('all_equipment')
            
            except ValueError:
                return render(request,'itequipments/edit_equipment.html', 
                {'equipment':equipment_edit, 'form':form, 'error': 'Incorrect data, Please try again.'})

@login_required
def delete_equipment(request, log_pk ):
    equipment_delete = get_object_or_404(All_equipment, pk=log_pk)
    if request.method == 'POST':
        equipment_delete.delete()
        return redirect('all_equipment')
    return render(request,'itequipments/delete_equipment.html', {'equipment':equipment_delete})