from django.http import HttpResponse
from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User
import pika
import json
from .tokens import account_activation_token


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'category', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', "first_name", "last_name", "products"]


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['url', 'username', "password", 'email', "first_name", "last_name"]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()
        # current_site = get_current_site(request)
        # mail_subject = 'Activate your blog account.'
        # message = render_to_string('acc_active_email.html', {
        #     'user': user,
        #     'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        #     'token': account_activation_token.make_token(user),
        # })
        # to_email = form.cleaned_data.get('email')
        # email = EmailMessage(
        #     mail_subject, message, to=[to_email]
        # )
        # email.send()
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()
        data = {'To': user.email, 'message': "Please verify your email address\n\n" + 'localhost:8300/activate/' + str(user.pk) + '/' + str(
            account_activation_token.make_token(user))}
        channel.queue_declare(queue='email.notify')
        channel.basic_publish(exchange='', routing_key='email.notify',
                              body=json.dumps(data))
        connection.close()
        # return HttpResponse('Please confirm your email address to complete the registration')
        return user
