from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from django.contrib.auth import authenticate

import logging
logger = logging.getLogger('app_api')

class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginUser(APIView):
    def post(self, request:Request):
        email = request.data.get('email')
        password = request.data.get('password')

        print(email)
        user = authenticate(email=email, password=password)

        if user is not None:
            serializer = CustomUserSerializer(user)

            response = {
                "status" : True,
                "message":"login Successful",
                "user": serializer.data,
                "token": user.auth_token.key,
            }
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message":"Invalid User"}, status=status.HTTP_200_OK)

        

    def get(self, request:Request):
        content={
            "user": str(request.user),
            "auth" : str(request.auth),
        }
        return Response(data=content, status=status.HTTP_200_OK)



class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)





# class RegisterAdmin(APIView):
#     def post(self, request):
#         request.data["is_admin"] = True
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         #Ílogger.info(serializer)
#         serializer.save()

#         return JsonResponse(status=status.HTTP_201_CREATED, data={'status':'true','message':'success', 'result': serializer.data})
    

# class RegisterCustomer(APIView):
#     def post(self, request):
#         request.data["is_customer"] = True
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return JsonResponse(status=status.HTTP_201_CREATED, data={'status':'true','message':'success', 'result': serializer.data})


# class LoginAdmin(APIView):
#     def post(self, request):
#         email = request.data['email']
#         password = request.data['password']
#         user = CustomUser.objects.filter(email=email).filter(is_admin=True).first()

#         if user is None:
#             return JsonResponse(status=status.HTTP_401_UNAUTHORIZED, data={'status':'false','message':'failure', 'result': {
#             'message': 'User Not Found',
#             }})

#         if not user.check_password(password):
#             return JsonResponse(status=status.HTTP_401_UNAUTHORIZED, data={'status':'false','message':'failure', 'result': {
#             'message': 'Incorrect Password',
#             }})

#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }

#         userObject = {
#             'id': user.id,  
#             'name': user.firstname + ' ' + user.lastname,
#             'email': user.email,
#             'streetAddress': user.streetAddress,
#             'postcode': user.postcode,
#             'city': user.city,
#             'region': user.region,
#             'contact': user.contact,
#         }

#         token = jwt.encode(payload, 'secret', algorithm='HS256')
        
#         response = Response()
#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'message': 'success',
#             'jwt': token
#         }
#         #return response
#         return JsonResponse(status=status.HTTP_200_OK, data={'status':'true','message':'success', 'result': {
#             'message': 'success',
#             'jwt': token,
#             'user': userObject
#         }})




# class LoginCustomer(APIView):
#     def post(self, request):
#         email = request.data['email']
#         password = request.data['password']
#         user = CustomUser.objects.filter(email=email).filter(is_customer=True).first()

#         if user is None:
#             return JsonResponse(status=status.HTTP_401_UNAUTHORIZED, data={'status':'false','message':'failure', 'result': {
#             'message': 'User Not Found',
#             }})

#         if not user.check_password(password):
#             return JsonResponse(status=status.HTTP_401_UNAUTHORIZED, data={'status':'false','message':'failure', 'result': {
#             'message': 'Incorrect Password',
#             }})

#         payload = {

#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }

#         userObject = {
#             'id': user.id,  
#             'name': user.firstname + ' ' + user.lastname,
#             'email': user.email,
#             'streetAddress': user.streetAddress,
#             'postcode': user.postcode,
#             'city': user.city,
#             'region': user.region,
#             'contact': user.contact,
#         }

#         token = jwt.encode(payload, 'secret', algorithm='HS256')
        
#         response = Response()
#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'message': 'success',
#             'jwt': token
#         }
#         #return response
#         return JsonResponse(status=status.HTTP_200_OK, data={'status':'true','message':'success', 'result': {
#             'message': 'success',
#             'jwt': token,
#             'user': userObject
#         }})





# class AuthenticateUser(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('jwt')
        
#         if not token:
#             raise AuthenticationFailed('Unauthenticated')

#         try:
#             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated')

#         user = CustomUser.objects.filter(id=payload['id']).first()

#         serializer = UserSerializer(user)
#         return Response(serializer.data)
    


# class Logout(APIView):
#     def post(self, request):
#         response = Response()
#         response.delete_cookie('jwt')
#         response.data = {
#             'message': 'success',
#         }
#         return response


