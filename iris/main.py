from iris.knn import classify_score


def main():
    train_scores, test_scores = classify_score(1, 20)

    print(f"Training set scores: {train_scores}")

    print(f"Test set scores: {test_scores}")

if __name__ == "__main__":
    main()