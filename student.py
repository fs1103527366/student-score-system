def score_stat(scores):
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores)/len(scores)
    print(f"最高分：{max_score}")
    print(f"最低分：{min_score}")
    print(f"平均分：{avg_score:.2f}")

if __name__ == "__main__":
    score_list = [85,92,78,66,90]
    score_stat(score_list)