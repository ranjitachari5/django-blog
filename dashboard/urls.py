from django.urls import path

from . import views

urlpatterns=[
    path('',views.dashboard,name='dashboard'),
    path('categories/',views.categories,name='categories'),
    path('categories/add_category',views.add_category,name='add_category'),
    path('categories/delete_category/<int:pk>/',views.delete_category,name='delete_category'),
    path('categories/edit/<int:pk>/',views.edit_category,name='edit_category'),
    path('posts/',views.posts,name="posts"),
    path('posts/edit_post/<int:pk>',views.edit_post,name="edit_post"),
    path('posts/delete_post/<int:pk>',views.delete_post,name="delete_post"),
    path('posts/add_post/',views.add_post,name="add_post"),
    path('users/',views.users,name='users'),
    path('users/edit_user/<int:pk>',views.edit_user,name='edit_user'),
    path('users/delete_user/<int:pk>',views.delete_user,name='delete_user'),
    path('users/add_user/',views.add_user,name='add_user'),
]
