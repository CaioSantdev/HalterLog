from rest_framework.routers import DefaultRouter
from workout.views.treinoView import TreinoViewSet
from workout.views.serieView import SerieViewSet
from workout.views.exercicioView import ExercicioViewSet

router = DefaultRouter()

router.register('treinos',TreinoViewSet)
router.register('exericios',ExercicioViewSet)
router.register('series',SerieViewSet)

urlpatterns = router.urls