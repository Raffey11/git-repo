def fibonacci(num: int) -> int:
    print("Hello Raffey Commit")
    if num in {0, 1}:
        return num
    print("Hello Post Commit")
    return fibonacci(num - 1) + fibonacci(num - 2)

if __name__ == '__main__':
    print("Hello Raffey")
    print(fibonacci(10))
