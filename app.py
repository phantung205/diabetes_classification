from flask import Flask,render_template,request
from src import inference
import os
from src import config
from datetime import datetime
from flask import send_file

# tạo hai thư mục lưu file người dùng upload và kết quả dự đoán
upload = config.upload_folder
result = config.result_folder
os.makedirs(upload, exist_ok=True)
os.makedirs(result, exist_ok=True)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html" ,data=None,error=None,prediction=None,proba_dict=None,selected_model="logistic",output_save=None)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # lấy tên model
        model_name = request.form["model_name"]

        # lấy dữ liệu người dùng nhập vào
        data = {
            "Pregnancies": int(request.form["Pregnancies"]),
            "Glucose": float(request.form["Glucose"]),
            "BloodPressure": float(request.form["BloodPressure"]),
            "SkinThickness": float(request.form["SkinThickness"]),
            "Insulin": float(request.form["Insulin"]),
            "BMI": float(request.form["BMI"]),
            "DiabetesPedigreeFunction": float(request.form["DiabetesPedigreeFunction"]),
            "Age": int(request.form["Age"])
        }
        # validation dữ liệu
        validation(data)

        # dự đoán
        prediction, proba_dict = inference.model_from_dic(data,model_name)

        return render_template("index.html",data=data,prediction=prediction,proba_dict=proba_dict,selected_model=model_name,error=None,output_save=None)

    except Exception as e:
        model_name =request.form.get("model_name","logistic")
        return render_template("index.html",data=request.form,error=str(e),prediction=None,proba_dict=None,selected_model=model_name,output_save=None)

@app.route("/predict_file", methods=["POST"])
def predict_file():
    try:
        # lấy tên model
        model_name = request.form["model_name"]

        # lấy ra tên file upload
        file = request.files["file"]
        filename = file.filename

        # check xem đã chọn file chưa
        if file.filename == "":
            raise ValueError("Chưa chọn file")

        # check đuôi đúng định dạng chưa
        ext = os.path.splitext(filename)[1].lower()
        allowed_ext = {".csv",".xlsx",".xls"}
        if ext not in allowed_ext:
            raise ValueError("Chỉ hỗ trợ file CSV hoặc Excel")

        #lưu file người dùng upload
        name, ext = os.path.splitext(filename)
        timestamp = datetime.now().strftime("%S_%M_%H_%d_%m_%Y")
        new_filename = f"{name}_{timestamp}{ext}"
        input_path = os.path.join(upload,new_filename)
        file.save(input_path)

        # lưu file kết quả
        output_filename = f"{name}_prediction_{timestamp}.csv"
        # dự đoán
        df_result = inference.model_from_file(input_path,model_name)
        output_path =  os.path.join(result,output_filename)
        df_result.to_csv(output_path,index=False)

        return render_template("index.html",data=None,error=None,prediction=None,proba_dict=None,selected_model=model_name,output_save=output_filename)
    except Exception  as e:
        model_name = request.form.get("model_name", "logistic")
        return render_template("index.html", data=None, error=str(e), prediction=None, proba_dict=None,selected_model=model_name,output_save=None)

@app.route("/download/<filename>")
def download_file(filename):
    file_path = os.path.join(result, filename)
    return send_file(
        file_path,
        as_attachment=True
    )

def validation(data):
    if data["Age"] <= 0:
        raise ValueError("Tuổi phải lớn hơn 0")
    if data["BMI"] <= 0:
        raise ValueError("BMI phải lớn hơn 0")
    if data["Glucose"] <= 0:
        raise ValueError("Glucose phải lớn hơn 0")
    if data["Pregnancies"] < 0:
        raise ValueError("Pregnancies phải lớn hơn 0")
    if data["BloodPressure"] <= 0:
        raise ValueError("BloodPressure phải lớn hơn 0")
    if data["SkinThickness"] <= 0:
        raise ValueError("SkinThickness phải lớn hơn 0")
    if data["DiabetesPedigreeFunction"] < 0:
        raise ValueError("DiabetesPedigreeFunction phải lớn hơn 0")
    if data["Insulin"] <= 0:
        raise ValueError("Insulin phải lớn hơn 0")


if __name__ == '__main__':
    app.run(debug=True)