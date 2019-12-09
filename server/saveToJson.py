import json
import os
import shutil

def to_file(target_location, text, debug=False):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    savefile = os.path.join(THIS_FOLDER, "summaries", target_location)

    if(debug):
        print(savefile)
        print(text)

    with open(savefile, "w") as file:
        json.dump(text, file, indent=2)

def empty_summaries_folder():
    folder = './summaries'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

def save_urls_to_json(url_list, path):
    file_name = "summaries/bbc_"+"_".join(path.split("/")) + ".json"
    with open(file_name, 'w') as outfile:
        json.dump(url_list, outfile, indent=2)
