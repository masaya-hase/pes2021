from django.shortcuts import render
from .models import Player, Ability, Skill, Formation
from django.views.generic import ListView

# Create your views here.


def detailview(request, pk):
    player = Player.objects.filter(pk=pk)[0]
    ability = Ability.objects.filter(pk=pk)[0]
    skill = Skill.objects.filter(player=pk)
    formation = Formation.objects.filter(pk=pk)[0]
    return render(request, 'detail.html', {'player': player, 'ability': ability, 'skill': skill, 'formation': formation})


class legendListView(ListView):
    model = Player
    template_name = 'legend_list.html'

    def get_queryset(self):
        return Player.objects.filter(player_style='レジェンド')


class iconicListView(ListView):
    model = Player
    template_name = 'iconic_list.html'

    def get_queryset(self):
        return Player.objects.filter(player_style='アイコニックモーメント')


class fpListView(ListView):
    model = Player
    template_name = 'fp_list.html'

    def get_queryset(self):
        return Player.objects.filter(player_style='FP')
