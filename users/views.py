from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime
from rest_framework.decorators import api_view

import logging
logger = logging.getLogger('app_api')


class RegisterAdmin(APIView):
    def post(self, request):
        request.data["is_admin"] = True
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #Ílogger.info(serializer)
        serializer.save()

        return JsonResponse(status=status.HTTP_201_CREATED, data={'status':'true','message':'success', 'result': serializer.data})
    

class RegisterCustomer(APIView):
    def post(self, request):
        request.data["is_customer"] = True
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(status=status.HTTP_201_CREATED, data={'status':'true','message':'success', 'result': serializer.data})


class LoginAdmin(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).filter(is_admin=True).first()

        if user is None:
            return JsonResponse(status=status.HTTP_401_UNAUTHORIZED, data={'status':'false','message':'failure', 'result': {
            'message': 'User Not Found',
            }})

        if not user.check_password(password):
            return JsonResponse(status=status.HTTP_401_UNAUTHORIZED, data={'status':'false','message':'failure', 'result': {
            'message': 'Incorrect Password',
            }})

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        userObject = {
            'id': user.id,  
            'name': user.firstname + ' ' + user.lastname,
            'email': user.email,
            'streetAddress': user.streetAddress,
            'postcode': user.postcode,
            'city': user.city,
            'region': user.region,
            'contact': user.contact,
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'message': 'success',
            'jwt': token
        }
        #return response
        return JsonResponse(status=status.HTTP_200_OK, data={'status':'true','message':'success', 'result': {
            'message': 'success',
            'jwt': token,
            'user': userObject
        }})




class LoginCustomer(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).filter(is_customer=True).first()

        if user is None:
            return JsonResponse(status=status.HTTP_401_UNAUTHORIZED, data={'status':'false','message':'failure', 'result': {
            'message': 'User Not Found',
            }})

        if not user.check_password(password):
            return JsonResponse(status=status.HTTP_401_UNAUTHORIZED, data={'status':'false','message':'failure', 'result': {
            'message': 'Incorrect Password',
            }})

        payload = {

            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        userObject = {
            'id': user.id,  
            'name': user.firstname + ' ' + user.lastname,
            'email': user.email,
            'streetAddress': user.streetAddress,
            'postcode': user.postcode,
            'city': user.city,
            'region': user.region,
            'contact': user.contact,
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'message': 'success',
            'jwt': token
        }
        #return response
        return JsonResponse(status=status.HTTP_200_OK, data={'status':'true','message':'success', 'result': {
            'message': 'success',
            'jwt': token,
            'user': userObject
        }})





class AuthenticateUser(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()

        serializer = UserSerializer(user)
        return Response(serializer.data)
    


class Logout(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success',
        }
        return response



@api_view(['GET', 'POST'])
def admin_list(request):
    if request.method == 'GET':
        customers = User.objects.filter(is_admin=True)
        serializer = UserSerializer(customers, many=True)
        return JsonResponse(status=200, data={'status': 'true', 'message': 'success', 'result': serializer.data})


@api_view(['GET', 'PUT', 'DELETE'])
def admin_details(request, id):
    try:
        customer = User.objects.filter(is_admin=True).get(pk=id)

    except User.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND,  data={'message':'Request not found'})

    if request.method == 'GET':
        serializer = UserSerializer(customer)
        return JsonResponse(status=200, data={'status':'true','message':'success', 'result': serializer.data})

    elif request.method == 'PUT':
        serializer = UserSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(status=200, data={'status':'true','message':'success', 'result': serializer.data})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, data={'status':'false','message':'Bad Request'})
    
    elif request.method == 'DELETE':
        customer.delete()
        return JsonResponse(status=status.HTTP_200_OK, data={'status': 'true', 'message': 'success'})  
    





@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method == 'GET':
        customers = User.objects.filter(is_customer=True)
        serializer = UserSerializer(customers, many=True)
        return JsonResponse(status=200, data={'status': 'true', 'message': 'success', 'result': serializer.data})



@api_view(['GET', 'PUT', 'DELETE'])
def customer_details(request, id):

    try:
        customer = User.objects.filter(is_customer=True).get(pk=id)

    except User.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND,  data={'message':'Request not found'})

    if request.method == 'GET':
        serializer = UserSerializer(customer)
        return JsonResponse(status=200, data={'status':'true','message':'success', 'result': serializer.data})

    elif request.method == 'PUT':
        serializer = UserSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(status=200, data={'status':'true','message':'success', 'result': serializer.data})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, data={'status':'false','message':'Bad Request'})
    
    elif request.method == 'DELETE':
        customer.delete()
        return JsonResponse(status=status.HTTP_200_OK, data={'status': 'true', 'message': 'success'})  
    





