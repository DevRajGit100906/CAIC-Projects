# PROJECT\_REPORT.md

## 📘 Week 1 Project Report: CS Research Track

This report presents the work done for **Week 1** of the CS\_Research\_ARIES\_X\_ACES\_ACM project. The main objectives included implementing core numerical algorithms from scratch using only `NumPy` and `Pandas`, focusing on understanding optimization and root-finding fundamentals.

---

## 📑 Table of Contents

* Objectives
* Deliverables
* Linear Regression with L1 Regularization
* Newton-Raphson Method for Root Finding
* Key Code Snippets
* Conclusion

---

## 🎯 Objectives

* 🧮 Implement a **custom Linear Regression algorithm** using gradient descent and L1 regularization (Lasso).
* 🔁 Build a **recursive implementation of Newton-Raphson method** to compute the mth root of a number.
* 🧪 Use only fundamental libraries: `NumPy`, `Pandas`
* 💡 Focus on numerical stability and interpretability

---

## 📂 Deliverables

* ✅ Python implementation: `week1_csresearch.py`
* ✅ Jupyter notebook: `WEEK1_CSRESEARCH.ipynb`
* ✅ Both functions written from scratch without `sklearn` or high-level packages

---

## 📉 Linear Regression with L1 Regularization

### 🔍 Function Signature

```python
def linearRegression(X: np.array, Y: np.array, lr: float, lambda_: float):
```

### 🧠 Approach

* Initialized weights and bias to zeros
* Applied **gradient descent** over 1000 epochs
* Used **L1 penalty** (`lambda_ * sign(weights)`) to promote sparsity

### 📐 Equation Used

ŷ = Xw + b
Loss = MSE + λ‖w‖₁

### ⚙️ Gradient Updates

```python
weights_grad = (1/m) * np.dot(X.T, error) + (lambda_/m) * np.sign(weights)
bias_grad = (1/m) * np.sum(error)
```

---

## 📏 Newton-Raphson Method

### 🧮 Functionality

Computes the **mth root of a number `x`** using recursive Newton-Raphson updates.

### 🔍 Function Signature

```python
def newtonRaphson(x: float, m: float):
```

### 🔄 Recursive Implementation

```python
def find_root_recursive(current_root, tolerance=1e-7, max_iterations=100):
    if abs(current_root**m - x) < tolerance or max_iterations == 0:
        return current_root
    else:
        next_root = current_root - (current_root**m - x) / (m * current_root**(m-1))
        return find_root_recursive(next_root, tolerance, max_iterations - 1)
```

### 📌 Example

* For `x = 27` and `m = 3`, the function accurately computes the cube root ≈ 3.0

---

## 💻 Key Code Snippets

### Linear Regression with L1 Regularization

```python
weights = np.zeros(n)
bias = 0.0
for epoch in range(epochs):
    y_pred = np.dot(X, weights) + bias
    error = y_pred - y_train
    weights_grad = (1/m) * np.dot(X.T, error) + (lambda_/m) * np.sign(weights)
    bias_grad = (1/m) * np.sum(error)
    weights -= lr * weights_grad
    bias -= lr * bias_grad
```

### Newton-Raphson (Recursive)

```python
def newtonRaphson(x: float, m: float):
    root = x / m
    def find_root_recursive(current_root, tolerance=1e-7, max_iterations=100):
        if abs(current_root**m - x) < tolerance or max_iterations == 0:
            return current_root
        else:
            next_root = current_root - (current_root**m - x) / (m * current_root**(m-1))
            return find_root_recursive(next_root, tolerance, max_iterations - 1)
    return find_root_recursive(root)
```

---

## ✅ Conclusion

* 🚀 Successfully implemented linear regression with L1 regularization using raw NumPy
* 🧠 Recursively implemented Newton-Raphson for root-finding with good convergence
* 📉 Emphasis was on code clarity, numerical stability, and correct mathematical derivation
* 🔧 Set the stage for optimization-heavy projects and advanced research tasks in coming weeks

---
