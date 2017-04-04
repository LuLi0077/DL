# Generate TV Scripts using RNNs

Generate [Simpsons](https://en.wikipedia.org/wiki/The_Simpsons) TV scripts using part of the [Simpsons dataset](https://www.kaggle.com/wcukierski/the-simpsons-by-the-data) of scripts from 27 seasons.  The Neural Network will generate a new TV script for a scene at [Moe's Tavern](https://simpsonswiki.com/wiki/Moe's_Tavern). 

`tv_script_generation.ipynb` - 

* Get the data
* Explore the data
* Preprocess: lookup table; tokenize punctuation
* Build the Neural Network
* Train the Neural Network
* Generate TV script

The TV script doesn't make any sense.  We trained on less than a megabyte of text.  In order to get good results, we'll have to use a smaller vocabulary or get more data.  Luckly there's more [data](https://www.kaggle.com/wcukierski/the-simpsons-by-the-data)!  