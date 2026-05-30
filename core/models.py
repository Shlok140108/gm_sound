from django.db import models



class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default='GM SOUND')
    tagline = models.CharField(max_length=200, blank=True)
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    logo_white = models.ImageField(upload_to='site/', blank=True, null=True)
    phone_primary = models.CharField(max_length=20, blank=True)
    phone_secondary = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    whatsapp_number = models.CharField(max_length=20, blank=True)
    years_of_experience = models.PositiveIntegerField(default=15)
    map_embed_url = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    working_hours = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        # Singleton: only one instance allowed
        self.pk = 1
        super().save(*args, **kwargs)

class HomeContent(models.Model):
    # Home About Section

    about_title = models.CharField(max_length=200)

    about_description = models.TextField()

    # Stats

    products_sold = models.CharField(
        max_length=20,
        default="500+"
    )

    happy_clients = models.CharField(
        max_length=20,
        default="200+"
    )

    delivery_area = models.CharField(
        max_length=50,
        default="Pan India"
    )

    # About Page

    mission = models.TextField()

    vision = models.TextField()

    company_description = models.TextField()

    class Meta:
        verbose_name = "Website Content"

    def __str__(self):
        return "Website Content"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

class HeroSlide(models.Model):
    subtitle = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='hero/')
    button_text = models.CharField(max_length=50, blank=True)
    button_url = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/')
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True, help_text='Heroicons name e.g. speaker-wave')
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class WhyChooseUs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Why Choose Us Items'

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.PositiveIntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.company}'


class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f'{self.name} — {self.submitted_at.strftime("%d %b %Y %H:%M")}'

class ExperienceVideo(models.Model):
    title       = models.CharField(max_length=200, default='Experience The Sound',
                                   help_text='Overlay title shown on the video screen')
    subtitle    = models.CharField(max_length=300, blank=True,
                                   help_text='Short tagline below the title')
    video_file  = models.FileField(upload_to='experience/', blank=True, null=True,
                                   help_text='Upload an MP4 video (recommended: 1080p, max 50MB)')
    video_url   = models.URLField(blank=True,
                                  help_text='OR paste a YouTube / direct MP4 URL instead of uploading')
    is_active   = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Experience Video'
        verbose_name_plural = 'Experience Video'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.pk = 1   # singleton — only one record
        super().save(*args, **kwargs)

class ProductReview(models.Model):
    RATING_CHOICES = [(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)]

    product     = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    name        = models.CharField(max_length=100, verbose_name='Your Name')
    email       = models.EmailField(verbose_name='Email Address',
                                    help_text='Not shown publicly')
    rating      = models.PositiveIntegerField(choices=RATING_CHOICES, default=5)
    title       = models.CharField(max_length=150, blank=True, verbose_name='Review Title')
    body        = models.TextField(verbose_name='Your Review')
    is_approved = models.BooleanField(default=False,
                                      help_text='Only approved reviews are shown publicly')
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Product Review'
        verbose_name_plural = 'Product Reviews'

    def __str__(self):
        return f'{self.rating}★ — {self.product.name} by {self.name}'
