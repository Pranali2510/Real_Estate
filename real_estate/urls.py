from django.urls import path
from.import views

urlpatterns = [
    path("", views.index, name="index"),
    path("customer_dashboard/", views.customer_dashboard, name="customer_dashboard"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("agent_grid/", views.agent_grid, name="agent_grid"),
    path("services/", views.services, name="services"),
    path("property_grid/", views.property_grid, name="property_grid"),
    path("add_property/", views.add_property, name="add_property"),
    path("customer_register/", views.customer_register.as_view(), name="customer_register"),
    path("agent_register/", views.agent_register.as_view(), name="agent_register"),
    path("login/", views.login_request, name="login_request"),
    path("view_properties/", views.view_properties, name="view_properties"),
    path("agent_dashboard/", views.agent_dashboard, name="agent_dashboard"),
    path("logout/", views.logout_view, name="logout_view"),
    path("update_property/<int:id>/", views.update_property, name="update_property"),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('delete1/<int:id>/', views.delete1, name='delete1'),
    path("ufeedback/", views.ufeedback, name="ufeedback"),
    path("afeedback/", views.afeedback, name="afeedback"),
    path('property_single/<int:id>/', views.property_single, name='property_single'),
    path('view_agent/', views.view_agent, name="view_agent"),
    path('a_notification/', views.a_notification, name="a_notification"),
    path("u_properties/", views.u_properties, name="u_properties"),
    path('view_user/', views.view_user, name="view_user"),

]
