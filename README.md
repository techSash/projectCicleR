# projectCicleR

### In collaboration with Dhruv Hariharan

This github repository contains all the code for our projectCicleR. This project focuses on ting a solution to reducing waste from the ladfills by segregating organic and recyclable garbage with the help of Computer vision and IoT. 

We also built a webapp for easy access to the deep mearning model. The web app is accessible at http://projectcicler.pythonanywhere.com/

For segregating the waste, we built a Convolutional Neural Network with three convolutional layers and three layers in the feed forward network. Even though this is a simple model, we were able to achieve a raw accuracy of 88%. 

For the dataset, we scraped images from the internet of organic and recyclable waste. The dataset contains 22564 training set and 2513 validation set. The dataset can be accessed from [this link](https://www.kaggle.com/datasets/techsash/waste-classification-data)

This repository also contains the code for the webapp which was built using django. To set up the webapp in your local system, clone this repository and install the requirements in the requirements.txt. 

Some of the major requirements for the webapp are 
1. Django
2. Tensorflow
3. numpy
4. basic_classifier.h5 (this is available in models/basic_classifier.h5)

Please note that th4e DJANO_SECRET_KEY has been hidden in this project, and will have to be generated to run correctly in the local system.

You can also access the script for building the model we used under this scripts folder. 
