#include <iostream>
#include "alg_lib.h"

using namespace std;

int main()
{
	int nArray[6] = { 1,6,2,4,7,3 };
	BubbleSort(nArray,6);
	for (int i = 0; i < sizeof(nArray)/sizeof(int);i++)
	{
		cout<<nArray[i]<<endl;
	}

	system("pause");
	return 0;
}