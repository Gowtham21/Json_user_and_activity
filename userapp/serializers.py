from rest_framework import serializers
from .models import user, activity


class activitySerializer(serializers.ModelSerializer):
    class Meta:
        model = activity
        fields = ('start_time', 'end_time')
        #depth = 5

class userSerializer(serializers.ModelSerializer):
    user_activities = activitySerializer(many=True)
    class Meta:
        model = user
        fields = ('id','real_name','tz','user_activities')
        #depth = 5

'''
Now we are using Serializers allow complex data such as querysets and model instances to be converted
to native Python datatypes that can then be easily rendered into JSON, The ModelSerializer class provides
a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields.
'''
