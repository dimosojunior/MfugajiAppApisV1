
from django.urls import path
from . import views

# # MWANZO IN ORDER TO USE MODEL VIEW SET
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


# router.register('Customers', views.CustomersViewSet)






urlpatterns = router.urls