# EmotionDetector
This is the code repository for Alae-Eddine Sahbou Emotion Detector project. This program uses computer vision and facial analysis techniques to detect and recognize emotions in real-time video feed.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3
- OpenCV 
- deepface library 

### Installing
1. Clone the repository to your local machine
2. Install the required libraries by running the following command:
```pip install opencv-python deepface```
3. Run the program using the command:
```python emotion_detector.py```

### Building APK and Desktop App

To build the program into an APK file for android, you can use the tool called Buildozer.

1. Install Buildozer by running the following command:
```pip install buildozer```
2. Create a new buildozer.spec file in the root of your project directory.
3. In the buildozer.spec file, specify the requirements for your APK.
4. Run the following command to build the APK:
```buildozer android debug```

### To build the program into a desktop app, you can use the tool called PyInstaller.

1. Install PyInstaller by running the following command:
```pip install pyinstaller```
2. Run the following command to build the desktop app:
```pyinstaller --onefile emotion_detector.py```

## Note

The haarcascade_frontalface_default.xml file is a pre-trained classifier for detecting faces in images. This file is used by OpenCV to detect faces in the video feed. You can find more information about this file and how to use it on the OpenCV documentation website.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/alaesahbou/EmotionDetector/blob/master/LICENSE) file for details.
