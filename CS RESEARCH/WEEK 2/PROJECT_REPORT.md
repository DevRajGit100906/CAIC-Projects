# 📊 Project Report – CS Research Week 2 (CAIC Summer of Tech 2025)

**Author:** Dev Raj Das  
**Track:** CS Research  
**Week:** 2  
**Dates:** June 2025  
**Original Task Repo:** [devclub-iitd/CAIC_Summer_Of_Tech_25](https://github.com/devclub-iitd/CAIC_Summer_Of_Tech_25/tree/main/CS_Research_ARIES_X_ACES_ACM/Week-2)

---

## ✅ Objective

The goal of Week 2 was to explore **basic data handling and visualization techniques using Pandas, NumPy, and Matplotlib**. The objective was to:

- Analyze structured datasets (like Fashion-MNIST CSVs)
- Perform preprocessing and exploratory data analysis
- Use plotting libraries to visualize distributions and relationships
- Build foundational skills for future deep learning projects

---

## 📁 Submitted Files

📂 [Week 2 Folder](https://github.com/DevRajGit100906/CAIC-Projects/tree/main/CS%20RESEARCH/WEEK%202)

| File | Description |
|------|-------------|
| `WEEK2_CSRESEARCH.ipynb` | Main Jupyter notebook with code and outputs |
| `WEEK2_CSRESEARCH.pdf`   | Exported notebook as PDF |
| `FASHIONMNIST/*.csv`     | Raw data files (train/test datasets) |

---

## 📌 Task Breakdown & My Approach

### 🔹 1. Dataset Loading & Cleaning
- Used Pandas to load `fashion-mnist_train.csv` and `fashion-mnist_test.csv`
- Checked for null values, duplicated rows, and data types
- Normalized pixel values from `[0, 255]` to `[0, 1]`

### 🔹 2. Exploratory Data Analysis (EDA)
- Computed label distributions using `value_counts()`
- Visualized label frequencies with **bar plots**
- Displayed sample images using `matplotlib.pyplot.imshow()`
- Calculated pixel intensity histograms and means

### 🔹 3. NumPy Operations
- Performed matrix manipulations and reshaping
- Applied `np.mean()`, `np.std()`, and filtering logic
- Converted DataFrames to NumPy arrays and back for vectorized processing

### 🔹 4. Plotting & Visualization
- Used **Matplotlib** to:
  - Plot sample clothing images from Fashion-MNIST
  - Compare class distributions
  - Visualize pixel intensity spread and class-wise variations

---

## 📊 Results & Learnings

- **Learned to handle image data in tabular format**
- **Understood how to clean and normalize datasets**
- **Practiced transforming and analyzing structured data using Pandas and NumPy**
- **Built confidence with basic visualizations and statistical analysis**

---

## 🧠 Concepts Reinforced

- Data preprocessing for machine learning
- Vectorized operations with NumPy
- Visual storytelling with plots
- Image dataset representation in CSV/tabular format

---

## 📈 Sample Output Visuals

- Label frequency distribution bar plot
- Grayscale rendering of Fashion-MNIST samples
- Mean image matrix per class (using NumPy averaging)
- Pixel intensity histograms

---

## 📌 Tools Used

- Python 3.11  
- Jupyter Notebook  
- Pandas, NumPy  
- Matplotlib  
- Git & GitHub for version control

---

## 🔚 Conclusion

This week served as a bridge between raw data and model-ready data. I built a solid foundation in data wrangling and visualization, which will directly support model training in Week 3.

---

## 🔗 Links

- 📂 My Submission: [GitHub Repo – Week 2](https://github.com/DevRajGit100906/CAIC-Projects/tree/main/CS%20RESEARCH/WEEK%202)
- 📝 Official Task: [DevClub Week 2](https://github.com/devclub-iitd/CAIC_Summer_Of_Tech_25/tree/main/CS_Research_ARIES_X_ACES_ACM/Week-2)
- 📊 Fashion-MNIST Dataset: [Zalando GitHub](https://github.com/zalandoresearch/fashion-mnist)

---
