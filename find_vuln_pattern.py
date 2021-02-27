# coding:utf-8
"""
脚本功能：提取出Python代码中所有的字符串常量，调用工具判断正则表达式是否存在漏洞，打印漏洞信息
"""
import os
import re
import subprocess
from util import find_python_str


scan_bin = "./scan.bin"
# pattern_1 = re.compile(r"VULNERABLE:\s*(\d+)")
pattern_1 = re.compile(r"Kleene")
record_list = []


class Token(object):
    def __init__(self, value, filename):
        self.value = value
        self.filename = filename


def is_vuln_str(input_str):
    """
    :return:
    """
    # 太长的字符串
    if len(input_str) >= 200:
        return False

    # 重复检测
    if input_str in record_list:
        return False
    else:
        record_list.append(input_str)

    # 白名单文件

    # 根据历史排查形成的经验，白名单
    if "**" in input_str:
        return False

    input_str += "\n"  # 换行很重要，scan_bin需要

    try:
        input_str = input_str.encode()
    except Exception as _:
        return False

    p = subprocess.Popen(scan_bin, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    content = p.communicate(input=input_str)[0]
    # print(content)
    vuln = re.findall(pattern_1, content.decode())
    if len(vuln) > 0 and vuln[0] != '0':
        # print(input_str)
        return True


def report_or_not(file_path, str_str):
    """
    :param file_path:
    :param str_str:
    :return:
    """
    if is_vuln_str(str_str) is not True:  # 不存在漏洞的
        return

    # 存在漏洞
    if file_path.endswith("_test.py"):
        return
    if file_path.endswith("_tests.py"):
        return
    if "/tests/" in file_path:
        return
    if "/test/" in file_path:
        return
    if "/pipenv/" in file_path:
        return
    if "test_regex.py" in file_path:
        return

    print(file_path, str_str)


def is_bad_dir(dir_path):

    for i in os.listdir(dir_path):
        file_path = dir_path + os.sep + i

        if os.path.isfile(file_path):
            if i.endswith(".py"):
                str_list = find_python_str(file_path)
                for str_str in str_list:
                    report_or_not(file_path, str_str)

        elif os.path.isdir(file_path):
            if i in [".", ".."]:
                continue
            else:
                is_bad_dir(file_path)


def test1():
    str_list = find_python_str("/tmp/_header_value_parser.py")
    for str_str in str_list:
        is_vuln_str(str_str)


def test2():
    is_vuln_str("(a.*)*y")


if __name__ == "__main__":
    is_bad_dir("/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7")
    is_bad_dir("/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/python-skeletons")
    is_bad_dir("/usr/local/lib/python3.7/site-packages")
    is_bad_dir("/Users/xxxxxxx/Library/Python/3.7/lib/python/site-packages")
