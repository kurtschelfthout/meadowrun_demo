import asyncio

from meadowrun import AllocCloudInstance, Deployment, run_function

from iris.knn import classify_score


async def main():
    train_scores, test_scores = await run_function(
        # the function to run
        lambda: classify_score(1,20), 
        # properties of the VM that runs the function
        AllocCloudInstance( 
            logical_cpu_required=2,
            memory_gb_required=16,
            interruption_probability_threshold=15,
            cloud_provider="EC2"),
        # what to deploy on the VM - in this case local code and conda env
        await Deployment.mirror_local(),
        # Alternatively run from a git repository:
        # Deployment.git_repo(
        #     "https://github.com/kurtschelfthout/meadowrun_demo",
        #     conda_yml_file="env.yml",
        # )
    )
    print()
    print(f"Training set scores: {train_scores}")
    print()
    print(f"Test set scores: {test_scores}")

if __name__ == "__main__":
    asyncio.run(main())
