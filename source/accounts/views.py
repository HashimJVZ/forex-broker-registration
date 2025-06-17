from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.signing import Signer, BadSignature
from django.core.mail import send_mail
from .models import User
from .serializers import RegisterSerializer, KYCUploadSerializer

signer = Signer()


@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = signer.sign(user.email)
        verification_link = f"http://localhost:8000/api/verify-email/?token={token}"
        send_mail(
            subject="Verify your Email - Forex Broker",
            message=f"Click the link to verify your account:\n{verification_link}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return Response(
            {"message": "User registered. Check email to verify."},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def verify_email(request):
    token = request.GET.get("token")
    try:
        email = signer.unsign(token)
        user = User.objects.get(email=email)
        user.email_verified = True
        user.save()
        return Response({"message": "Email verified successfully"})
    except (BadSignature, User.DoesNotExist):
        return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)

 
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_kyc(request):
    if not request.user.email_verified:
        return Response({'error': 'Email not verified'}, status=status.HTTP_403_FORBIDDEN)
    serializer = KYCUploadSerializer(instance=request.user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "KYC document uploaded"})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
