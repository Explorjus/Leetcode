using System;

int[] nums = {1,5,3,5,3,2,3,4,5,2};
int val = 2;

int k = 0;

for (var i = 0; i < nums.Length; i++)
{
    if (nums[i] != val)
    {
        nums[k] = nums[i];
        k++;
    }
}

Console.WriteLine("k = " + k);
Console.WriteLine(string.Join(", ", nums[..k]));
