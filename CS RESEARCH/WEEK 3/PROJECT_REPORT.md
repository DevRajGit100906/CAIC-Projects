# Week 3 Project Report: CNNs on Fashion-MNIST

**Course:** CS Research – Summer of Tech 2025

**Conducted By:** ARIES x ACES x ACM

**Date:** July 15, 2025

**Author:** Dev Raj Das

---

## 🧾 Objective

To design, train, and evaluate Convolutional Neural Networks (CNNs) for image classification on the Fashion-MNIST dataset. The goal was to implement two popular deep learning architectures: **AlexNet** (in TensorFlow) and **ResNet** (in PyTorch), and compare their performance.

---

## 🔧 Tools & Technologies

* **TensorFlow/Keras** – for AlexNet

* **PyTorch** – for ResNet

* **Pandas, NumPy** – data manipulation

* **Matplotlib** – plotting training curves

* **scikit-learn** – for train-validation split

---

## 📦 Dataset Description

**Fashion-MNIST**:

* 70,000 grayscale 28x28 images of fashion items

* 10 categories (num_classes = 10)

* Split into 60,000 training and 10,000 testing images

* Preprocessing involved normalisation (pixel values from 0-255 to 0.0-1.0) and reshaping to (28, 28, 1)

* Split into training, validation, and test sets (54,000 training, 6,000 validation, 10,000 testing images)

---

## 📐 Model Architectures

### 1. **AlexNet (TensorFlow)**

* 5 convolutional layers with ReLU and max pooling

* Fully connected layers with dropout

* Optimiser: Adam

* Loss: Sparse Categorical Crossentropy

* Epochs: 20

* Test Accuracy: **91.39%**

### 2. **ResNet (PyTorch)**

* 3 residual blocks using `BasicBlock` (layers=\[2,2,2\])

* Adaptive average pooling + fully connected layer

* Optimiser: Adam (learning rate=0.001)

* Loss: CrossEntropyLoss

* Epochs: 20

* Test Accuracy: **92.87%**

---

## 📈 Results Summary

| **Metric** | **AlexNet** | **ResNet** |
|---|---|---|
| Final Accuracy | 91.39% | **92.87%** |
| Loss Curve | Converged | Smooth, faster |
| Training Time | Moderate | Efficient (CPU) |

---

## 🔍 Analysis

* ResNet performed better due to its residual connections, which help gradient flow during backpropagation, contributing to better performance and generalisation.

* AlexNet showed signs of overfitting after approximately 10-12 epochs, where training accuracy continued to increase significantly while validation accuracy plateaued or slightly decreased.

* ResNet generalised better on the validation and test sets, maintaining a closer gap between training and validation accuracy/loss throughout the training process.

---

## 📚 Learnings

* Model depth should be balanced with regularisation to prevent overfitting (e.g., dropout layers in AlexNet, residual connections in ResNet).

* The choice of framework (TensorFlow/Keras vs. PyTorch) influences implementation style, with Keras offering a higher-level abstraction and PyTorch providing more control.

* Visualising training progress (accuracy and loss curves) is crucial for identifying overfitting and understanding model behaviour over epochs.

---

## ✅ Conclusion

Both CNN architectures achieved strong results on the Fashion-MNIST dataset. ResNet demonstrated superior accuracy and generalisation, validating the efficacy of residual connections in deep learning models, especially for deeper networks.

---

## 🔗 References

* Fashion-MNIST Dataset: <https://github.com/zalandoresearch/fashion-mnist>

* PyTorch Docs: <https://pytorch.org/docs/stable/index.html>

* TensorFlow Docs: <https://www.tensorflow.org/api_docs>
'''
