# Image classifier with python
#### Video Demo: https://youtu.be/Rb958lKVkeQ
#### Description:
so as you know, right now ai(artificial intelligence) is one of the technology trends in the world.

and this is a CNN ai Classifier and the neural network model is vgg11(because that was the only one github supported. the other ones were too heavy) that is pretrained with about 2.1m images in imageNet.

classifier has a number to label txt because classifier returns numbers and we want words.

the webpage also uses bootstrap(for alerts).

the classifier can use alexnet and resnet too but because code.cs50.io couldn't run it, i decided not to bring them in(so right now flask app only has vgg11(but classifier has the other two and can be called through terminal))



## webpage interface
its really simple(i didn't put much effort into it).
<p>so you go into the website.<p>
<p>you upload your image<p>
<p>you click submit<p>
<p>and you wait(for about 15 to 20 seconds in code.cs50.io<p>


### How to launch the application
1. download the archive.
2. download requirements.txt libraries.
3. in terminal go to interface folder.
4. run `flask run`
5. in browser go to `localhost:5000`
6. upload file
7. and done!


## improvments in the Future
- improve ui
- add a section where you can tell what you want to find
- add different CNN models
- improve picture compability


### Definitions:

**CNN(convolutional neural network)**: CNN is a network architecture for deep learning which learns directly from data. CNNs are particularly useful for finding patterns in images to recognize objects. They can also be quite effective for classifying non-image data such as audio, time series, and signal data. a CNN is nothing but a filter that is used to extract the features from the images.

**vgg11**: vgg11 is a neural network model and it has 11 layers(as the number says) and its not the most accurate one or the fastest one. but its definitly one of the lightest models out there!

**vgg16**: vgg16 is like a big brother to vgg11. so it has 5 more layers and its about 6% more accurate.

**resnet**: resnet is another neural network model and it layers vary between 101 and 138! but unlike other models(which higher layers mean higher accuracy), resnet is not that accurate but its definitly fast.

and yes if you are wondering where did the helpers.py go(from the video), i deleted it because as i said in the video i didnt even import it! so it was useless file sitting there. and i dont like useless files(unlike some guys).


