# Image-colorization
An attempt to colorise black and white images via the use of Auto-encoders.

## Introduction

Autoencoders are a specific type of feedforward neural networks where the input is the same as the output. They compress the input into a lower-dimensional code and then reconstruct the output from this representation. The code is a compact “summary” or “compression” of the input, also called the latent-space representation.

An autoencoder consists of 3 components:

1. encoder : compresses the input and produces the code
2. code
3. decoder : reconstructs the input only using this code.

## What we need :

1. Encoding Method
2. Decoding Method
3. Loss Function to compare the outputs with the target

## Dataset: 

The COCO-2017 Dataset's validation directory is used over here in the model due to the system's limited storage capacity. We will be converting the given images into black & white to create the desired dataset. 

## How to work :

```
sh datacreation.sh
python data_manipulation.py

```
