from importlib.resources import files


def read_template(file_name: str):
    '''读取当前包内 templates/file_name 对应的资源（返回字符串）'''
    return files(__name__).joinpath('templates', file_name).read_text(encoding="utf-8") 
