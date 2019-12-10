import json
import os
import shutil


def empty_summaries_folder():
    folder = './summaries'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)


def save_to_json(urls, path):
    file_name = "summaries/bbc_"+"_".join(path.split("/")) + ".json"
    with open(file_name, 'w') as outfile:
        json.dump(urls, outfile, indent=2)
