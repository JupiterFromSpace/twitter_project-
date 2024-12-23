from rest_framework.response import Response
from post.serializer import UserProfileSerializer , CreatUserProfileSerializer
from post.models import UserProfile
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView,CreateAPIView




class ListUserProfileView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    #permission_classes = (IsAuthenticated,)


class CreateUserProfileView(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = CreatUserProfileSerializer


class UserProfileView(APIView):
    permission_classes = (IsAuthenticated,)


    def get(self,request):
        all_user_profile_obj = UserProfile.objects.all()

        serializer = UserProfileSerializer(all_user_profile_obj,many=True)

        return Response(serializer.data)
    