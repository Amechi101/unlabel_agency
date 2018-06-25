import cloudinary
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
        THUMBNAIL = dict(
            format="jpg", 
            crop="fill", 
            height=284, 
            width=284,
        ),
        GENERAL_IMAGES = dict(
            format="jpg", 
            transformation=[
                dict(crop="fill", width=1000)
            ]
        ),
    )

