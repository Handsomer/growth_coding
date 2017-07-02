#include <iostream>
#include "alg_lib.h"

using namespace std;

int main()
{
	TreeNode*  p_root1 = new TreeNode;
	TreeNode*  p_root2 = new TreeNode;
	CreateTree1(p_root1);
	CreateTree2(p_root2);
	
	mergeTrees(p_root1, p_root2);
	pre(p_root1);
	system("pause");
	return 0;
}