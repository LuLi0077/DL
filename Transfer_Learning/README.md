# Transfer Learning with AlexNet, VGG, GoogLeNet and ResNet

Transfer learning involves taking a pre-trained neural network and adapting the neural network to a new, different data set.

Four cases when using transfer learning:
![Guide](https://github.com/LuLi0077/DL/blob/master/Transfer_Learning/images/guide.png)

## [AlexNet](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
![AlexNet](https://github.com/LuLi0077/DL/blob/master/Transfer_Learning/images/alexnet.png)

AlexNet is a popular base network for transfer learning because its structure is relatively straightforward, it's not too big, and it performs well empirically.

* [German Traffic Sign dataset](https://d17h27t6h515a5.cloudfront.net/topher/2016/October/580a829f_train/train.p)
* [AlexNet weights](https://d17h27t6h515a5.cloudfront.net/topher/2016/October/580d880c_bvlc-alexnet/bvlc-alexnet.npy)
* `alexnet.py` - TensorFlow implementation of AlexNet (adapted from [Michael Guerhoy and Davi Frossard](http://www.cs.toronto.edu/~guerzhoy/tf_alexnet/)).
* `caffe_classes.py` - AlexNet was trained on the ImageNet database, which has 1000 classes of images.
* `imagenet_inference.py` - ImageNet inference.
* `traffic_sign_inference.py` - Traffic sign inference (Resize Required: AlexNet expects a 227x227x3 pixel image, whereas the traffic sign images are 32x32x3 pixels).
* `feature_extraction.py` - Remove the final, 1000-neuron classification layer and replace it with a new, 43-neuron classification layer.
* `train_feature_extraction.py` - Read in the training dataset and train the network.
* `train_feature_extraction_cifar10.py` - Test model performance using Cifar10 dataset.


## VGG, GoogLeNet and ResNet

These models were trained for days or weeks on the ImageNet dataset. Thus, the weights encapsulate higher-level features learned from training on thousands of classes.

* [ImageNet dataset](http://www.image-net.org/)
* [Cifar10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html)
* `feature_extraction_vgg.py` - Train feature extraction with the VGG network/Cifar10 dataset bottleneck features. The 100 in vgg_cifar10_100 indicates this file has 100 examples per class.