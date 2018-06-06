from django import forms

from .models import Product, ProductCategory, ProductReview

class ProductReviewForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ProductReviewForm, self).__init__(*args, **kwargs)

        for x in range(1,6):

            num = str(x)
        
            self.fields['review_image_' + num].required = True
            self.fields['review_image_' + num].label = 'Image' + " " + num
            self.fields['review_image_' + num].error_messages = 'You have exceed 10MB!'
            self.fields['review_image_' + num].help_text = 'Please keep file size under 10 MB.'
 
        
        self.fields['video'].required = True
        self.fields['video'].error_messages = 'You have exceed 100MB! or you have uploaded an invaild video format'
        self.fields['video'].help_text = '''Create a 90sec - 2min video showing the product in action. Wear the product and describe what you liked, 
        didn’t like, if it fit true to size, how the material felt, how you would style it etc. 
        Please talk within the video about the product. If you feel uncomfortable talking within the video, you can have someone do a voice over.
        Please do not exceed 100MB. All reviews should be your honest opinion of the product!'''
        
        self.fields['summary'].required = True
        self.fields['summary'].max_length = 700
        self.fields['summary'].error_messages = 'You have exceed over 700 characters!'
        self.fields['summary'].help_text = '''Write a 2-3 sentence product description, which can highlight/summarize points from your video. 
        Please do not exceed 700 characters (max).'''
    
    class Meta:
        model = ProductReview
        fields = (
            'summary',
            'review_image_1', 
            'review_image_2', 
            'review_image_3', 
            'review_image_4',
            'review_image_5',
            'video',  
            'purchase_product',
        )

   
