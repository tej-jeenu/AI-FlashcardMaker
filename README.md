# FlashcardMaker
This app is designed to convert specification points in AQA specifications into a CSV file containing equivalent flashcard questions which can be used for Anki. The app uses YOLOV8 to create bounding boxes around the relevant specification points and crop those bounding boxes as images. Once the images are cropped tesseract is used to extract the text from those pictures. Finally, the ChatGPT API is used to prompt ChatGPT to convert the specification points into questions that can be used for a flashcard.

This project is still in progress so I will continue to add improvements


# # Inspiration and reason behind making application
I myself was once I student who used to learn vast amounts of information from resources given by teachers, only to realize that not every bit of the given resource is actually relevant for the exam. From the perspective of A Levels and GCSE's, I also realised it was the same case. Teachers would give resources such as handouts, powerpoints, notes, textbooks and would contain vast amounts of information. The likelihood is that people try to make revision resources to learn this A Level and GCSE content which takes a lot of time to create. While it isn't a bad thing to create resources it does take a large chunk of time and pupils are not learning anything effectively in that time. With this understanding, I wanted to create something which will cut down time to create effective revision resources significantly to allow students to have more time in the day to ACTUALLY effectively learn content. Furthermore, I realized that alongside the vast amounts of content being given, not every bit of content that teachers teach and give as resources is not necessarily examined. This renders some of the information to be useless but pupils would still try and learn this content as it is guided to them by teachers. This is therefore another area where pupils waste time in the process of revision. together I therefore wanted to make an app that cuts down the time to make revision resources and also highlights ONLY the relevant information.

## key technologies which my app uses
- Python Programming Language for writing the code
- Tkinter Python Framework for creating a UI to use the app
- YoloV8 Python Library to allow me to train and create object detection AI model
- ChatGPT API to allow me to rephrase statements into flashcard questions
- pytesseract python library to extract strings for images
- pdf2image python library to convert all pages in a pdf to images


## How I used my key technologies to create my app




