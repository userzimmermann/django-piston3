from django.contrib import admin
from .models import Nonce, Token, Consumer

admin.site.register(Nonce)
admin.site.register(Token)
admin.site.register(Consumer)
