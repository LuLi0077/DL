# Intro to RNN

Recurrent Neural Networks are a type of neural network architecture specially suited for handling sequences such as text, and audio. 

Build a character-wise RNN trained on Anna Karenina. It'll be able to generate new text based on the text from the book.

This network is based off of Andrej Karpathy's [post on RNNs](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) and [implementation in Torch](https://github.com/karpathy/char-rnn). Also, some information [here at r2rt](http://r2rt.com/recurrent-neural-networks-in-tensorflow-ii.html) and from [Sherjil Ozair](https://github.com/sherjilozair/char-rnn-tensorflow) on GitHub. Below is the general architecture of the character-wise RNN.

<img src="charseq.jpeg" width="500">

`Intro_to_RNN.ipynb`
* Load the text file
* Making training and validation batches
* Building the model
* Training
* Sampling


### Resources
* [Attention and Augmented Recurrent Neural Networks](http://distill.pub/2016/augmented-rnns/)
* [A Beginner’s Guide to Recurrent Networks and LSTMs](https://deeplearning4j.org/lstm.html)
* [Recurrent Neural Networks in Tensorflow I](http://r2rt.com/recurrent-neural-networks-in-tensorflow-i.html)
* [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* [LSTM Networks for Sentiment Analysis](http://deeplearning.net/tutorial/lstm.html)
* [LSTM Networks for Sentiment Analysis on Tweets](http://k8si.github.io/2016/01/28/lstm-networks-for-sentiment-analysis-on-tweets.html)
* [Deep Learning Sentiment One Character at a T-i-m-e](https://gab41.lab41.org/deep-learning-sentiment-one-character-at-a-t-i-m-e-6cd96e4f780d#.9luqnhbfa)
* [Lexicon-Based Methods for Sentiment Analysis](https://www.aclweb.org/anthology/J/J11/J11-2001.pdf)
* [A comparison of Lexicon-based approaches for Sentiment Analysis of microblog posts](http://ceur-ws.org/Vol-1314/paper-06.pdf)
* [Time Series Prediction with LSTM Recurrent Neural Networks in Python with Keras](http://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/)
