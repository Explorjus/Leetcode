using System.Collections.Generic;

int[] nums = { 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 };

int usun_duplikaty(int[] nums)
{
	int k = 1;

	for (int i = 1; i < nums.Length; i++)
	{
		if (nums[i] != nums[k - 1])
		{
			nums[k] = nums[i];
			k++;
		}
	}
	return k;
}

int wynik = usun_duplikaty(nums);

Console.WriteLine(wynik);