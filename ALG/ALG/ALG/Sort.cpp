#include <iostream>
#include "mainALG.h"

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
