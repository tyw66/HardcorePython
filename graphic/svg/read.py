from importlib.resources import files


def read_template(file_name: str):
    '''读取当前包内 file_path 对应的资源（返回字符串'''
    return files(__name__).joinpath(file_name).read_text(encoding="utf-8")
    
    #读取当前模块包内templates/file_name文件的内容并解码为字符串 (找不到pkg_resources)
    # file_path = path.join('templates', file_name)
    # byte_str = pkg_resources .resource_string(__name__, file_path)
    # return byte_str.decode('utf-8') 

