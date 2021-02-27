# coding:utf-8
import ast


class CodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.str_token_list = []

    def visit_Str(self, node):
        # print(node.s)
        self.str_token_list.append(node.s)
        self.generic_visit(node)

    def visit_Bytes(self, node):
        # print(node.s.decode())
        try:
            self.str_token_list.append(node.s.decode())
        except Exception as _:
            pass
        self.generic_visit(node)

        
def find_python_str(code_file_path):
    """
    从python代码中找到所有常量字符串
    :param code_file_path:
    :return:
    """
    with open(code_file_path, "rb") as f:
        content = f.read()

    try:
        r_node = ast.parse(content)
        # print(ast.dump(r_node))
    except:
        return []

    visitor = CodeVisitor()
    visitor.visit(r_node)
    return visitor.str_token_list


def test():

    _ = find_python_str("test_data/1.py")
    # print(_)
    assert _ == ['a', 'b', '\nzzzzz\n']


# def find_python_str(code_file_path):
#     """
#     从python代码中找到所有常量字符串
#     :param code_file_path:
#     :return:
#     """
#     ret_list = []
#     with open(code_file_path, "rb") as f:
#         tokens = list(tokenize(f.readline))
#         for token in tokens:
#             # print(token.string)
#             ret_list.append(token.string)
#     return list(set(ret_list))


if __name__ == "__main__":
    test()
