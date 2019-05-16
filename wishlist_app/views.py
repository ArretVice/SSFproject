from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import WishlistItem
from .forms import AddItemForm


# Create your views here.
@login_required(login_url='users:login')
def edit_item(request, user_id, item_id):
    if request.user.id == user_id:
        instance = get_object_or_404(WishlistItem, user_id=user_id, id=item_id)
        form = AddItemForm(request.POST or None, instance=instance)
        if form.is_valid():
            edited_item = form.save()
            messages.success(request, f'{edited_item} successfully edited')
            return redirect('wishlist:edit_wishlist', user_id=user_id)
        return render(request, 'wishlist_app/edit_item.html', {'form': form})
    else:
        return HttpResponseForbidden()

@login_required(login_url='users:login')
def add_item(request, user_id):
    if request.user.id == user_id:
        if request.method == 'POST':
            form = AddItemForm(request.POST)
            if form.is_valid():
                new_item = form.save(commit=False)
                new_item.user = request.user
                new_item.save()
                messages.success(request, f'Added {new_item} to wishlist')
                return redirect('wishlist:edit_wishlist', user_id=user_id)
            else:
                messages.warning(request, 'Warning: some fields were not filled correctly')
                form = AddItemForm(request.POST)
        else:
            form = AddItemForm()
        return render(request, 'wishlist_app/add_item.html', {'form': form})
    else:
        return HttpResponseForbidden()

@login_required(login_url='users:login')
def edit_wishlist(request, user_id):
    if request.user.id == user_id:
        items = WishlistItem.objects.filter(user_id=user_id)
        return render(request, 'wishlist_app/edit_wishlist.html', {'items': items})
    else:
        return HttpResponseForbidden()

def all_wishlists_view(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(pk=request.user.id)
        other_users = User.objects.exclude(pk=request.user.id)
        users = [current_user] + ([x for x in other_users])
    else:
        users = User.objects.all()
    return render(request, 'wishlist_app/all_wishlists.html', {'users': users})

@login_required(login_url='users:login')
def delete_item(request, user_id, item_id):
    if request.user.id == user_id:
        item = get_object_or_404(WishlistItem, user_id=user_id, id=item_id)
        return render(request, 'wishlist_app/delete_item.html', {'item': item})
    else:
        return HttpResponseForbidden()

@login_required(login_url='users:login')
def confirm_delete_item(request, user_id, item_id):
    if request.user.id == user_id:
        item = get_object_or_404(WishlistItem, user_id=user_id, id=item_id)
        item_name = item.item_name
        item.delete()
        messages.success(request, f'{item_name} deleted')
        return redirect('wishlist:edit_wishlist', user_id=user_id)
    else:
        return HttpResponseForbidden()
