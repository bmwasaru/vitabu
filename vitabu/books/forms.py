from django import forms

from .models import Book


class BookForm(forms.ModelForm):
	# publication_date = forms.DateInput(attrs={'class':'datepicker'})

	class Meta:
		model = Book
		fields = ('title', 'publication_date', 'author', 'editor',
                  'edition', 'year', 'publisher', 'pages', 'condition',
                  'shelf_location', 'notes', 'copies')
