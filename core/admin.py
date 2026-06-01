from django.contrib import admin
from django.utils.html import format_html
from django.contrib import admin
from .models import ExperienceVideo, ProductReview
from .models import HomeContent


from .models import (
    SiteSettings, HeroSlide, ProductCategory, Product,
    Service, WhyChooseUs, Testimonial, ContactSubmission
)

admin.site.site_header = 'GM SOUND Admin'
admin.site.site_title = 'GM SOUND'
admin.site.index_title = 'Dashboard'


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Brand', {'fields': ('site_name', 'tagline', 'logo', 'logo_white')}),
        ('Contact Info', {'fields': ('phone_primary', 'phone_secondary', 'email', 'address', 'whatsapp_number' , 'working_hours')}),
        ('Social Media', {'fields': ('facebook_url', 'instagram_url', 'youtube_url')}),
        ('SEO & Map', {'fields': ('meta_description', 'meta_keywords', 'map_embed_url')}),
        ('Stats', {'fields': ('years_of_experience',)}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('About Section', {
            'fields': ('about_title', 'about_description'),
        }),
        ('Stats Bar', {
            'fields': ('products_sold', 'happy_clients', 'delivery_area'),
        }),
        ('Services Section', {
            'fields': ('services_heading', 'services_subtext'),
            'description': 'Controls the headline and description above the services carousel on the homepage.',
        }),
        ('About Page Content', {
            'fields': ('mission', 'vision', 'company_description'),
            'classes': ('collapse',),
        }),
    )

    def has_add_permission(self, request):
        return not HomeContent.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'order', 'is_active', 'preview')
    list_editable = ('order', 'is_active')
    ordering = ('order',)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;border-radius:4px;">', obj.image.url)
        return '—'
    preview.short_description = 'Preview'


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_featured', 'is_active', 'order', 'thumbnail')
    list_editable = ('is_featured', 'is_active', 'order')
    list_filter = ('category', 'is_featured', 'is_active')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('order', '-created_at')

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;border-radius:4px;">', obj.image.url)
        return '—'
    thumbnail.short_description = 'Image'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('thumbnail', 'title')
    ordering = ('order',)
    fieldsets = (
        ('Service Details', {
            'fields': ('title', 'description', 'order', 'is_active'),
        }),
        ('Image', {
            'fields': ('image',),
            'description': 'Upload a high-quality image (recommended: 800×600px or wider, landscape).',
        }),
    )

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:52px;width:80px;object-fit:cover;border-radius:6px;">',
                obj.image.url
            )
        return format_html(
            '<div style="height:52px;width:80px;background:#1a1a1a;border-radius:6px;'
            'display:flex;align-items:center;justify-content:center;'
            'color:#555;font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:1px;">No img</div>'
        )
    thumbnail.short_description = ''


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'rating', 'is_active', 'created_at')
    list_editable = ('is_active',)
    list_filter = ('rating', 'is_active')


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'submitted_at', 'is_read')
    list_editable = ('is_read',)
    list_filter = ('is_read',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'submitted_at')

    def has_add_permission(self, request):
        return False

@admin.register(ExperienceVideo)
class ExperienceVideoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle', 'is_active'),
        }),
        ('Video Source — use ONE of the two below', {
            'fields': ('video_file', 'video_url'),
            'description': 'Upload an MP4 file OR paste a direct video URL. Uploaded file takes priority.',
        }),
    )

    def has_add_permission(self, request):
        return not ExperienceVideo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display  = ('star_display', 'product', 'name', 'title', 'is_approved', 'submitted_at')
    list_editable = ('is_approved',)
    list_filter   = ('is_approved', 'rating', 'product')
    search_fields = ('name', 'email', 'title', 'body')
    readonly_fields = ('name', 'email', 'product', 'rating', 'title', 'body', 'submitted_at')
    ordering = ('-submitted_at',)

    def star_display(self, obj):
        filled = '★' * obj.rating
        empty  = '☆' * (5 - obj.rating)
        return format_html(
            '<span style="color:#FF5722;font-size:14px;letter-spacing:1px;">{}</span>'
            '<span style="color:#333;font-size:14px;">{}</span>',
            filled, empty
        )
    star_display.short_description = 'Rating'

    def has_add_permission(self, request):
        return False