# Transfer Learning with AlexNet, VGG, Inception and ResNet

Transfer learning is the practice of starting with a network that has already been trained, and then applying that network to your own problem.

Because neural networks can often take days or even weeks to train, transfer learning (i.e. starting with a network that somebody else has already trained) can greatly shorten training time.

Two popular methods are feature extraction and finetuning:
* Feature extraction - Take a pretrained neural network and replace the final (classification) layer with a new classification layer, or perhaps even a small feedforward network that ends with a new classification layer. During training the weights in all the pre-trained layers are frozen, so only the weights for the new layer(s) are trained. In other words, the gradient doesn't flow backwards past the first new layer.
* Finetuning - This is similar to feature extraction except the pre-trained weights aren't frozen. The network is trained end-to-end.

Here we will focus on feature extraction since it's less computationally intensive.

We'll use two datasets in this lab:

1. German Traffic Sign Dataset
2. Cifar10

Unless you have a powerful GPU, running feature extraction on these models will take a significant amount of time. To make things we precomputed **bottleneck features** for each (network, dataset) pair, this will allow you experiment with feature extraction even on a modest CPU. You can think of bottleneck features as feature extraction but with caching.  Because the base network weights are frozen during feature extraction, the output for an image will always be the same. Thus, once the image has already been passed once through the network we can cache and reuse the output.

The files are encoded as such:

- {network}_{dataset}_bottleneck_features_train.p
- {network}_{dataset}_bottleneck_features_validation.p

network can be one of 'vgg', 'inception', or 'resnet'

dataset can be on of 'cifar10' or 'traffic'