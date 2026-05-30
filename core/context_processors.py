from .models import SiteSettings
from .models import ExperienceVideo

def site_settings(request):
    try:
        settings = SiteSettings.objects.first()
    except Exception:
        settings = None
    return {'site_settings': settings}



def experience_video(request):
    try:
        video = ExperienceVideo.objects.get(pk=1, is_active=True)
    except ExperienceVideo.DoesNotExist:
        video = None
    return {'experience_video': video}