from django.core.management.base import BaseCommand
from core.models import (
    SiteSettings, Service, WhyChooseUs, ProductCategory, Testimonial
)


class Command(BaseCommand):
    help = 'Seed initial demo data'

    def handle(self, *args, **options):
        # Site Settings
        if not SiteSettings.objects.exists():
            SiteSettings.objects.create(
                site_name='GM SOUND',
                tagline='Leading sound system manufacturing company delivering high-performance professional audio solutions.',
                phone_primary='7057500369',
                phone_secondary='9822640732',
                email='info@sbproaudio.com',
                address='Wadgaon Sheri, Subhadra Trinity, Office No. 5, Near Jain Sthanak, Pune - 411014',
                years_of_experience=15,
            )
            self.stdout.write(self.style.SUCCESS('✓ Site settings created'))

        # Services
        services_data = [
            ('Professional Sound Systems', 'High-quality sound systems for concerts, events, weddings, clubs, and auditoriums with crystal-clear audio output.'),
            ('DJ Audio Setup', 'Complete DJ sound setup solutions with powerful speakers and amplifiers for professional DJ performances.'),
            ('Speaker Manufacturing', 'Premium speaker cabinets designed for deep bass and crystal-clear harmonics with durable build quality.'),
            ('Amplifier Solutions', 'Professional amplifiers engineered for maximum power output and reliability in any installation.'),
            ('Flight Case Manufacturing', 'Heavy-duty flight cases designed to protect your audio equipment during transport and touring.'),
            ('Installation & Setup', 'Expert installation and setup services for auditoriums, clubs, events, and commercial venues.'),
        ]
        for i, (title, desc) in enumerate(services_data):
            Service.objects.get_or_create(title=title, defaults={'description': desc, 'order': i})
        self.stdout.write(self.style.SUCCESS(f'✓ {len(services_data)} services created'))

        # Why Choose Us
        why_data = [
            ('Manufacturing Quality Products', 'Premium-grade manufacturing with strict quality control standards for professional audio equipment.'),
            ('Powerful Bass & Clear Sound', 'Engineered for deep bass response and crystal-clear audio output for professional applications.'),
            ('Professional Audio Expertise', 'Years of industry experience and technical audio expertise in sound system design.'),
            ('Durable & Rugged Build', 'Built to last with rugged construction for professional touring and installation use.'),
            ('Customized Solutions', 'Tailored audio solutions for your specific venue, event, or installation requirements.'),
            ('Affordable Pricing', 'Competitive prices without compromising on quality or performance standards.'),
        ]
        for i, (title, desc) in enumerate(why_data):
            WhyChooseUs.objects.get_or_create(title=title, defaults={'description': desc, 'order': i})
        self.stdout.write(self.style.SUCCESS(f'✓ {len(why_data)} why-choose-us items created'))

        # Product Categories
        cats = ['DJ Speakers', 'Subwoofers', 'Amplifiers', 'Flight Cases', 'Line Arrays', 'Accessories']
        for i, name in enumerate(cats):
            from django.utils.text import slugify
            ProductCategory.objects.get_or_create(slug=slugify(name), defaults={'name': name, 'order': i})
        self.stdout.write(self.style.SUCCESS(f'✓ {len(cats)} product categories created'))

        # Testimonials
        testimonials_data = [
            ('Rahul Sharma', 'Event Manager', 'StarEvents Pune', 'Excellent quality speakers! Used GM SOUND systems for multiple large-scale events and they never disappoint. Crystal clear sound even at full volume.', 5),
            ('DJ Vikram', 'Professional DJ', 'VikramBeats', 'Best DJ speakers in this price range. The bass response is incredible. Highly recommended for professional setups.', 5),
            ('Priya Joshi', 'Auditorium Manager', 'City Cultural Center', 'We installed GM SOUND systems in our auditorium and the difference is night and day. Very professional team with excellent after-sales support.', 5),
        ]
        for name, desig, company, msg, rating in testimonials_data:
            Testimonial.objects.get_or_create(name=name, defaults={
                'designation': desig, 'company': company, 'message': msg, 'rating': rating
            })
        self.stdout.write(self.style.SUCCESS(f'✓ {len(testimonials_data)} testimonials created'))

        self.stdout.write(self.style.SUCCESS('\n🎉 Demo data seeded successfully!'))
        self.stdout.write('  → Now create a superuser: python manage.py createsuperuser')
        self.stdout.write('  → Visit /admin/ to manage content')
