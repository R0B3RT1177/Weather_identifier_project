# Weather Identifier

 Will identify weather from dew, fogsmog, frost, glaze, hail, lightning, rain, rainbow, rime,  sandstorm, and snow.

![An image of rime, with a identification of rime with a confidence of %89.34](file:///C:/Users/Windows/Desktop/weather_test_1.jpg)

## The Algorithm

I used imagenet for my project.

Imagenet takes and input then it classifies the image and gets the confidence it has in that classification, then it overlays the classification and confidence on the image. For videos it just does this on loop until the video stops.


## Running this project

**Data**
 1. Get the dataset [here](https://www.kaggle.com/datasets/jehanbhathena/weather-dataset/discussion)
 2. Secure copy the dataset to the jetson nano into /home/nvidia/jetson-inference/python/training/classification/data
 3. Use the file_mover.py in the reposotory to sort all of the data.

**Re-training**
 1. Go into the docker container from the jetson-inference folder.
 2. Cd into python/training/classification
 3. Run: python3 train.py --model-dir=models/_dataset name_ data/_dataset name_
 4. If you pause and want to restart the training, from the docker container cd back to
 python/training/classification then you would want to run:
 python3 train.py --resume models/<dataset name>/checkpoint.pth.tar --start-epoch <epoch    number you left off at> --model-dir=models/<dataset name> data/<dataset name>

**Using**
 1. In the docker container, cd to python/training/classification again
 2. From there, convert the re-trained network to a ONNX format by running python3
onnx_export.py --model-dir=models/cat_dog
 3. Exit the docker container by pressing ctrl + d or just typing exit
 4. Set NET and DATASET variables by running NET=models/<dataset name> first, then running
DATASET=data/<dataset name>
 5. You can get an image using wget, but you should use one that's in your testing folder
for this next part
 6. run imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0
--labels=$DATASET/labels.txt $DATASET/test/<path to a classification img> <output img
name.jpg>
 7. Secure copy the output img to your desktop to check it

 

5. Make sure to include any required libraries that need to be installed for your project to run.

[View a video explanation here](video link)
