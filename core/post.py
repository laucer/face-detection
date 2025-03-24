from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from core.face_detection import detect_faces_and_generate_image


class ImageUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        image = request.FILES.get("image")
        if not image:
            return Response({"error": "No image provided"}, status=400)

        temp_path = f"/tmp/{image.name}"
        with open(temp_path, "wb+") as f:
            for chunk in image.chunks():
                f.write(chunk)

        generated_name = detect_faces_and_generate_image(temp_path)
        url = request.build_absolute_uri(f"/media/{generated_name}")

        # notify websocket clients
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("face_group", {
            "type": "send_url",
            "url": url
        })

        return Response({"url": url})
