import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm
import matplotlib.pyplot as plt
import os

def train_model(model, train_loader, val_loader, device, 
                num_epochs=30, learning_rate=0.001):
    """Train the model with Adam optimizer and LR scheduler."""
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='max', factor=0.5, patience=3)
    
    train_losses = []
    val_losses = []
    train_accs = []
    val_accs = []
    learning_rates = []
    
    best_val_acc = 0.0
    
    for epoch in range(num_epochs):
        current_lr = optimizer.param_groups[0]['lr']
        learning_rates.append(current_lr)
        
        # Training phase
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0
        
        train_bar = tqdm(train_loader, desc=f'Epoch {epoch+1}/{num_epochs}')
        for images, labels in train_bar:
            images, labels = images.to(device), labels.to(device)
            
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            
            train_bar.set_postfix({'loss': running_loss/len(train_loader), 
                                   'acc': 100.*correct/total})
        
        train_loss = running_loss / len(train_loader)
        train_acc = 100. * correct / total
        train_losses.append(train_loss)
        train_accs.append(train_acc)
        
        # Validation phase
        model.eval()
        val_loss = 0.0
        correct = 0
        total = 0
        
        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                loss = criterion(outputs, labels)
                val_loss += loss.item()
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
        
        val_loss = val_loss / len(val_loader)
        val_acc = 100. * correct / total
        val_losses.append(val_loss)
        val_accs.append(val_acc)
        
        print(f'Epoch {epoch+1}: Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.2f}%, '
              f'Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.2f}%, LR: {current_lr:.6f}')
        
        # Learning rate scheduling
        scheduler.step(val_acc)
        
        # Save best model
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), 'results/best_model.pth')
    
    return train_losses, val_losses, train_accs, val_accs, learning_rates

def plot_training_history(train_losses, val_losses, train_accs, val_accs, learning_rates, model_name):
    """Plot training history with learning rate."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Loss plot
    axes[0, 0].plot(train_losses, label='Train Loss', color='blue', linewidth=2)
    axes[0, 0].plot(val_losses, label='Val Loss', color='orange', linewidth=2)
    axes[0, 0].set_xlabel('Epoch', fontsize=12)
    axes[0, 0].set_ylabel('Loss', fontsize=12)
    axes[0, 0].set_title(f'{model_name} - Loss Curves', fontsize=14)
    axes[0, 0].legend(fontsize=11)
    axes[0, 0].grid(True, alpha=0.3)
    
    # Accuracy plot
    axes[0, 1].plot(train_accs, label='Train Acc', color='blue', linewidth=2)
    axes[0, 1].plot(val_accs, label='Val Acc', color='orange', linewidth=2)
    axes[0, 1].set_xlabel('Epoch', fontsize=12)
    axes[0, 1].set_ylabel('Accuracy (%)', fontsize=12)
    axes[0, 1].set_title(f'{model_name} - Accuracy Curves', fontsize=14)
    axes[0, 1].legend(fontsize=11)
    axes[0, 1].grid(True, alpha=0.3)
    
    # Learning rate plot
    axes[1, 0].plot(learning_rates, label='Learning Rate', color='green', linewidth=2)
    axes[1, 0].set_xlabel('Epoch', fontsize=12)
    axes[1, 0].set_ylabel('Learning Rate', fontsize=12)
    axes[1, 0].set_title(f'{model_name} - Learning Rate Schedule', fontsize=14)
    axes[1, 0].legend(fontsize=11)
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_yscale('log')
    
    # Train vs Val Accuracy Difference
    acc_diff = [t - v for t, v in zip(train_accs, val_accs)]
    axes[1, 1].plot(acc_diff, label='Train-Val Gap', color='red', linewidth=2)
    axes[1, 1].axhline(y=0, color='black', linestyle='--', alpha=0.5)
    axes[1, 1].set_xlabel('Epoch', fontsize=12)
    axes[1, 1].set_ylabel('Accuracy Difference (%)', fontsize=12)
    axes[1, 1].set_title(f'{model_name} - Overfitting Analysis', fontsize=14)
    axes[1, 1].legend(fontsize=11)
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'results/{model_name}_training_history.png', dpi=150, bbox_inches='tight')
    plt.show()