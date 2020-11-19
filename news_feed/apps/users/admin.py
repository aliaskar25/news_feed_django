from django.contrib import admin

from .models import User
from .models import Blog

from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    class Meta:
        model = User
        fields = ('email', )

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

admin.site.register(User, UserAdmin)
admin.site.register(Blog)
