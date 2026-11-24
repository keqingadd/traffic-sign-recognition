import torch
import os
from src.data_loader import load_gtsrb_data, visualize_samples
from src.models import get_model
from src.train import train_model, plot_training_history
from src.evaluate import (evaluate_model, plot_confusion_matrix, visualize_predictions,
                          plot_per_class_metrics, plot_class_distribution, plot_confidence_distribution)
from src.utils import set_device, save_model

def main():
    os.makedirs('results', exist_ok=True)
    
    device = set_device()
    
    print("Loading GTSRB dataset...")
    train_loader, val_loader, test_loader = load_gtsrb_data(batch_size=64)
    
    print("Visualizing sample images...")
    visualize_samples(train_loader, num_samples=10)
    
    # Plot class distribution
    print("Plotting class distribution...")
    all_labels = []
    for _, labels in test_loader:
        all_labels.extend(labels.numpy())
    plot_class_distribution(all_labels)
    
    # Only train LeNet-5
    model = get_model('lenet5', num_classes=43)
    model = model.to(device)
    
    num_epochs = 30
    learning_rate = 0.001
    
    print("\n" + "="*50)
    print("Training LeNet-5 (Enhanced)")
    print("="*50)
    
    train_losses, val_losses, train_accs, val_accs, learning_rates = train_model(
        model, train_loader, val_loader, device,
        num_epochs=num_epochs, learning_rate=learning_rate
    )
    
    plot_training_history(train_losses, val_losses, train_accs, val_accs, learning_rates, 'lenet5')
    
    # Load best model and evaluate
    model.load_state_dict(torch.load('results/best_model.pth'))
    metrics = evaluate_model(model, test_loader, device)
    
    print("\nLeNet-5 Results:")
    print(f"Accuracy:  {metrics['accuracy']:.4f}")
    print(f"Precision: {metrics['precision']:.4f}")
    print(f"Recall:    {metrics['recall']:.4f}")
    print(f"F1 Score:  {metrics['f1']:.4f}")
    
    # Generate all visualizations
    print("\nGenerating visualizations...")
    plot_confusion_matrix(metrics['labels'], metrics['predictions'])
    plot_per_class_metrics(metrics['labels'], metrics['predictions'])
    plot_confidence_distribution(metrics['labels'], metrics['probabilities'])
    visualize_predictions(model, test_loader, device)
    
    # Save results
    save_model(model, 'results/lenet5_final.pth')
    
    with open('results/comparison.txt', 'w') as f:
        f.write(f"lenet5_enhanced: Accuracy={metrics['accuracy']:.4f}, Precision={metrics['precision']:.4f}, "
                f"Recall={metrics['recall']:.4f}, F1={metrics['f1']:.4f}\n")
    
    print("\n" + "="*50)
    print("All results saved to results/ directory")
    print("="*50)

if __name__ == '__main__':
    main()
