from django.shortcuts import render
from core.forms import *
from home.views import get_random_color


def kanban_add(request):
    card_form = KanbanCardForm(request.POST)
    if request.user.is_authenticated:
        current_user = request.user
        username = User.objects.get(username=current_user.username)
        user_icon_text = current_user.username[0].upper()
        user_icon_color = get_random_color()
        return render(request, 'home.html', {"username": username,
                                               "user_icon_text": user_icon_text,
                                               "user_icon_color": user_icon_color, 'card_form': card_form})

