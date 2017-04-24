# qa_skill

Instructions:

Run word2VecModel.py

This code uses the google news word embedding pretrained model. At first luanch, the program should install several dependencies.
It will also download the pretrained model, which is about 2.5Gb. Please be patient.

After you have downloaded the model, you can comment out the 22nd line in word2VecModel.py which fetches the model.

Each time you run the code, it will load the downloaded model, which takes a few minutes.

To use the classification, type the question or a sentence when prompted. If the input falls into a group of question types,
it shall be included in the return. It will also include the key information extracted from the input, and the classification that
the input is categorized.

There are four categories: Criticize, General, iFEED, Vassar, each corresponds to a branch of Daphne scheme. The sample questions are
located in the /data folder. To add sample questions, add to the txt file with each new question on a new line. To add a category, simply
create a new txt file with sample questions in it.





Note: becuase we have not set a valve for what is the lowest requirement for a classification, if you enter a random word/sentence/question that
has no correlation to any category, it will most likely get a classification what so ever to one of the category.
Remeber this is a little demo and test, it will need furthur work.
