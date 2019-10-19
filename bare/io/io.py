import os
import xmltodict
import json

def create_dir(directory):
    if directory == None:
        return None
    
    else:
        if not os.path.exists(directory):
            os.makedirs(directory)
        return os.path.abspath(directory)

def xml_to_json(xml_file_name):
    with open(xml_file_name, 'r') as f:
        xml_as_json = json.loads(json.dumps(xmltodict.parse(f.read())))
        
    return xml_as_json
    
def split_file(file_path_and_name):
    file_path = os.path.split(file_path_and_name)[0]
    file_name = os.path.splitext(os.path.split(file_path_and_name)[-1])[0]
    file_extension = os.path.splitext(os.path.split(file_path_and_name)[-1])[-1]
    
    return file_path, file_name, file_extension


def rename_file(source_file_name, 
                pattern=None,
                new_pattern=None,
                destination_file_path=None,
                destination_file_extension=None):
    
    file_path, file_name, file_extention = split_file(source_file_name)
    
    if pattern:
        if new_pattern==None:
            new_pattern=''
        
        file_name = file_name.replace(pattern, new_pattern)
        
    if destination_file_path:
        create_dir(destination_file_path)
        file_path = destination_file_path
        
    if destination_file_extension:
        file_extention = destination_file_extension
            
    destination_file_name = os.path.join(file_path, file_name+file_extention)
    return destination_file_name

def batch_rename_files(source_file_path,
                       file_extension=None,
                       pattern=None,
                       new_pattern=None,
                       destination_file_path=None,
                       destination_file_extension=None):
    
    var_list = [file_extension, pattern, new_pattern, destination_file_path, destination_file_extension]
    if all(isinstance(x, type(None)) for x in var_list):
        print("No options provided. Source and destination files identical.")
    
    else:
        if file_extension:
            files = glob.glob(os.path.join(source_file_path,'**','*'+ file_extension), recursive=True)
        else:
            files = glob.glob(os.path.join(source_file_path,'**','*'), recursive=True)

        for source_file_name in files:

            new_file = rename_file(source_file_name, 
                                   pattern=pattern,
                                   new_pattern=new_pattern,
                                   destination_file_path=destination_file_path,
                                   destination_file_extension=destination_file_extension)

            if source_file_name != new_file:
                shutil.copy2(source_file_name,new_file)