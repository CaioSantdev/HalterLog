from django.contrib import admin
from workout.models.treinoModel import Treino
from workout.models.exercicioModel import Exercicio
from workout.models.serieModel import Serie


class SerieInline(admin.TabularInline):
    model = Serie
    extra = 0
    fields = ('numero', 'tipo', 'repeticoes', 'peso', 'descanso', 'observacao')
    readonly_fields = ('criado_em', 'atualizado_em')


class ExercicioInline(admin.TabularInline):
    model = Exercicio
    extra = 0
    fields = ('nome', 'grupo_muscular')
    show_change_link = True


@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'usuario', 'criado_em', 'atualizado_em')
    list_filter = ('usuario',)
    search_fields = ('nome', 'usuario__username')
    inlines = [ExercicioInline]
    ordering = ['-criado_em']


@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'treino', 'grupo_muscular')
    list_filter = ('grupo_muscular',)
    search_fields = ('nome', 'treino__nome')
    inlines = [SerieInline]


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('id', 'exercicio', 'numero', 'tipo', 'repeticoes', 'peso', 'descanso')
    list_filter = ('tipo',)
    search_fields = ('exercicio__nome',)
    ordering = ['exercicio', 'numero']
