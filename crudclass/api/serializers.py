from rest_framework import serializers
from .models import Student

#validators
def start_with_s(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should be start with s')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_s])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):  # Indented properly inside the class
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    #Field level validation
    #def validate_roll(self, value):
        #if value >= 200:
            #raise serializers.ValidationError('seat full')
            #return value
            
            
#object level validation
#def validate_object(self, data):
    #nm = data.get('name')
    #ct = data.get('city')
    #if nm.lower() == 'suraj' and ct.lower() != 'ktm':
        #raise serializers.ValidationError('city must ne ktm')
    #return data    
    
    


    
            
    