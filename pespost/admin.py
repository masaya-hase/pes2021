from django.contrib import admin
from .models import Player, Ability, Skill, Formation

# Register your models here.


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 10


class AbilityInline(admin.TabularInline):
    model = Ability
    extra = 1


class FormationInline(admin.TabularInline):
    model = Formation
    extra = 1


class PlayerAdmin(admin.ModelAdmin):
    inlines = [AbilityInline, SkillInline, FormationInline]


admin.site.register(Player, PlayerAdmin)
# admin.site.register(Ability)
# admin.site.register(Skill)
