import asyncio

from meadowrun import Deployment, EC2AllocHost, run_function

from iris.knn import classify_score


async def main():
    train_scores, test_scores = await run_function(
        lambda: classify_score(1, 20),
        EC2AllocHost(
            logical_cpu_required=2,
            memory_gb_required=16,
            interruption_probability_threshold=15),
        Deployment.git_repo(
            "https://github.com/kurtschelfthout/meadowrun_demo",
            conda_yml_file="env.yml",
        )
    )
    print()
    print(f"Training set scores: {train_scores}")
    print()
    print(f"Test set scores: {test_scores}")

if __name__ == "__main__":
    asyncio.run(main())
