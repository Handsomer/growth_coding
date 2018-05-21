from  contextlib import contextmanager

'''
    contextlib : 上下文管理模块
'''
@contextmanager
def make_open_context(filename,mode):
    fp = open(filename, mode)
    try:
        yield fp
    finally:
        fp.close()

