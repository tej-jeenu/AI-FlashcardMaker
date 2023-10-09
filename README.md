# FlashcardMaker
This app is designed to convert specification points in AQA specifications into a CSV file containing equivalent flashcard questions which can be used for Anki. The app uses YOLOV8 to create bounding boxes around the relevant specification points and crop those bounding boxes as images. Once the images are cropped tesseract is used to extract the text from those pictures. Finally, the ChatGPT API is used to prompt ChatGPT to convert the specification points into questions that can be used for a flashcard.

This project is still in progress so I will continue to add improvements


## Inspiration and reason behind making application
I myself was once I student who used to learn vast amounts of information from resources given by teachers, only to realize that not every bit of the given resource is actually relevant for the exam. From the perspective of A Levels and GCSE's, I also realised it was the same case. Teachers would give resources such as handouts, powerpoints, notes, textbooks and would contain vast amounts of information. The likelihood is that people try to make revision resources to learn this A Level and GCSE content which takes a lot of time to create. While it isn't a bad thing to create resources it does take a large chunk of time and pupils are not learning anything effectively in that time. With this understanding, I wanted to create something which will cut down time to create effective revision resources significantly to allow students to have more time in the day to ACTUALLY effectively learn content. Furthermore, I realized that alongside the vast amounts of content being given, not every bit of content that teachers teach and give as resources is not necessarily examined. This renders some of the information to be useless but pupils would still try and learn this content as it is guided to them by teachers. This is therefore another area where pupils waste time in the process of revision. together I therefore wanted to make an app that cuts down the time to make revision resources and also highlights ONLY the relevant information.

## key technologies which my app uses
- Python Programming Language for writing the code
- Tkinter Python Framework for creating a UI to use the app
- Ultralytics Python Library to allow me to train and create a yolov8 object detection AI model
- ChatGPT API to allow me to rephrase statements into flashcard questions
- pytesseract python library to extract strings for images
- pdf2image python library to convert all pages in a pdf to images


## How I used my key technologies to create my app
I realise that the best way to retrieve only the relevant exam information that needs to be learnt is by referencing exam specifications. Within exam specifications, there are specification points that refer to information that needs to be known. I realised that if I could rephrase specification points into flashcard questions it would do most of the work in making flashcards. Since my aim was to improve revision effectiveness, I decided to target an effective revision technique that was already in use. This is the reason I decided to target flashcard making. In the process of thinking about how I can aid flashcard making, I was already using ANKI at the time for my own studying and discovered that it can take CSV files and turn them into flashcards if the CSV file was laid out in a certain format. All together with this information I discovered, I realised that if I could find a way to first isolate specification points from a specification, rephrase them as flashcard questions and append them to a CSV in a structure that ANKI understands then I would be able to create half of all the flashcards needed for GCSE and A Level Exams. This would cut down time in thinking about what flashcards to create and how the flashcard questions need to be phrased as well as filling in the first side of the flashcards. With the understanding of the processes I needed to do, I will now explain how I carried out the processes.

The first step was to extract the specification points from the specification. the reason why this is an important step is that specifications can contain a lot of unnecessary information like headers, titles, and extra information which aren't needed and therefore need to be eliminated. I realised using an AI model would be the best solution as there was always a set pattern for the layout of the specification points. From my perspective, I decided to look at AQA specifications since I had used them for my exams. I realised that every time specification points were mentioned they would always have a header called "Content" in a set pattern and colour in an outlined box. I knew that an AI model could easily recognise these patterns if I could train it with labelled image data of pages in a specification. I, therefore, used the YOLOv8 python library as it was specialised for image and object detection and therefore would create the best possible AI model for my purpose. it would essentially create bounding boxes over the patterns I trained the model to detect. These bounding boxes could be used as outlines to crop the image with the same library. Once I had the cropped images I needed to extract the specification points as strings so I could rephrase the points. This is when I used the pytesseract library which calls the tesseract OCR engine for extracting text from images. when using this I was able to get the specification points as text. 

I wanted to add each specification point to a list and realised that for AQA specifications a full stop was used at the end of each specification point. I therefore used a full stop as a delimeter to split the string into a list. Now I had all the specification points in a list I needed to convert them into flashcard questions. Initially, I tried to see if I could use NLP to do this however this was quite difficult due to the variety of how specification point statements are phrased. I experimented with ChatGPT to see if it could rephrase statements instead since I knew it was very good at handling commands like these. In experimenting I found that it was rephrasing really well and probably better than I could've done with my own NLP model. I, therefore, decided to utilise the GPT API since it was already doing my required function best. I created a custom prompt as a string " Can you convert x into a flashcard question?" where x was one of the specification points in my list. For each specification point I simply sent this prompt and got a flashcard question that I can use back adding it to another list.

Finally, I have my list of flashcard questions so I had to append them to a CSV file with the structure "question,-". The structure was used for each row of the CSV file to represent the front and back of a flashcard. I was able to then import this CSV file and my flashcards would be displayed in the correct format in ANKI.

In terms of how the user would interact with these processes, I made a tkinter UI in Python which will allow the user to input an AQA specification able to specify page numbers to look at specifications points and then output a CSV file with the matching questions associated with the specification point locations specified. I used pdf2image to convert the specification as a pdf file into a series of images which can be used as inputs for my trained AI object detection model.

## what went well
- trained AI model was completely accurate when testing with multiple GCSE and A-level specifications (trained at 300 epochs)
- pytesseract extracted text accurately
- GPT API effectively returned flashcard questions which were phrased in the best way possible and made sense

## potential improvements
- utilising a payed version of chatgpt as free api calls are very slow and sometimes crash








