import os

file_path_base = "/home/nvidia/jetson-inference/python/training/classification/data/weather_identifier/"
#We create this variable to prepend to all of our other filepaths because this will
#be the start of every filepath we use.

counter = 0
#The idea here is to go through the dataset and split 1/10 into validation, 
#another 1/10 into testing, and 8/10 into training datasets so train.py works.

os.mkdir(file_path_base + "train")
os.mkdir(file_path_base + "val")
os.mkdir(file_path_base + "test")
#Makes the validation, testing, and training folders.

weather_identifier = ['dew','fogsmog','frost','glaze', 'hail', 'lightning', 'rain', 'rainbow', 'rime', 'sandstorm', 'snow']

for weather_type in weather_identifier: #We have to do this for every classification type.
    os.mkdir(file_path_base + "train/" + weather_type)
    os.mkdir(file_path_base + "val/" + weather_type)
    os.mkdir(file_path_base + "test/" + weather_type)
    for fname in os.listdir(file_path_base + weather_type): #This goes through the files in the directory
        counter += 1 #Increment counter
        old_filepath = file_path_base + weather_type + "/" + fname #Setting the old filepath
        if counter%10 == 0: #This ensure that we only move every 10th picture
            new_filepath = file_path_base + "val/" + weather_type + "/" + fname
            #After setting the old and new filepath, we use os.rename to actually move it.
            #Where old_filepath is is where the path being replaced is goes, and new_filepath is where 
            #the replacing filepath goes.
            os.rename(old_filepath,new_filepath)
        elif counter %10 == 1:
            new_filepath = file_path_base + "test/" + weather_type + "/" + fname
            os.rename(old_filepath,new_filepath)
        else:
            new_filepath = file_path_base + "train/" + weather_type + "/" + fname
            os.rename(old_filepath, new_filepath)
    print(weather_type + " done being moved")
