from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import View
from .models import HomeContent
from .models import (
    HeroSlide, Product, ProductCategory,
    Service, WhyChooseUs, Testimonial, SiteSettings
)
from .forms import ContactForm,ProductReviewForm
from django.http import JsonResponse
from django.db.models import Avg, Count, Q
from core import models



class HomeView(View):
    def get(self, request):
        context = {
            'slides': HeroSlide.objects.filter(is_active=True),
            'featured_products': Product.objects.filter(is_featured=True, is_active=True)[:6],
            'services': Service.objects.filter(is_active=True)[:3],
            'why_items': WhyChooseUs.objects.all()[:6],
            'testimonials': Testimonial.objects.filter(is_active=True)[:6],
            'content': HomeContent.objects.first(),
        }
        return render(request, 'core/home.html', context)


class AboutView(View):
    def get(self, request):
        context = {
            'why_items': WhyChooseUs.objects.all(),
            'content': HomeContent.objects.first()
        }
        return render(request, 'core/about.html', context)


class ServicesView(View):
    def get(self, request):
        context = {
            'services': Service.objects.filter(is_active=True),
        }
        return render(request, 'core/services.html', context)


class ProductsView(View):
    def get(self, request):
        category_slug = request.GET.get('category')
        categories = ProductCategory.objects.all()
        products = Product.objects.filter(is_active=True)
        active_category = None
        if category_slug:
            active_category = get_object_or_404(ProductCategory, slug=category_slug)
            products = products.filter(category=active_category)
        context = {
            'products': products,
            'categories': categories,
            'active_category': active_category,
        }
        return render(request, 'core/products.html', context)


class TestimonialsView(View):
    def get(self, request):
        context = {
            'testimonials': Testimonial.objects.filter(is_active=True),
        }
        return render(request, 'core/testimonials.html', context)


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'core/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent. We will get back to you shortly.')
            return redirect('contact')
        return render(request, 'core/contact.html', {'form': form})

class ProductsView(View):
    def get(self, request):
        category_slug  = request.GET.get('category')
        categories     = ProductCategory.objects.all()
        products       = Product.objects.filter(is_active=True)
        active_category = None
        if category_slug:
            active_category = get_object_or_404(ProductCategory, slug=category_slug)
            products = products.filter(category=active_category)

        # Annotate each product with avg rating + review count
        from django.db.models import Avg, Count
        products = products.annotate(
            avg_rating=Avg(
                'reviews__rating',
                filter=Q(reviews__is_approved=True)
            ),
            review_count=Count(
                'reviews',
                filter=Q(reviews__is_approved=True)
            ),
        )

        context = {
            'products':        products,
            'categories':      categories,
            'active_category': active_category,
            'review_form':     ProductReviewForm(),
        }
        return render(request, 'core/products.html', context)


class SubmitReviewView(View):
    """Handles AJAX or normal POST for product reviews."""
    def post(self, request, product_id):
        import json
        product = get_object_or_404(Product, pk=product_id, is_active=True)
        form    = ProductReviewForm(request.POST)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.save()
                return JsonResponse({'ok': True,
                    'message': 'Thank you! Your review is pending approval.'})
            return JsonResponse({'ok': False, 'errors': form.errors}, status=400)

        # Normal form fallback
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            messages.success(request, 'Thank you! Your review is pending approval.')
        return redirect('products')
