import cloudinary

from django.contrib.sites.models import Site

def site_processor(request):
    return { 
        'site': Site.objects.get_current() 
    }


def consts(request):
    return dict(
        ICON_EFFECTS = dict(
            format="png",
            type="facebook",
            transformation=[
                dict(height=95, width=95, crop="thumb", gravity="face", effect="sepia", radius=20),
                dict(angle=10),
            ]
        ),
        COMPRESS_IMAGES = dict(
            format="jpg", 
            type="fetch",
            crop="fit", 
            height=1000, 
            width=1000,
            quality="auto"
        ),
        THUMBNAIL = dict(
            format="jpg", 
            crop="fill", 
            height=284, 
            width=284,
        ),
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