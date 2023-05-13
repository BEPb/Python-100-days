"""
Python 3.9 программа преобразования-генерации в файл submission.py (в рамках соревнования kaggle ConnectX)
программа на Python по изучению обучения с подкреплением - Reinforcement Learning
Название файла gen_submission.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-12-22
"""
import sys
import base64
import inspect
import os

assert len(sys.argv) == 2, "please specify model path."
model_path = sys.argv[1]

with open(model_path, 'rb') as f:
    raw_bytes = f.read()
    encoded_weights = base64.encodebytes(raw_bytes)

# encode weights of model to byte string
submission_file = """
import base64
decoded = base64.b64decode({})

""".format(encoded_weights)

# insert code snippet of loading weights
# with open('submission_template.py', 'r') as f:
with open('/home/user/PycharmProjects/Python-100-days/Game_AI_and_Reinforcement_Learning/ConnectX/v2/submission_template.py', 'r') as f:
    submission_file += ''.join(f.readlines())

# generate final submission file
with open('submission.py', 'w') as f:
    f.write(submission_file)
