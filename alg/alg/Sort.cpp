#include <iostream>
#include "alg_lib.h"

using namespace std;

void BubbleSort(int nArray[], int n)
{
	int flag = n;
	int k = 0;

	while (flag>0)
	{
		k = flag;
		flag = 0;
		for (int i = 1; i < k;i++)
		{
			if (nArray[i - 1] > nArray[i])
			{
				int tmp= nArray[i - 1];
				nArray[i-1] = nArray[i];
				nArray[i] = tmp;
				flag = i;
			}
		}
	}
}


TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
	if (t1)
	{
		if (t2)
		{
			t1->val += t2->val;
			if (t1->left && t2->left)
				mergeTrees(t1->left, t2->left);
			if (t1->right && t2->right)
				mergeTrees(t1->right, t2->right);
			if (!t1->left && t2->left)
			{
				t1->left = t2->left;
			}
			if (!t1->right && t2->right)
			{
				t1->right = t2->right;
			}
		}
		else
		{
			return t1;
		}
	}
	else
	{
		t1 = t2;
	}
	return t1;
}

//1,3,2,5
void  CreateTree1(TreeNode * p_tree)
{
	p_tree->val = 1;
	TreeNode* p_1 = new TreeNode;
	p_1->val = 3;
	TreeNode* p_2 = new TreeNode;
	p_2->val = 2;
	TreeNode* p_3 = new TreeNode;
	p_3->val = 5;

	p_tree->left = p_1;
	p_tree->right = p_2;

	p_1->left = p_3;
	p_1->right = NULL;

	p_2->left = NULL;
	p_2->right = NULL;

	p_3->left = NULL;
	p_3->right = NULL;
}

//2,1,3,NULL,4,NULL£¬7
void  CreateTree2(TreeNode * p_tree)
{
	p_tree->val = 2;
	TreeNode* p_1 = new TreeNode;
	p_1->val = 1;
	TreeNode* p_2 = new TreeNode;
	p_2->val = 3;
	TreeNode* p_3 = new TreeNode;
	p_3->val = 4;

	TreeNode* p_4 = new TreeNode;
	p_4->val = 7;

	p_tree->left = p_1;
	p_tree->right = p_2;

	p_1->left = NULL;
	p_1->right = p_3;

	p_2->left = NULL;
	p_2->right = p_4;

	p_3->left = NULL;
	p_3->right = NULL;

	p_4->left = NULL;
	p_4->right = NULL;
}

void pre(TreeNode* p_root)
{
	if (p_root)
		cout << p_root->val << endl;
	if (p_root->left)
		pre(p_root->left);
	if (p_root->right)
		pre(p_root->right);
}