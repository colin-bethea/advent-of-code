'''

--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

'''

import csv

target = 2020

def solve():
   with open('../input.csv', newline='') as f:
      reader = csv.reader(f)
      nums = list(map(lambda x: int(x[0]), list(reader)))
      for n1 in nums:
         for n2 in nums:
            for n3 in nums:
               if n1 + n2 + n3 == target:
                  return n1 * n2 * n3
   
print(solve())