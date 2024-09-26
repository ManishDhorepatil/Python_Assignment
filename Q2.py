#solution
def count_obstructions(test_cases):
    results = []
    
    for i in range(test_cases):
        N, K = map(int, input().split())
        heights = list(map(int, input().split()))
        
        count = 0
        for height in heights:
            if height > K:
                count += 1
       
        results.append(count)
    
    # Output 
    print("\n".join(map(str, results)))


if __name__ == "__main__":
    test_cases = int(input())  # Number of test cases for use 
    count_obstructions(test_cases)
