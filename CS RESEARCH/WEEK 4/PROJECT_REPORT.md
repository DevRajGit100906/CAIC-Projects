# Project Report: Brain Tumor Detection with CNN 🧠

This report details the implementation of a Convolutional Neural Network (CNN) to classify MRI scans for the presence of brain tumors. This project was completed as part of the CSoT'25 Week 4 CS Research program.

---

## 1. Introduction 🎯

[cite_start]The primary objective of this project was to develop a deep learning model capable of accurately identifying whether a person has a brain tumor based on their MRI scan[cite: 4]. [cite_start]The project involved implementing a CNN using TensorFlow and Keras, processing a raw image dataset, training the model, and finally, evaluating its performance and visualizing the results[cite: 5].

---

## 2. Dataset 📁

The project utilized the **Brain MRI Dataset for Detection and Analysis** from Kaggle.

-   **Content**: The dataset consists of MRI scans organized into two categories: `yes` (containing a tumor) and `no` (without a tumor).
-   [cite_start]**Link**: [https://www.kaggle.com/datasets/sudipde25/mri-dataset-for-detection-and-analysis/data](https://www.kaggle.com/datasets/sudipde25/mri-dataset-for-detection-and-analysis/data) [cite: 6]

---

## 3. Methodology ⚙️

### 3.1. Data Preprocessing

[cite_start]The raw image data was preprocessed to be suitable for training the CNN model[cite: 21]:

-   [cite_start]🖼️ **Image Resizing**: All images were resized to a uniform dimension of $150 \times 150$ pixels[cite: 22, 24].
-   [cite_start]⚖️ **Normalization**: Pixel values were normalized to a range of $[0, 1]$ by dividing each pixel by 255.0[cite: 22, 28, 41]. This helps in faster and more stable training.
-   [cite_start]✂️ **Data Splitting**: The dataset was split into a training set (80%) and a validation set (20%)[cite: 23, 25]. [cite_start]This resulted in 4200 training images and 1049 validation images[cite: 70].
-   ✨ **Data Augmentation**: To prevent overfitting and improve the model's ability to generalize, data augmentation techniques were applied to the training set. [cite_start]These included random rotations, shifts, shears, zooms, and horizontal flips[cite: 30, 31, 32, 33, 34, 35, 36].

### 3.2. Model Architecture 🏗️

[cite_start]A sequential CNN model was constructed using TensorFlow/Keras[cite: 5, 80]. [cite_start]The architecture was designed for binary image classification with the following layers [cite: 78-101]:

| Layer Type             | Output Shape            | Parameters | Details                                                                 |
| ---------------------- | ----------------------- | ---------- | ----------------------------------------------------------------------- |
| `Conv2D`               | (None, 148, 148, 32)    | 320        | 32 filters, (3,3) kernel, ReLU activation, input shape (150,150,1)       |
| `BatchNormalization`   | (None, 148, 148, 32)    | 128        | Normalizes the activations of the previous layer                        |
| `MaxPooling2D`         | (None, 74, 74, 32)      | 0          | (2,2) pool size                                                         |
| `Dropout`              | (None, 74, 74, 32)      | 0          | 25% dropout rate                                                        |
| `Conv2D`               | (None, 72, 72, 64)      | 18,496     | 64 filters, (3,3) kernel, ReLU activation                               |
| `BatchNormalization`   | (None, 72, 72, 64)      | 256        |                                                                         |
| `MaxPooling2D`         | (None, 36, 36, 64)      | 0          | (2,2) pool size                                                         |
| `Dropout`              | (None, 36, 36, 64)      | 0          | 25% dropout rate                                                        |
| `Conv2D`               | (None, 34, 34, 128)     | 73,856     | 128 filters, (3,3) kernel, ReLU activation                              |
| `BatchNormalization`   | (None, 34, 34, 128)     | 512        |                                                                         |
| `MaxPooling2D`         | (None, 17, 17, 128)     | 0          | (2,2) pool size                                                         |
| `Dropout`              | (None, 17, 17, 128)     | 0          | 25% dropout rate                                                        |
| `Flatten`              | (None, 36992)           | 0          | Flattens the input for the dense layers                                 |
| `Dense`                | (None, 256)             | 9,470,208  | 256 units, ReLU activation                                              |
| `Dropout`              | (None, 256)             | 0          | 50% dropout rate                                                        |
| `Dense` (Output)       | (None, 1)               | 257        | 1 unit, Sigmoid activation for binary classification                    |

[cite_start]The model was compiled with the **Adam optimizer**, using **binary cross-entropy** as the loss function and **accuracy** as the evaluation metric[cite: 74, 98, 99, 100].

### 3.3. Model Training 🚀

[cite_start]The model was trained for a maximum of 20 epochs[cite: 198]. [cite_start]An `EarlyStopping` callback was used to monitor the validation loss (`val_loss`)[cite: 192, 195]. [cite_start]This callback stopped the training if the validation loss did not improve for 3 consecutive epochs (`patience=3`) and restored the weights from the best-performing epoch[cite: 196, 197]. [cite_start]Training was halted after 12 epochs as the model's performance on the validation set had converged [cite: 223-299].

---

## 4. Evaluation and Results 📊

[cite_start]The model was evaluated on the validation dataset, which served as the test set for the final performance assessment[cite: 301, 305].

### 4.1. Performance Score ✅

-   [cite_start]**Final Test Accuracy**: **87.70%** [cite: 308]
-   [cite_start]**Final Test Loss**: **0.3804** [cite: 310]

### 4.2. Performance Curves 📈

[cite_start]The accuracy and loss curves for both training and validation sets were plotted to visualize the model's learning progress[cite: 302].

-   **Training and Validation Accuracy**: The training accuracy quickly reached ~88% and remained stable. The validation accuracy, after some initial fluctuation, also converged to approximately 87.7%, closely following the training accuracy. [cite_start]This indicates that the model was not significantly overfitting[cite: 334].

    <img width="1156" height="470" alt="image" src="https://github.com/user-attachments/assets/5c3a58fd-d0a5-4a35-9c33-00767f20aa3c" />


-   **Training and Validation Loss**: Both training and validation losses saw a sharp decrease after the first epoch. [cite_start]The validation loss reached its minimum value of 0.3804 at epoch 9, triggering the early stopping mechanism after 3 more epochs of no improvement[cite: 278, 337].

    <img width="1143" height="470" alt="image" src="https://github.com/user-attachments/assets/e28891a0-8850-43ee-8dff-703b058af6a9" />


---

## 5. Conclusion ✨

This project successfully demonstrated the use of a Convolutional Neural Network to build an effective brain tumor detection model. By preprocessing the MRI scan dataset and building a well-structured CNN, the model achieved a final accuracy of **87.70%**. The use of data augmentation, Batch Normalization, and Dropout layers helped in creating a robust model that generalizes well, as evidenced by the closely aligned training and validation curves. [cite_start]The modular code structure, organized into classes for model building, training, and testing, ensures the project is both readable and reusable[cite: 76].
