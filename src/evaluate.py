import torch
import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc

def evaluate_model(model, test_loader, device):
    """Evaluate model on test set."""
    model.eval()
    all_preds = []
    all_labels = []
    all_probs = []
    
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            probs = torch.nn.functional.softmax(outputs, dim=1)
            _, predicted = torch.max(outputs, 1)
            all_preds.extend(predicted.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
            all_probs.extend(probs.cpu().numpy())
    
    # Calculate metrics
    accuracy = accuracy_score(all_labels, all_preds)
    precision, recall, f1, _ = precision_recall_fscore_support(all_labels, all_preds, average='weighted')
    
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'predictions': all_preds,
        'labels': all_labels,
        'probabilities': np.array(all_probs)
    }

def plot_confusion_matrix(labels, preds, num_classes=43):
    """Plot confusion matrix."""
    cm = confusion_matrix(labels, preds)
    plt.figure(figsize=(12, 10))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=range(num_classes), yticklabels=range(num_classes))
    plt.xlabel('Predicted Class', fontsize=12)
    plt.ylabel('True Class', fontsize=12)
    plt.title('Confusion Matrix', fontsize=14)
    plt.tight_layout()
    plt.savefig('results/confusion_matrix.png', dpi=150, bbox_inches='tight')
    plt.show()

def plot_per_class_metrics(labels, preds, num_classes=43):
    """Plot per-class precision, recall, and F1-score."""
    precision, recall, f1, support = precision_recall_fscore_support(labels, preds, average=None)
    
    x = np.arange(num_classes)
    width = 0.25
    
    fig, ax = plt.subplots(figsize=(16, 6))
    bars1 = ax.bar(x - width, precision, width, label='Precision', color='steelblue')
    bars2 = ax.bar(x, recall, width, label='Recall', color='orange')
    bars3 = ax.bar(x + width, f1, width, label='F1-Score', color='green')
    
    ax.set_xlabel('Class', fontsize=12)
    ax.set_ylabel('Score', fontsize=12)
    ax.set_title('Per-Class Precision, Recall, and F1-Score', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(range(num_classes), fontsize=8)
    ax.legend(fontsize=11)
    ax.set_ylim([0, 1.1])
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('results/per_class_metrics.png', dpi=150, bbox_inches='tight')
    plt.show()

def plot_class_distribution(labels, num_classes=43):
    """Plot class distribution in test set."""
    class_counts = np.bincount(labels, minlength=num_classes)
    
    fig, ax = plt.subplots(figsize=(14, 5))
    colors = plt.cm.Set3(np.linspace(0, 1, num_classes))
    bars = ax.bar(range(num_classes), class_counts, color=colors)
    
    ax.set_xlabel('Class', fontsize=12)
    ax.set_ylabel('Number of Samples', fontsize=12)
    ax.set_title('Test Set Class Distribution', fontsize=14)
    ax.set_xticks(range(num_classes))
    ax.set_xticklabels(range(num_classes), fontsize=8)
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('results/class_distribution.png', dpi=150, bbox_inches='tight')
    plt.show()

def plot_confidence_distribution(labels, probs, num_classes=43):
    """Plot prediction confidence distribution."""
    max_probs = np.max(probs, axis=1)
    correct_mask = np.array(labels) == np.argmax(probs, axis=1)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(max_probs[correct_mask], bins=30, alpha=0.7, label='Correct Predictions', color='green', density=True)
    ax.hist(max_probs[~correct_mask], bins=30, alpha=0.7, label='Wrong Predictions', color='red', density=True)
    
    ax.set_xlabel('Prediction Confidence', fontsize=12)
    ax.set_ylabel('Density', fontsize=12)
    ax.set_title('Prediction Confidence Distribution', fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('results/confidence_distribution.png', dpi=150, bbox_inches='tight')
    plt.show()

def visualize_predictions(model, test_loader, device, num_samples=10):
    """Visualize model predictions on test samples."""
    model.eval()
    dataiter = iter(test_loader)
    images, labels = next(dataiter)
    images, labels = images.to(device), labels.to(device)
    
    with torch.no_grad():
        outputs = model(images)
        probs = torch.nn.functional.softmax(outputs, dim=1)
        _, predicted = torch.max(outputs, 1)
    
    fig, axes = plt.subplots(2, 5, figsize=(14, 7))
    for i, ax in enumerate(axes.flat):
        if i < len(images):
            img = images[i].cpu().numpy().transpose(1, 2, 0)
            img = img * 0.5 + 0.5  # Denormalize
            ax.imshow(img)
            color = 'green' if predicted[i] == labels[i] else 'red'
            conf = probs[i][predicted[i]].item() * 100
            ax.set_title(f'True: {labels[i].item()} | Pred: {predicted[i].item()}\nConf: {conf:.1f}%', 
                        color=color, fontsize=10)
            ax.axis('off')
    plt.suptitle('Model Predictions (Green=Correct, Red=Wrong)', fontsize=14, y=1.02)
    plt.tight_layout()
    plt.savefig('results/predictions.png', dpi=150, bbox_inches='tight')
    plt.show()