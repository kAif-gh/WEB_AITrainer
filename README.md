
# Web interface AITrainer 

A prototype Web Application that implements computer Vision model built with OpenCV, Mediapipe and tested with MoveNet.
It can be used to detect the correct pose in an exercise and also to count reps of
a complete movement.

# Goals

The goal is to create practical web inteface easy to use that create a pose detection system, able to recognize the movement
Of a person by creating landmarks on each joint of the body, then calculating 
the different angles to classify if the exercises are correct or not and calculating the number of reps.
In order to do so, i tested Mediapipe and MoveNet to choose the optimal model to work with, in conjunction with OpenCV
to process the video feed of the webcam.



## Technologies

* Python
* Mediapipe
* MoveNet
* OpenCV
* Flask
* html 
* javascript
* CSS



## Usage

You have to install the required packages, you can do it:
* via pip
```bash
  pip install -r requirements.txt
```
Once you installed all the required packages there is two ways to run the exercises of the projects:
* you can type in the command line from the root folder 

```bash
 $env:FLASK_APP="C:\Users\MSI\Desktop\WebAITrainer\routes.py"
```
```bash
 $env:FLASK_ENV = "development"  
```
```bash
 flask run     
```
Or 
```bash
 flask run --host=0.0.0.0 --port=5000      
```

