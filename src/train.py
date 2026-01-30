import os.path
import joblib
from charset_normalizer.md import CjkUncommonPlugin
from sklearn.compose import  ColumnTransformer
from src import preprocessing, config
import argparse
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OrdinalEncoder,OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report,roc_auc_score


def parse_args():
    p = argparse.ArgumentParser(description="Train a classification model for diabetes")
    # argument test size and random state
    p.add_argument("--random_state","-r",type=int,default=42, help="random state")
    p.add_argument("--test_size","-t",type=float,default=0.2,help="test size")
    # name model
    p.add_argument("--model_name","-m",type=str,default="random_forest", help="choice model")
    # argument randomforest
    p.add_argument("--n_estimators","-n",type=int,default=200 , help="n_estimators")
    p.add_argument("--criterion","-rf_c",type=str,default="gini" , help="criterion")
    # argument  LogisticRegression
    p.add_argument("--c_logis","-c",type=float,default=0.1,help="c in logisticregresstion")
    p.add_argument("--max_iter","-i",type=int,default=1000,help="max_iter in logisticregresstion")
    # argument svm
    p.add_argument("--kernel","-k",type=str,default="rbf", help="kernel svm")

    return p.parse_args()

def build_model(args):
    if args.model_name == "random_forest":
        clf = RandomForestClassifier(
            n_estimators=args.n_estimators,
            criterion= args.criterion,
            random_state=args.random_state,
            class_weight="balanced"
        )
    elif args.model_name == "logistic":
        clf = LogisticRegression(
            C=args.c_logis,
            penalty="l2",
            solver="lbfgs",
            class_weight="balanced",
            max_iter=args.max_iter
        )
    elif args.model_name == "svm":
        clf = SVC(
            kernel=args.kernel,
            C=1,
            gamma="scale",
            class_weight="balanced",
            probability=True
        )
    else:
        raise ValueError(
            f"Model '{args.model_name}' is not supported. "
            "Choose from: random_forest, logistic, svm"
        )
    return clf

def main(args):
    # lấy ra dữ liệu đã chia
    x_train, x_test, y_train, y_test = preprocessing.preprocess_and_split(args.test_size,args.random_state)

    # tạo pipeline chuẩn hóa
    num_transformer = Pipeline(steps=[
        ("imputer",SimpleImputer(strategy="median")),
        ("scaler",StandardScaler())
    ])

    # thực hiện chuẩn hóa
    preprocessor = ColumnTransformer(transformers=[
        ("num_feature",num_transformer,config.numerical_col)
    ])

    # tạo model pipline
    clf = build_model(args)
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("clf", clf),
    ])

    # fit dữ liệu vào
    pipeline.fit(x_train, y_train)

    # test model
    y_predict = pipeline.predict(x_test)
    y_proba = pipeline.predict_proba(x_test)[:, 1]
    roc_auc = roc_auc_score(y_test, y_proba)
    # print result
    print(classification_report(y_test, y_predict))
    print(f"ROC-AUC: {roc_auc:.4f}")

    # lưu model kết quả đánh giá lại
    if not os.path.isdir(config.dir_result):
        os.makedirs(config.dir_result)
    path_result = os.path.join(config.dir_result,f"train_report_{args.model_name}.txt")
    with open(path_result,"w") as f:
        f.write(classification_report(y_test, y_predict))
        f.write(f"\nROC-AUC: {roc_auc:.4f}\n")

    # lưu model
    if not os.path.isdir(config.dir_model):
        os.makedirs(config.dir_model)
    model_file = f"{args.model_name}.pkl"
    model_path = os.path.join(config.dir_model,model_file)
    joblib.dump(pipeline, model_path)
    print("save model successfull")


if __name__ == '__main__':
    args = parse_args()
    main(args)


