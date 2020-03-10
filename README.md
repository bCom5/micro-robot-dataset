# Micro-robot Dataset
We pull images from [Tiny-Imagenet](https://tiny-imagenet.herokuapp.com/) and create three datasets for Micro-robot
purposes. Each class has 500 training images and 50 testing images:

10 classes of outdoor objects a micro-robot may encounter.

1. acorn
2. basketball
3. bee
4. black_widow
5. frog
6. ladybug
7. mushroom
8. nail
9. snail
10. tarantula

10 classes of indoor objects a micro-robot may encounter.

1. banana
2. candle
3. dumbbell
4. iPod
5. pill_bottle
6. pop_bottle
7. sandal
8. sock
9. syringe
10. teapot

20 classes combining the indoor and outdoor objects.

## To Use:

1. Run `sh setup.sh` __in the current directory__.
2. Use an `ImageFolder`/`DataLoader` in PyTorch, implementation from outside this directory.
