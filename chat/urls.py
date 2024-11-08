from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatapp_home, name='chatapp-home'),
    path('search/chats/', views.search_chats, name='search-chats'),
    path('my-chats/', views.my_chats, name='my-chats'),
    path('my-chats/leave-group/<group_username>', views.leave_group, name='leave-group'),
    path('private/single-chat/<user_id>', views.single_chat, name='single-chat'),
    path('private/single-chat/delete/<user_id>', views.delete_single_chat, name='delete-single-chat'),
    path('public/group-chat/<group_username>', views.public_group_chat, name='public-chat'),
    path('private/group-chat/<group_username>', views.private_group_chat, name='private-chat'),
    path('group-chat/edit/<group_username>', views.edit_group, name='edit-group'),
    path('group-chat/create/', views.create_group, name='create-group'),
    path('group-chat/create/public/', views.create_public_group, name='create-public-group'),
    path('group-chat/create/private/', views.create_private_group, name='create-private-group'),
    path('group-chat/delete/<group_username>', views.delete_group, name='delete-group'),
    path('group-chat/detail-area/<group_username>/', views.group_detail_area, name='group-detail-area'),
]

