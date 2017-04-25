from django import forms

from .models import Book


class PublicationDate(forms.DateInput):
    input_type = 'date'


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'publication_date', 'author', 'editor',
                  'edition', 'year', 'publisher', 'ISBN', 'pages', 'condition',
                  'shelf_location', 'notes', 'copies')
        widgets = {
            'publication_date': PublicationDate(),
        }
