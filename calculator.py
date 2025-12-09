def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == "__main__":
    scores = [80, 90, 100]
    print(f"平均点: {calculate_average(scores)}")
    
    # バグ確認用: 空リストを渡すと死ぬ
    empty_scores = []
    print(f"空の平均: {calculate_average(empty_scores)}")

