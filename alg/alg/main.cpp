
#include "alg_lib.h"

int main()
{
	//vector<int> vec;
	//vec.push_back(1);
	//vec.push_back(1);
	//vec.push_back(1);
	//vec.push_back(2);
	//vec.push_back(2);
	//vec.push_back(3);
	//vec.push_back(6);
	//vec.push_back(6);
	//vector<int>::iterator it; 
	//int sum = 0;
	//sum = getNum(vec);
	//cout << sum << endl;
	int a[10] = { 1,3,6,2,4,2,4,2,42,4 };
	BubbleSort5(a, 10);
	for (int i = 0; i < 10; i++)
	{
		cout << a[i] << endl;
	}
	system("pause");
	return 0;
} 