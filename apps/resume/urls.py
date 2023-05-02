from rest_framework.routers import DefaultRouter

from apps.resume.views import ResumeViewSet


router = DefaultRouter()
router.register("resume", ResumeViewSet, basename="resume")

urlpatterns = router.urls
