from rest_framework import serializers
from catdog_ai.models import Pet
from catdog_ai.ai import cat_dog_predict

class PetSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        pet = Pet.objects.create(**validated_data)
        pet_type = cat_dog_predict(pet.photo.path)
        pet.classification = pet_type
        pet.save()
        return pet

    class Meta:
        model = Pet
        fields = ('id', 'photo', 'classification', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
        extra_kwargs = {
            'photo': {'write_only': True},
            'classification': {'required': False},
        }
