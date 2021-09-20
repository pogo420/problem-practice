# Max distribution between n elements.
# i -> j dissipation(K) during transfer
# Find max power distribution.

# power of 2 and sum of digits till we get single digit
# any number % 9 == 0 sum aff all digits till single = 9
# any number can be represent as n = 9x + k so n % 9

# can we make a list strictly increasing by doing  A[i] - K, where A[0] <= K < =A[N]
# if A[i-1] <= A[i] <= A[i+1] then ok
# else A[i] = A[i-1] + A[i+1] // 2 but A[i] != A[i+1] != A[i-1]
