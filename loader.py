import numpy as np
from PIL import Image, ImageEnhance
from torchvision.datasets import ImageFolder
import torchvision.transforms as transforms
import torchvision
import torch
from torch.utils.data import DataLoader

batch_size = 128

def get_transforms(size):
    # Data
    print('==> Preparing data..')

    train_compose = []
    test_compose = []

    # other transformations to add to the list
    if size == 32:
        train_compose.extend([
            transforms.Resize(32),
            transforms.RandomCrop(32, padding=4),
        ])
        test_compose.extend([
            transforms.Resize(32),
        ])
    else:
        # @TODO implement 64x64
        print('Only implemented for 32x32 images!')
        raise NotImplementedError
    
    # note fix the avg and std of dataset
    train_compose.extend([
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
    ])

    test_compose.extend([
        transforms.Resize(32),
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
    ])

    train_transform = transforms.Compose(train_compose)
    test_transform = transforms.Compose(test_compose)

    return train_transform, test_transform

def get_iterators(train_dir, test_dir, size):
    train_transform, test_transform = get_transforms(size)

    train_folder = ImageFolder(train_dir, train_transform)
    test_folder = ImageFolder(test_dir, test_transform)

    train_iterator = DataLoader(
        train_folder, batch_size=batch_size, num_workers=4,
        shuffle=True, pin_memory=True
    )

    test_iterator = DataLoader(
        test_folder, batch_size=256, num_workers=4,
        shuffle=False, pin_memory=True
    )

    # can be useful:
    # train_size = len(train_iterator.dataset)
    # test_size = len(test_iterator.dataset)
    return train_iterator, test_iterator

def get_outdoor_iterators(size=32):
    train_dir = 'micro-robot-dataset/dataset/outdoor/train/'
    test_dir = 'micro-robot-dataset/dataset/outdoor/test/'

    return get_iterators(train_dir, test_dir, size)

def get_indoor_iterators(size=32):
    train_dir = 'micro-robot-dataset/dataset/indoor/train/'
    test_dir = 'micro-robot-dataset/dataset/indoor/test/'

    return get_iterators(train_dir, test_dir, size)

def get_combined_iterators(size=32):
    train_dir = 'micro-robot-dataset/dataset/combined/train/'
    test_dir = 'micro-robot-dataset/dataset/combined/test/'

    return get_iterators(train_dir, test_dir, size)

def get_micro_iterators(size=32):
    train_dir = 'micro-robot-dataset/dataset/micro/train/'
    test_dir = 'micro-robot-dataset/dataset/micro/test/'

    return get_iterators(train_dir, test_dir, size)
