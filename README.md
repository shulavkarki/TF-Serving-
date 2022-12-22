# TF-Serving-
Tensorflow Serving API to serve Text classification model

Run Tf-Serving with docker:
```
docker run -it --rm -p 8501:8501 -v "{models_dir}:/models" -v {config_dir}/config.pbtxt:/models/config.pbtxt" tensorflow/serving tensorflow_model_server --model_config_file=/models/config.pbtxt
```
