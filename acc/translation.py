from modeltranslation.translator import translator, TranslationOptions
from .models import Post

class PostTranslationOptions(TranslationOptions):
    fields = ('text', 'discription',)

translator.register(Post, PostTranslationOptions)