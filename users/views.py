
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import UserRegistrationSerializer,UserLoginSerializer,SuperUSerRegistrationSerializer
from rest_framework.generics import RetrieveAPIView
from .models import User


class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 'True',
            'status code' : status_code,
            'message': 'User registered  successfully',
            }
        
        return Response(response, status=status_code)
class RegisterAdmin(CreateAPIView):

    serializer_class = SuperUSerRegistrationSerializer
        # Todo: Change permisssion to must be admin and is authenticated later

    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 'True',
            'status code' : status_code,
            'message': 'User registered  successfully',
            'super_data':serializer.data
            }
        
        return Response(response, status=status_code)


# class RegisterAdmin(ModelViewSet):
#     # Todo: Change permisssion to must be admin and is authenticated later
#     permission_classes = [AllowAny]
#     serializer_class = SuperUSerRegistrationSerializer
#     queryset = User.objects.all()
        




class AuthUserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user  = request.user
        serialized = UserRegistrationSerializer(user).data
        return Response(serialized,status=200)

class UserWithProfile(ModelViewSet):
    queryset  = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserRegistrationSerializer

    def update(self, request,pk):
        try:
            user = User.objects.get(pk = pk)
            userProfile  = user.profile
            serialized = UserRegistrationSerializer(request.POST)
            if(serialized.is_valid):
                user.email = request.POST.get('email')
                userProfile.first_name= request.POST.get('first_name')
                userProfile.last_name = request.POST.get('last_name')
                user.save()
                userProfile.save()
                return Response({'user':serialized.data,'message':"User updated succesfully"},status=200)
            else:
                raise ValidationError('Invalid data',code=400)
        except ObjectDoesNotExist:
            raise ValidationError('There is no user with given the id provided',code=400)



class UserLoginView(APIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)