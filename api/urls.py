from django.urls import path

from . import views

urlpatterns = [
        path('', views.apiOverview, name="api-overview"),
        path('VCT_list/', views.VCT_list, name="VCT_list" ),
        path('VCT_add/', views.VCT_add, name='VCT_add'),
        path('VCT_update/<str:pk>/', views.VCT_update, name="VCT_update"),
	path('VCT_delete/<str:pk>/', views.VCT_delete, name="VCT_delete"),

        path('Prob_occur_list/', views.Prob_occur_list, name="Prob_occur_list" ),
        path('Prob_occur_add/', views.Prob_occur_add, name='Prob_occur_add'),
        path('Prob_occur_update/<str:pk>/', views.Prob_occur_update, name="Prob_occur_update"),
	path('Prob_occur_delete/<str:pk>/', views.Prob_occur_delete, name="Prob_occur_delete"),

        path('Res_list/', views.Res_list, name="Res_list" ),
        path('Res_add/', views.Res_add, name='Res_add'),
        path('Res_update/<str:pk>/', views.Res_update, name="Res_update"),
	path('Res_delete/<str:pk>/', views.Res_delete, name="Res_delete"),
]