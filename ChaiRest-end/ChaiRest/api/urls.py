from django.urls import path, include

from . import views
from api.views import *
# from views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )



urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category-list' ),
    path('category/<int:id>/', CategoryDetailView.as_view(), name='category-details'),
    path('category/<int:id>/furniture/', CategoryFurnitureList.as_view(), name='furniture-list'),
    path('furniture/', FurnitureListView.as_view(), name='furniture-details'),
    path('furniture/<int:id>', FurnitureDetailView.as_view(), name='furniture-details'),
    # path('auth/login/', TokenObtainPairView.as_view(), name='jwt-obtain-token'),
    # path('auth/refresh/', TokenRefreshView.as_view(), name='jwt-refresh-token'),
    # path('auth/verify/', TokenVerifyView.as_view(), name='jwt-verify-token'),
]
