from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        # Basic sanitation: limit length and remove suspicious characters if desired
        if len(title) > 200:
            raise forms.ValidationError("Title is too long.")
        return title

class SearchForm(forms.Form):
    q = forms.CharField(required=False, max_length=100)

    def clean_q(self):
        q = self.cleaned_data.get('q', '').strip()
        # Additional validation/sanitization if needed
        return q
