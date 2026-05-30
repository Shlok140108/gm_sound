from django.urls import path
from . import views
from .views import SubmitReviewView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('testimonials/', views.TestimonialsView.as_view(), name='testimonials'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('products/<int:product_id>/review/',SubmitReviewView.as_view(), name='submit_review'),
]