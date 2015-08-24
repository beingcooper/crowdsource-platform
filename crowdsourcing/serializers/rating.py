from crowdsourcing import models
from crowdsourcing.serializers.user import UserProfileSerializer
from rest_framework import serializers

class WorkerRequesterRatingSerializer(serializers.ModelSerializer):
    origin = UserProfileSerializer(read_only=True)

    class Meta:
        model = models.WorkerRequesterRating
        fields = ('id', 'origin', 'target', 'module', 'weight',
                  'type', 'created_timestamp', 'last_updated')

    def create(self, **kwargs):
        print kwargs
        rating = models.WorkerRequesterRating.objects.create(origin=kwargs['origin'], **self.validated_data)
        return rating