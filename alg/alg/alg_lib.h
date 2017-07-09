#include <iostream>
#include <vector>
#include <algorithm>
using  namespace std;

void BubbleSort(int nArray[], int n);

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	//	TreeNode(int x) : val(x), left(NULL), right(NULL) {}

};


TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2);
void  CreateTree1(TreeNode * p_tree);
void  CreateTree2(TreeNode * p_tree);
void pre(TreeNode* p_root);
int arrayPairSum(vector<int>& nums);//vector 需要使用 using namespace std; 来声明下

bool sortBy(int a, int b);