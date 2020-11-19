from django.contrib import admin

from .models import User
from .models import Blog

from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    class Meta:
        model = User

    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 
                'password2', 'follows'),}),
    )
    
    fieldsets = (
        (None, {'fields': ('username', 'email')}),
        (('Follows'), {'fields': ('follows', )}),
    )

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


admin.site.register(User, UserAdmin)
admin.site.register(Blog)
