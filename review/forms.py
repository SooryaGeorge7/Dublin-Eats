from django import forms
from review.models import Review
from django.forms import HiddenInput


class RatingForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'taste',
            'ambience',
            'customer_service',
            'value_for_money',
            'location',
            'comment_text',
            ]
        widgets = {
            'taste': HiddenInput(),
            'ambience': HiddenInput(),
            'location': HiddenInput(),
            'customer_service': HiddenInput(),
            'value_for_money': HiddenInput(),
            'comment_text': forms.Textarea(
                attrs={'placeholder': 'Type in a review here...',
                       'class': 'responsive-textarea',
                       }
            ),
        }
        labels = {
            'taste': 'Taste',
            'ambience': 'Ambience',
            'location': 'Location',
            'customer_service': 'Customer Service',
            'value_for_money': 'Value for Money',
            'comment_text': 'Review Comment',
        }
        help_texts = {
            'comment_text': 'Maximum 500 characters',
        }
