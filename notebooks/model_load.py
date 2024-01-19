from pyspark.ml import PipelineModel
from pyspark.sql.functions import col

if __name__ == '__main__':
    # Load model
    model = PipelineModel.load("models/als_pipeline/")
    # Predict
    user_id = 2
    user_recs = model.stages[-1].recommendForAllUsers(10).filter(col('userIndex') == user_id).collect()
    user_recs = user_recs[0]['recommendations']
    user_recs = [i.itemIndex for i in user_recs]
    # 将 csv 文件读为 Python 字典
    file_path = "dataset/tours_truncated.csv"
    import pandas as pd

    # 读取 CSV 文件并转换为字典
    df = pd.read_csv(file_path)
    data_dict = dict(zip(df["location_id"], df["display_name"]))
    print([data_dict[i] for i in user_recs])
