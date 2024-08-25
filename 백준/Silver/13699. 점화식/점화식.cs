using System;

namespace C_
{
    internal class _13699
    {
        public static void Main(string[] args)
        {
            long n = long.Parse(Console.ReadLine());

            long[] nums = new long[36];
            nums[0] = 1;
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j <= i; j++) {
                    nums[i + 1] += nums[j] * nums[i - j];
                }
            }
            Console.WriteLine(nums[n]);
            Console.ReadLine();
        }
    }
}
