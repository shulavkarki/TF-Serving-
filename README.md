# TF-Serving-
Tensorflow Serving API to serve Text classification model

Run Tf-Serving with docker:
```
docker run -it --rm -p 8501:8501 -v "{models_dir}:/models" -v {config_dir}/config.pbtxt:/models/config.pbtxt" tensorflow/serving tensorflow_model_server --model_config_file=/models/config.pbtxt
```
Response:
![image](https://user-images.githubusercontent.com/40908371/209067919-07242f14-0865-4e21-9e90-8381f5b029da.png)
