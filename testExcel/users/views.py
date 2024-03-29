from posix import environ
from django.shortcuts import render
from api_test.models import Profile,User
from api_test.serializers import ProfileSerializer
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

import requests, os

from .serializers import CreateUserSerializer




@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''
    Registers user to the server. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    # Put the data from the request into the serializer 
    serializer = CreateUserSerializer(data=request.data) 
    # Validate the data
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save() 
        # Then we get a token for the created user.
        # This could be done differentley 
        r = requests.post('http://{}:{}/o/token/'.format(os.getenv("DJANGO_HOST"), int(os.getenv("DJANGO_PORT"))), 
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': os.getenv("CLIENT_ID"),
                'client_secret': os.getenv("CLIENT_SECRET"),
            },
        )
        
        return Response(r.json())
    return Response(serializer.errors)



@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    '''
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    r = requests.post('http://{}:{}/o/token/'.format(os.environ["DJANGO_HOST"], int(os.environ["DJANGO_PORT"])), 
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': os.environ["CLIENT_ID"],
                'client_secret': os.environ["CLIENT_SECRET"],
            },
        )
    user = User.objects.get(username=request.data['username'])
    nom = user.last_name
    prenom = user.first_name
    email = user.email
    qs = Profile.objects.filter(user=user)
    serializer = ProfileSerializer(qs, many=True)

    details = {
        'nom':nom,
        'prenom':prenom,
        'email':email,
        'usename':request.data['username']
    }
        
    return Response({'token':r.json(),'profile':serializer.data,'details':details})



@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    '''
    r = requests.post('http://{}:{}/o/token/'.format(os.environ["DJANGO_HOST"], int(os.environ["DJANGO_PORT"])),
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': os.environ["CLIENT_ID"],
            'client_secret': os.environ["CLIENT_SECRET"],
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token": "<token>"}
    '''
    r = requests.post(
        'http://{}:{}/o/revoke_token/'.format(os.environ["DJANGO_HOST"], int(os.environ["DJANGO_PORT"])), 
        data={
            'token': request.data['token'],
                'client_id': os.environ["CLIENT_ID"],
                'client_secret': os.environ["CLIENT_SECRET"],
        },
    )
    # If it goes well return sucess message (would be empty otherwise) 
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)