import cloudinary

from django.contrib.sites.models import Site

def site_processor(request):
    return { 
        'site': Site.objects.get_current() 
    }


def consts(request):
    return dict(
        GENERAL_IMAGES = dict(
            format="jpg", 
            transformation=[
                dict(
                    crop="fit", 
                    quality="auto",
                    width=0.2
                )
            ]
        ),
    )