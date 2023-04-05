import argparse
from os import listdir
from classifier import classifier


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--dir", type = str, default = './uploads/',
                        help = "path to the folder of pet images.")

    parser.add_argument("--arch", type = str, default = 'resnet',
                        help = "choose the CNN model to use. resnet(default), vgg, alexnet.(use vgg11 if used on code.cs50.io)")


    in_arg = parser.parse_args()



    direct = listdir(in_arg.dir)
    model = in_arg.arch

    class_label = classifier(in_arg.dir + direct[0], model)
    results = class_label.lower().strip()


    print(results)


if __name__ == "__main__":
    main()
