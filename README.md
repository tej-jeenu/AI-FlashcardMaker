# FlashcardMaker
This app is designed to convert specification points in AQA specifications into a CSV file containing equivalent flashcard questions which can be used for Anki
# The app uses YOLOV8 to create bounding boxes around the relevant specification points and crop those bounding boxes as images. Once the images are cropped tesseract is used to extract the text from those pictures.Finally the CHatGPT API is used to prompt CHatGPT to conver the specification points into questions that can be used for a flashcard.
