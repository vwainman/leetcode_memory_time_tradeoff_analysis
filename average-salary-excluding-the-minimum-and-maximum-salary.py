# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/
#
# You are given an array of unique integers salary where salary[i] is the
# salary of the i^th employee.
#
# Return the average salary of employees excluding the minimum and maximum
# salary. Answers within 10^-5 of the actual answer will be accepted.


from typing import List


def average(salary: List[int]) -> float:
    salary_sum = salary[0]
    min_sal = salary[0]
    max_sal = salary[0]
    for pay in salary[1:]:
        min_sal = min(min_sal, pay)
        max_sal = max(max_sal, pay)
        salary_sum += pay
    total_sals = salary_sum - min_sal - max_sal
    n_sals = float((len(salary) - 2))  # cast to prevent int division result
    return total_sals / n_sals
