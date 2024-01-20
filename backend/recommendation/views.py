from pyspark.sql.functions import col
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tours
# from .serializers import ToursSerializer
from .spark_module import SparkModelSingleton


class ToursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = '__all__'


# Create your views here.
# @api_view(["GET"])
# def recommend_tours(request, user_id):
#     spark_model_instance = SparkModelSingleton()
#     model = spark_model_instance.model
#     user_recs = model.stages[-1].recommendForAllUsers(10).filter(col('userIndex') == user_id).collect()
#     user_recs = user_recs[0]['recommendations']
#     user_recs = [i.itemIndex for i in user_recs]
#     # 从数据库中获取推荐的旅游信息
#     tours = Tours.objects.filter(location_id__in=user_recs)
#     # 使用序列化器将模型实例转换为JSON格式
#     serializer = ToursSerializer(tours, many=True)
#     return Response({"predictions": serializer.data})
class RecommendTours(APIView):
    def get(self, request, user_id):
        spark_model_instance = SparkModelSingleton()
        model = spark_model_instance.model
        user_recs = model.stages[-1].recommendForAllUsers(10).filter(col('userIndex') == user_id).collect()
        user_recs = user_recs[0]['recommendations']
        user_recs = [i.itemIndex for i in user_recs]
        # 从数据库中获取推荐的旅游信息
        tours = Tours.objects.filter(location_id__in=user_recs)
        # 使用序列化器将模型实例转换为JSON格式
        serializer = ToursSerializer(tours, many=True)
        return Response(serializer.data)
