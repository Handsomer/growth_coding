#include "alg_lib.h"

int main()
{
	vector<int> vec;
	vec.push_back(1);
	vec.push_back(5);
	vec.push_back(3);
	vec.push_back(9);
	vector<int>::iterator it;
	for (it = vec.begin(); it < vec.end(); it++)
	{
		cout << *it << endl;
	}
	sort(vec.begin(),vec.end(),sortBy);
	int sum = 0;
	sum = arrayPairSum(vec);
	cout << sum << endl;
	system("pause");
	return 0;
} 