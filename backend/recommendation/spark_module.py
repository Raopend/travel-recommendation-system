from pyspark.ml import PipelineModel


class SparkModelSingleton:
    _instance = None
    _model_path = "resource/als_pipeline"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SparkModelSingleton, cls).__new__(cls)
            # 在第一次实例化时加载模型
            cls._instance.model = PipelineModel.load(cls._model_path)
        return cls._instance
