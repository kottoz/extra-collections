import pytest
from tests import *
from extra.trees.tree import TreeNode, Tree


def test_treenode():
    with pytest.raises(TypeError):
        TreeNode(None)
    with pytest.raises(ValueError):
        TreeNode('')
        TreeNode('      ')
        TreeNode('\t\n')
    # the following shouldn't raise anything
    TreeNode(get_int())
    TreeNode(get_float())
    TreeNode(get_string())
    TreeNode(get_value())
    TreeNode(get_list())


# def test_tree_with_known_values():
#     # create Simpsons Family tree
#     root = TreeNode('TheSimpsons')
#     # homer-side
#     abraham = TreeNode('Abraham + Mona')
#     herb = TreeNode('Herb')
#     homer = TreeNode('Homer')
#     abraham.children = [herb, homer]
    
#     # marge-side
#     jackie = TreeNode('Clancy + Jackie')
#     marge = TreeNode('Marge')
#     patty = TreeNode('Patty')
#     selma = TreeNode('Selma')
#     ling = TreeNode('Ling')
#     selma.children = [ling]
#     jackie.children = [marge, patty, selma]

#     # homer-marge children
#     bart = TreeNode('Bart')
#     lisa = TreeNode('Lisa')
#     maggie = TreeNode('Maggie')
#     homer.children = [bart, lisa, maggie]
#     marge.children = homer.children
#     # set root
#     root.children = [abraham, jackie]
#     t = Tree(root)
#     print(t)
#     print(len(t))