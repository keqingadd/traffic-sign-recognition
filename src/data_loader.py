import torch
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader, random_split
import matplotlib.pyplot as plt
import numpy as np
import os
import csv
from PIL import Image

class GTSRBDataset(Dataset):
    """Custom GTSRB dataset loader for Kaggle format."""
    
    def __init__(self, root_dir, split='train', transform=None):
        self.root_dir = root_dir
        self.split = split
        self.transform = transform
        self.samples = []
        
        if split == 'train':
            train_dir = os.path.join(root_dir, 'GTSRB', 'Final_Training', 'Images')
            for class_id in range(43):
                class_dir = os.path.join(train_dir, f'{class_id:05d}')
                if os.path.exists(class_dir):
                    csv_file = os.path.join(class_dir, f'GT-{class_id:05d}.csv')
                    with open(csv_file, 'r') as f:
                        reader = csv.DictReader(f, delimiter=';')
                        for row in reader:
                            img_path = os.path.join(class_dir, row['Filename'])
                            self.samples.append((img_path, int(row['ClassId'])))
        else:
            test_dir = os.path.join(root_dir, 'GTSRB', 'Final_Test', 'Images')
            csv_file = os.path.join(test_dir, 'GT-final_test.test.csv')
            with open(csv_file, 'r') as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    img_path = os.path.join(test_dir, row['Filename'])
                    self.samples.append((img_path, int(row['ClassId'])))
    
    def __len__(self):
        return len(self.samples)
    
    def __getitem__(self, idx):
        img_path, label = self.samples[idx]
        image = Image.open(img_path).convert('RGB')
        
        if self.transform:
            image = self.transform(image)
        
        return image, label

def get_data_transforms():
    """Define data transforms with augmentation for training and testing."""
    train_transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.RandomHorizontalFlip(p=0.3),
        transforms.RandomRotation(10),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    test_transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    return train_transform, test_transform

def load_gtsrb_data(data_dir='./data/gtsrb', batch_size=64):
    """Load and preprocess GTSRB dataset."""
    train_transform, test_transform = get_data_transforms()
    
    # Load full training set
    full_dataset = GTSRBDataset(
        root_dir=data_dir, 
        split='train', 
        transform=train_transform
    )
    
    # Split into train (80%), val (10%), test (10%)
    total = len(full_dataset)
    train_size = int(0.8 * total)
    val_size = int(0.1 * total)
    test_size = total - train_size - val_size
    
    train_dataset, val_dataset, test_dataset = random_split(
        full_dataset, [train_size, val_size, test_size]
    )
    
    # Create data loaders
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    return train_loader, val_loader, test_loader

def visualize_samples(loader, num_samples=10):
    """Visualize sample images from the dataset."""
    # Get class names (GTSRB has 43 classes)
    classes = [str(i) for i in range(43)]
    
    # Get some random samples
    dataiter = iter(loader)
    images, labels = next(dataiter)
    
    # Plot images
    fig, axes = plt.subplots(2, 5, figsize=(12, 6))
    for i, ax in enumerate(axes.flat):
        if i < len(images):
            # Convert tensor to numpy and transpose for plotting
            img = images[i].numpy().transpose(1, 2, 0)
            # Denormalize
            img = img * 0.5 + 0.5
            ax.imshow(img)
            ax.set_title(f'Label: {labels[i].item()}')
            ax.axis('off')
    plt.tight_layout()
    plt.savefig('results/sample_images.png')
    plt.show()