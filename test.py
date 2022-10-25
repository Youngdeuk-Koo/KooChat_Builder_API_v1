import os
path = '/mnt/c/Users/kooli/mrmind/1_development_project/chatbot/v.1.0.0_2022_10_20/koochat_builder_v1'
print(os.path.join(path, os.listdir(path)[-1]), type(os.path.join(path, os.listdir(path)[-1])))
