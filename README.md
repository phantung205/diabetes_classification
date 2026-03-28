#  Diabetes Prediction Web App (Machine Learning Classification)

Ứng dụng web dự đoán bệnh **Tiểu đường** sử dụng Machine Learning và Flask.  
Hỗ trợ dự đoán **1 mẫu** hoặc **nhiều mẫu qua file CSV / Excel**.

---

## 1. chức năng
- Dự đoán tiểu đường
- Hỗ trợ nhiều model:
  - Logistic Regression
  - Random Forest
  - SVM
  - XGBoost
- Upload file CSV / Excel
- Hiển thị xác suất dự đoán

---

## 2. Yêu cầu
- Python >= 3.8
- pip

---

## 3. Cấu trúc thư mục

```text
disease_nckh/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   ├── raw/
│   │   └── diabetes.csv
│   └── processed/
├── model/
├── reports/
├── src/
├── templates/
├── static/
└── uploads/
```

---

## 4 Dataset

### 4.1 Tải dữ liệu

- Kaggle (khuyên dùng):  
  https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

---

### 4.2 Cách dùng dữ liệu

1. Tải file `diabetes.csv`
2. Đặt vào thư mục:
```text
data/raw/diabetes.csv
```

---

### 4.3 Cột dữ liệu bắt buộc

| Column |
|------|
| Pregnancies |
| Glucose |
| BloodPressure |
| SkinThickness |
| Insulin |
| BMI |
| DiabetesPedigreeFunction |
| Age |
| Outcome |

---

## 5. Cài đặt

### 5.1 Tạo môi trường ảo (khuyên dùng)

```bash
python -m venv venv
```

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

---

### 5.2 Cài thư viện

```bash
pip install -r requirements.txt
```

Kiểm tra:
```bash
python -c "import flask, pandas, sklearn, joblib; print('OK')"
```

---

## 6. chỉnh cấu hình tham số mặc định
```text
config.py
```

---

## 7 Train model **(BẮT BUỘC)**

### 7.1 chạy các lệnh sau

```bash
# Logistic Regression
python -m src.train --model_name logistic

# Random Forest
python -m src.train --model_name random_forest

# SVM
python -m src.train --model_name svm

# XgBoost
python -m src.train --model_name xgboost
```

### 7.2 Model sau khi train sẽ nằm trong:
```text
model/*.pkl
```

---


## 8. Đánh giá mô hình

### metric đánh giá
- Accuracy
- Precision
- Recall (class 1)
- F1-score
- ROC-AUC

### Insight
- Recall cao giúp giảm thiểu việc bỏ sót các trường hợp mắc bệnh tiểu đường  
- Phù hợp cho các bài toán sàng lọc y tế  

---

## 9. Báo cáo

- EDA:
```
reports/edu/report_diabetes.html
```

- Kết quả huấn luyện:
```
reports/results/
```

---

## 👤 Tác giả

Phan Tùng  
GitHub: https://github.com/phantung205
