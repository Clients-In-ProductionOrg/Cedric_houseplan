"""
Serializers for core app
"""
from rest_framework import serializers
from .models import HousePlan, BuiltHome, Contact, Quote, SiteSettings, Floor, Feature, Amenity, HousePlanImage


class SiteSettingsSerializer(serializers.ModelSerializer):
    youtube_link = serializers.SerializerMethodField()
    
    def get_youtube_link(self, obj):
        """Return YouTube link in embed format"""
        return obj.get_embed_youtube_url()
    
    class Meta:
        model = SiteSettings
        fields = ['youtube_link', 'company_phone', 'company_email', 'company_address', 'about_text', 'updated_at']
        read_only_fields = ['updated_at']


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = ['id', 'level', 'floor_area', 'bedrooms', 'bathrooms', 'lounges', 'dining_areas', 'notes', 'order']
        read_only_fields = ['id']


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name', 'description', 'order']
        read_only_fields = ['id']


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['id', 'name', 'description', 'order']
        read_only_fields = ['id']


class HousePlanImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    def get_image_url(self, obj):
        """Return full URL for image"""
        if obj.image and obj.image.name:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            # For non-request context (e.g., serialization without request)
            image_url = f"/media/{obj.image.name}"
            return image_url
        return None
    
    class Meta:
        model = HousePlanImage
        fields = ['id', 'image', 'image_url', 'title', 'order']
        read_only_fields = ['id']


class HousePlanSerializer(serializers.ModelSerializer):
    floors = FloorSerializer(many=True, read_only=True)
    features = FeatureSerializer(many=True, read_only=True)
    amenities = AmenitySerializer(many=True, read_only=True)
    plan_images = HousePlanImageSerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()
    
    def get_image_url(self, obj):
        """Return full URL for primary image"""
        if obj.image and obj.image.name:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            # For non-request context (e.g., serialization without request)
            image_url = f"/media/{obj.image.name}"
            return image_url
        return None
    
    class Meta:
        model = HousePlan
        fields = ['id', 'name', 'description', 'price', 'bedrooms', 'bathrooms', 'garage', 
                  'square_feet', 'width', 'depth', 'image', 'image_url', 'plan_images', 'video_url', 
                  'display_section', 'is_popular', 'is_best_selling', 'is_new', 'pet_friendly', 'floors', 'features', 'amenities', 
                  'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class BuiltHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuiltHome
        fields = ['id', 'name', 'description', 'location', 'image', 'completion_date', 'is_featured', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone', 'subject', 'message', 'is_read', 'created_at']
        read_only_fields = ['id', 'created_at']


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'name', 'email', 'phone', 'house_plan', 'requirements', 'is_processed', 'created_at']
        read_only_fields = ['id', 'created_at']
