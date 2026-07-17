import os

from src import config


def get_report_names():

    reports = {}

    for file in os.listdir(config.dir_result):
        if file.endswith(".txt"):
            path = os.path.join(config.dir_result,file)

            with open(path,"r",encoding="utf-8") as f:
                reports[file] = f.read()

    return reports
