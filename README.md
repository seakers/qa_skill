# qa_skill

Instructions:

Run word2VecModel.py

This code uses the google news word embedding pretrained model. At first luanch, the program should install several dependencies.
It will also download the pretrained model, which is about 2.5Gb. Please be patient.

After you have downloaded the model, you can comment out the 22nd line in word2VecModel.py which fetches the model.

Each time you run the code, it will load the downloaded model, which takes a few minutes.

To use the classification, type the question or a sentence when prompted. If the input falls into a group of question types,
it shall be incloded in the return. It will also include the key information extracted from the input, and the classification that
the input is categorized.

For demo and testing purposes, this code only includes two types of classifications: university and location.

For example:

1.  Input: 
    is atlanta beautiful
    
    Return: 
    Question Type: KeyInfo: atlanta beautiful 
    Question Classification: location

2.  Input:
	where is california
	Question Type: where KeyInfo: california 
	Question Classification: location
	enter 'stop' to stop the program. please enter your question here: 

3.  Input:
	where is ucla
	Question Type: where KeyInfo: ucla 
	Question Classification: University

Note: becuase we have not set a valve for what is the lowest requirement for a classification, if you enter a random word that
has no correlation to either category, it will most likely get a classification what so ever to the closer yet remotely related category.
Remeber this is a little demo and test, it will need furthur work.
