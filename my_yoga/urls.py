from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trainings/', views.trainings, name='trainings'),
    path('timetable/', views.timetable, name='timetable'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('contacts/', views.contacts, name='contacts'),
    path('khichidi/', views.khichidi, name='khichidi'),  
    path('golden_milk/', views.golden_milk, name='golden_milk'),
    path('Sambar/', views.Sambar, name='Sambar'),
    path('vegetable_soup/', views.vegetable_soup, name='vegetable_soup'),
    path('side_plank_pose/', views.side_plank_pose, name='side_plank_pose'),
    path('tree_pose/', views.tree_pose, name='tree_pose'),
    path('bridge_pose/', views.bridge_pose, name='bridge_pose'),
    path('warrior_pose1/', views.warrior_pose1, name='warrior_pose1'),
    path('bee_breath/', views.bee_breath, name='bee_breath'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('book_session/<int:timetable_entry_id>/', views.book_session, name='book_session'),
    path('user_sessions/', views.user_sessions, name='user_sessions'),
    path('delete_session/<int:session_id>/', views.delete_session, name='delete_session'),
]
