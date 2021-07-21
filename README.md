# Speech Recognition on Android with Quartznet

## Introduction

Exporting the thunder-speech quartznet model to use inside android.
The same process can be done to other models in the library, like citrinet or wav2vec
and the exported torchscript model will have the same interface, meaning that the android code doesn't require modification.

This is a direct port of the official speech recognition example from pytorch, [here](https://github.com/pytorch/android-demo-app/tree/master/SpeechRecognition).

## Prerequisites

* thunder-speech (Optional)
* Python 3.8+ (Optional)
* Android Pytorch library 1.8
* Android Studio 4.0.1 or later

## Quick Start

### 1. Prepare the Model

First, run the following commands on a Terminal:

```
git clone https://github.com/scart97/quartznet-android
cd quartznet-android
```

If you don't have PyTorch installed or want to have a quick try of the demo app, you can download the scripted quartznet model [here](https://github.com/scart97/quartznet-android/releases/tag/model_example), then move the model.pt file to the app/src/main/assets/ folder.

Be aware that the downloadable model file was created with PyTorch 1.9.0, matching the PyTorch Android library 1.9.0 specified in the project's `build.gradle` file as `implementation 'org.pytorch:pytorch_android:1.9.0'`. If you use a different version of PyTorch to create your model by following the instructions below, make sure you specify the same PyTorch Android library version in the `build.gradle` file to avoid possible errors caused by the version mismatch.

### 2. Build and run with Android Studio

Start Android Studio, open the project, build and run the app on an Android device. After the app runs, tap the Start button and start saying something; after a couple of seconds, the model will infer to recognize your speech. Only basic decoding of the recognition result from an array of floating numbers of logits to a list of tokens is provided in this demo app, but it is easy to see, without further post-processing, whether the model can recognize your utterances.