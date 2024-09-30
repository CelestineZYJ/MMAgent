from papermage.recipes import CoreRecipe
import json
import os
from pathlib import Path

source_path = "/shared/nas2/jt/BriesMM/data/"
target_path = "/shared/nas2/jt/BriesMM/parsedData/"

def list_directories(path):
    files = []
    with os.scandir(path) as entries:
        # Filter out only directories and print them
        for entry in entries:
            if entry.is_dir():
                files.append(str(entry.name))
    return files

recipe = CoreRecipe()
files = list_directories(source_path)
for papername in files:
    path_str = source_path+papername+"/pdf/"+papername+".pdf"
    # path_str = "/shared/nas2/jt/BriesMM/third_party/papermage/tests/fixtures/papermage.pdf"
    path_obj = Path(path_str)
    doc = recipe.run(path_obj)
    with open(target_path+papername+'.json', 'w') as f_out:
        json.dump(doc.to_json(), f_out, indent=4)
