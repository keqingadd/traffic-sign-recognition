# Traffic Sign Recognition

Implementation of two CNN models (LeNet-5 and Custom CNN) for traffic sign recognition on GTSRB dataset.

## Requirements

- Python 3.8+
- PyTorch 1.9+
- torchvision
- matplotlib
- scikit-learn
- numpy
- seaborn
- tqdm

## Installation

```bash
pip install -r requirements.txt
```

## Dataset

GTSRB (German Traffic Sign Recognition Benchmark) dataset:
- Download from: https://benchmark.ini.rub.de/
- Place `GTSRB-Training_fixed.zip` in `data/gtsrb/`
- Or use Kaggle: https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign

## Usage

1. Run the main script:
```bash
python main.py
```

2. The script will:
   - Load and preprocess GTSRB dataset
   - Train both LeNet-5 and Custom CNN models
   - Evaluate models on test set
   - Generate visualizations and comparison results

## Results

- **LeNet-5**: Expected accuracy ~92-95%
- **Custom CNN**: Expected accuracy ~94-97%

Both models should achieve >90% accuracy as required.

## File Structure

- `src/data_loader.py`: Data loading and preprocessing
- `src/models.py`: Model definitions (LeNet-5, Custom CNN)
- `src/train.py`: Training pipeline
- `src/evaluate.py`: Evaluation metrics
- `src/utils.py`: Utility functions
- `main.py`: Main execution script
- `results/`: Saved models, plots, and metrics