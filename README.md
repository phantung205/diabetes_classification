# 🩺 Diabetes Prediction Web App (Flask + Machine Learning)

Ứng dụng web dự đoán bệnh **Tiểu đường** sử dụng Machine Learning và Flask.  
Hỗ trợ dự đoán **1 mẫu** hoặc **nhiều mẫu qua file CSV / Excel**.

---

## 🚀 Chức năng
- Dự đoán tiểu đường
- Hỗ trợ nhiều model:
  - Logistic Regression
  - Random Forest
  - SVM
- Upload file CSV / Excel
- Hiển thị xác suất dự đoán

---

## 🖥️ Yêu cầu
- Python >= 3.8
- pip

---

## 📂 Cấu trúc thư mục

```text
disease_nckh/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   ├── raw/
│   └── processed/
├── model/
├── reports/
├── src/
├── templates/
├── static/
└── uploads/
```

---

## ⚙️ Cài đặt

### 1️⃣ Tạo môi trường ảo (khuyên dùng)

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

### 2️⃣ Cài thư viện

```bash
pip install -r requirements.txt
```

Kiểm tra:
```bash
python -c "import flask, pandas, sklearn, joblib; print('OK')"
```

---

## 📊 Dataset

### 🔗 Tải dữ liệu

- Kaggle (khuyên dùng):  
  https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

- UCI Repository:  
  https://archive.ics.uci.edu/ml/datasets/diabetes

---

### 📥 Cách dùng dữ liệu

1. Tải file `diabetes.csv`
2. Đặt vào thư mục:
```text
data/raw/diabetes.csv
```

---

### 📌 Cột dữ liệu bắt buộc

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

## 🧠 Train model (BẮT BUỘC)

```bash
# Logistic Regression
python src/train.py --model_name logistic

# Random Forest
python src/train.py --model_name random_forest

# SVM
python src/train.py --model_name svm
```

📌 Model sau khi train sẽ nằm trong:
```text
model/*.pkl
```

---

## 🚀 Chạy Flask App

```bash
python app.py
```

Mở trình duyệt:
```text
http://127.0.0.1:5000
```

---

## 🧪 Ví dụ input dự đoán

```json
{
  "Pregnancies": 6,
  "Glucose": 148,
  "BloodPressure": 72,
  "SkinThickness": 35,
  "Insulin": 0,
  "BMI": 33.6,
  "DiabetesPedigreeFunction": 0.627,
  "Age": 50
}
```

---

## 🔁 Dùng dữ liệu mới để train

1. Đặt file CSV mới vào:
```text
data/raw/
```

2. Đảm bảo cột giống dataset gốc

3. Train lại model:
```bash
python src/train.py --model_name logistic
```

---

## ❗ Lỗi thường gặp

- ❌ Không chạy được app → **chưa train model**
- ❌ Lỗi thư viện → chạy lại:
```bash
pip install -r requirements.txt
```

---

## ⚠️ Lưu ý
- Chỉ dùng cho học tập / nghiên cứu
- Không thay thế chẩn đoán y tế
