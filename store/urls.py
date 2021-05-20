from django.urls import path

from . import views

urlpatterns = [
	#path('', views.index, name='index'),
	    # ex: /polls/5/
	#path('/details/', views.details, name='detailsview'),
    path('fullinfo/<int:o_id>/', views.GetDetails, name='details'),
    # ex: /polls/5/results/
    path('info/<int:o_id>/', views.GetDetails2, name='details2'),

    path('maintainance/<int:o_id>/', views.Maintainance_rec, name='maintainance_record'),

    path('maintainance_item/<int:o_id>/<int:i_id>', views.get_maintainance_info_item, name='maintainance_record_item'),
    
    # ex: /polls/5/vote/
    path('add_o/<int:o_id>/<str:o_namef>/<str:o_namel>/', views.Add_owner, name='Add_Info_owner'),
    
    path('add_ins/<int:o_id>/<str:installed_item>/<str:item_id>/', views.Add_owner_installation, name='Add_Info_owner'),

    #path('add_mains/<int:o_id>/<str:installed_item>/<str:item_id>/<str:remarks>/', views.Add_owner, name='Add_Info_owner'),
    

	]