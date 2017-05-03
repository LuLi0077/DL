# Autoencoders

Build a simple autoencoder to compress the MNIST dataset. With autoencoders, we pass input data through an encoder that makes a compressed representation of the input. Then, this representation is passed through a decoder to reconstruct the input data. Generally the encoder and decoder will be built with neural networks, then trained on example data.

<img src="Autoencoders/assets/autoencoder_1.png" width="600">


## `Simple_Autoencoder.ipynb`

Build a simple network architecture for the encoder and decoder:

<img src="Autoencoders/assets/simple_autoencoder.png" width="600">


## `Convolutional_Autoencoder.ipynb`

Improve our autoencoder's performance using convolutional layers:

<img src="Autoencoders/assets/convolutional_autoencoder.png" width="600">

The encoder part of the network will be a typical convolutional pyramid. Each convolutional layer will be followed by a max-pooling layer to reduce the dimensions of the layers. The decoder needs to convert from a narrow representation to a wide reconstructed image. For example, the representation could be a 4x4x8 max-pool layer. This is the output of the encoder, but also the input to the decoder. We want to get a 28x28x1 image out from the decoder so we need to work our way back up from the narrow decoder input layer.

Here our final encoder layer has size 4x4x8 = 128. The original images have size 28x28 = 784, so the encoded vector is roughlt 16% the size of the original image. These are just suggested sizes for each of the layers.

* Note: deconvolutional layers can lead to artifacts in the final images, such as checkerboard patterns. This is due to overlap in the kernels which can be avoided by setting the stride and kernel size equal. In [this Distill article](http://distill.pub/2016/deconv-checkerboard/) from Augustus Odena, *et al*, the authors show that these checkerboard artifacts can be avoided by resizing the layers using nearest neighbor or bilinear interpolation (upsampling) followed by a convolutional layer.

### Denoising

Autoencoders can be used to denoise images quite successfully just by training the network on noisy images. We'll use noisy images as input and the original, clean images as targets. Here's an example of the noisy and the denoised images.

<img src="Autoencoders/assets/denoising.png" width="600">


## Resources

* [Tutorial - What is a variational autoencoder?](https://jaan.io/what-is-variational-autoencoder-vae-tutorial/)
* [Introducing Variational Autoencoders (in Prose and Code)](http://blog.fastforwardlabs.com/2016/08/12/introducing-variational-autoencoders-in-prose-and.html)
* [Under the Hood of the Variational Autoencoder (in Prose and Code)](http://blog.fastforwardlabs.com/2016/08/22/under-the-hood-of-the-variational-autoencoder-in.html)
* [Variational Autoencoders Explained](http://kvfrans.com/variational-autoencoders-explained/)
* [Variational Autoencoder in TensorFlow](https://jmetzen.github.io/2015-11-27/vae.html)

