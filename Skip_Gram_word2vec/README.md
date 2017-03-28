# Skip-gram word2vec

When dealing with language and words, we end up with tens of thousands of classes to predict, one for each word. Trying to one-hot encode these words is massively inefficient, we'll have one element set to 1 and the other 50,000 set to 0. The word2vec algorithm finds much more efficient representations by finding vectors that represent the words. These vectors also contain semantic information about the words. Words that show up in similar contexts, such as "black", "white", and "red" will have vectors near each other. There are two architectures for implementing word2vec, CBOW (Continuous Bag-Of-Words) and Skip-gram.

<img src="images/word2vec_architectures.png" width="600">

In this implementation, we'll be using the skip-gram architecture because it performs better than CBOW. Here, we pass in a word and try to predict the words surrounding it in the text. In this way, we can train the network to learn representations for words that show up in similar contexts.

`Skip-Gram word2vec.ipynb` - 
* Load the [text8 dataset](http://mattmahoney.net/dc/textdata.html)
* Preprocessing `utils.py`
* Subsampling
* Making batches
* Building the graph:

<img src="images/skip_gram_net_arch.png" width="600">  

* Embedding:

<img src="images/word2vec_weight_matrix_lookup_table.png" width="600"> 

* Negative sampling
* Validation
* Training
* Visualizing the word vectors:

<img src="images/output.png" width="600"> 


### Resources
* A really good [conceptual overview](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/) of word2vec from Chris McCormick 
* [First word2vec paper](https://arxiv.org/pdf/1301.3781.pdf) from Mikolov et al.
* [NIPS paper](http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf) with improvements for word2vec also from Mikolov et al.
* An [implementation of word2vec](http://www.thushv.com/natural_language_processing/word2vec-part-1-nlp-with-deep-learning-with-tensorflow-skip-gram/) from Thushan Ganegedara
* TensorFlow [word2vec tutorial](https://www.tensorflow.org/tutorials/word2vec)
* Check out [this post from Christopher Olah](http://colah.github.io/posts/2014-10-Visualizing-MNIST/) to learn more about T-SNE and other ways to visualize high-dimensional data.