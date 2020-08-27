from django.contrib import admin
from .models import UserOverride

# Register your models here.

class UserExtension(admin.ModelAdmin):
    change_list_template = 'django_practical/user_template.html'
    date_hierachy = 'created'

    def changelist_view(self, request, extra_context=None):
        response= super().changelist_view(
            request, extra_context=extra_context,
        )
        try:
            qs=response.context_data['cl'].queryset
            print(qs)
        except (AttributeError, KeyError):
            return response
        
      
        response.context_data['userlist']=list(
            qs.values('username', 'email','first_name', 'last_name','is_active', 'user_permissions')
            # predefined keywords: Choices are: date_joined, email, first_name, groups, id, is_active, is_staff, is_superuser, last_login, last_name, logentry, password, user_permissions, user_ptr, user_ptr_id, username
            .order_by('-email')
        )
        return response

admin.site.site_header="Django Backend Practical"

admin.site.register(UserOverride, UserExtension)

