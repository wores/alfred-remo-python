import inspect


def create_instance_func_dict(clss_name):
    func_dict = {}
    for func_name, func in inspect.getmembers(clss_name(), inspect.ismethod):
        func_dict[func_name] = func
    return func_dict
