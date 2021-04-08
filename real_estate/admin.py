from django.contrib import admin
from .models import User, Customer, Agent, Property, Afeedback, Ufeedback, Comments_model
from django.contrib import admin

from .models import PropertyImage
# admin.site.register(Property)
admin.site.register(Afeedback)
admin.site.register(Ufeedback)
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Agent)
admin.site.register(Comments_model)


class PropertyImageAdmin(admin.StackedInline):
    model = PropertyImage

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageAdmin]

    class Meta:
       model = Property

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    pass



