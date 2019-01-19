# DeeptechAIGarbageCollectors
Project for the Deeptech AI Hackathon

The Python files are direct exports from their corresponding Jupyter Notebooks.

datavalue.py is the script which searches for the Impressum on a Website and finds the zip code and the cityname of the address via Regex.

findingnouns.py contains the code for loading the german tagger and tag the text and find the 5 most significant words.

imagecruncher.py transforms the screenshots to a grayscaled 84x48 image.

screenshotnetwork.py contains the CNN for classifying the Screenshots.

textnetwork.py contains the Feed Forward Network for classifying the word embeddings.

website_screenshot_generator.py is the script for creating the Screenshots of the URLs.

word2vec.py uses the list of significant words and creates 10 dimensional embeddings from them.

wordextraction.py downloads all the clear text from a URL.

All those scripts are interconnected by pickle files which get created after running a script. The next script in the pipeline loads its corresponding input pickles and creates own pickles as output, and so forth.
