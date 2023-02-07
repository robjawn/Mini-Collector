from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('minis/', views.mini_index, name='index'),
    path('minis/<int:mini_id>/', views.mini_detail, name="detail"),
    path('minis/create/', views.MiniCreate.as_view(), name='minis_create'),
    path('minis/<int:pk>/update/', views.MiniUpdate.as_view(), name='minis_update'),
    path('minis/<int:pk>/delete/', views.MiniDelete.as_view(), name='minis_delete'),
    path('minis/<int:mini_id>/add_stock/', views.add_stock, name='add_stock'),
    path('minis/<int:mini_id>/assoc_paint/<int:paint_id>/', views.assoc_paint, name='assoc_paint'),
    path('paints/', views.PaintIndex.as_view(), name='paints_index'),
    path('paints/create', views.PaintCreate.as_view(), name='paints_create'),
    path('paints/<int:pk>/update', views.PaintUpdate.as_view(), name='paints_update'),
    path('paints/<int:pk>/delete', views.PaintDelete.as_view(), name='paints_delete'),
    path('paints/<int:pk>/', views.PaintDetail.as_view(), name='paints_detail'),
    path('accounts/signup/', views.signup, name='signup')
]