# Python Assignment

## Question 1: Convert Integer Values to Indian Currency Notation

### Problem Statement:
Write a Python code to convert integer values to Indian currency notations without using any currency libraries.

### Example:
- **Input**: `504678`
- **Output**: `5,04,678`

### Explanation:
The task is to format an integer value by adding commas in the Indian numbering system, where the first comma comes after three digits from the right, and subsequent commas come after every two digits.

### Input Format:
- A single integer representing the value to be converted.

### Output Format:
- The formatted string in Indian currency notation.

### Constraints:
- The input will always be a positive integer.

---

## Question 2: Minimum Players to Be Shot

### Problem Statement:
Gi-Hun and Ali have the same height. Gi-Hun wants to hide behind Ali, but there are `N` players standing between them. Gi-Hun wants to know how many players need to be shot so that Ali is visible in his line of sight.

### Note:
- Ali is visible if no one between Gi-Hun and Ali is taller than them.
- Players with the same height as Gi-Hun and Ali do not obstruct the line of sight.

### Input Format:
- The first line contains a single integer `T` — the number of test cases.
- For each test case:
  - The first line contains two space-separated integers `N` and `K` — the number of players between Gi-Hun and Ali, and the height of both Gi-Hun and Ali.
  - The second line contains `N` space-separated integers representing the heights of the players standing between them.

### Output Format:
For each test case, output the minimum number of players that need to be shot for Ali to be visible to Gi-Hun.

### Constraints:
- \( 1 \leq T \leq 10^5 \)
- \( 1 \leq N \leq 10^5 \)
- \( 1 \leq K \leq 10^6 \)
- \( 1 \leq H_i \leq 10^6 \) for every \( 1 \leq i \leq N \)
- The sum of \( N \) across all test cases does not exceed \( 5 \times 10^5 \)

### Sample Input:
