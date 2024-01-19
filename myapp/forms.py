from django import forms

class FeedbackForm(forms.Form):
    feedback_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
