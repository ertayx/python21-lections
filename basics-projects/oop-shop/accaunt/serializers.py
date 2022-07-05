from abstract.serializers import BaseSerializer

from .models import User

class UserSerialize(BaseSerializer):
    class Meta:
        fields = ["email","name","sex","is_authenticated"]
        queryset = User.objects
    