from rest_framework.routers import DefaultRouter
from workout.views.treinoView import TreinoViewSet
from workout.views.serieView import SerieViewSet
from workout.views.exercicioView import ExercicioViewSet
from workout.views.sessaoTreinoView import SessaoTreinoViewSet
from workout.views.serieExecutadaView import SerieExecutadaViewSet

router = DefaultRouter()

router.register('treinos',TreinoViewSet)
router.register('exericios',ExercicioViewSet)
router.register('series',SerieViewSet)
router.register('sessoes',SessaoTreinoViewSet)
router.register('series-executadas',SerieExecutadaViewSet)


urlpatterns = router.urls