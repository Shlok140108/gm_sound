from django import forms
from .models import ContactSubmission, ProductReview



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ('name', 'email', 'phone', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Full Name', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email Address', 'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-input'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5, 'class': 'form-input'}),
        }


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model  = ProductReview
        fields = ('name', 'email', 'rating', 'title', 'body')
        widgets = {
            'name':   forms.TextInput(attrs={'placeholder': 'Your Name',       'class': 'form-input'}),
            'email':  forms.EmailInput(attrs={'placeholder': 'Email Address',   'class': 'form-input'}),
            'title':  forms.TextInput(attrs={'placeholder': 'Review title (optional)', 'class': 'form-input'}),
            'body':   forms.Textarea(attrs={'placeholder': 'Share your experience with this product…',
                                            'rows': 4, 'class': 'form-input'}),
            # Rating widget is replaced by JS stars in the template
            'rating': forms.HiddenInput(),
        }