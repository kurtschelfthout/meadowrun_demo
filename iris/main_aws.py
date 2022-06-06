import asyncio

from meadowrun import AllocCloudInstance, Deployment, run_function

from iris.knn import classify_score


async def main():
    train_scores, test_scores = await run_function(
        classify_score, # the function to run
        AllocCloudInstance( # properties of the VM on which to run the function
            logical_cpu_required=2,
            memory_gb_required=16,
            interruption_probability_threshold=15,
            cloud_provider="EC2"),
        await Deployment.mirror_local(), # what to deploy on the VM - here local code and conda env
        # Alternative which doesn't need local checkout/conda env:
        # Deployment.git_repo(
        #     "https://github.com/kurtschelfthout/meadowrun_demo",
        #     conda_yml_file="env.yml",
        # )
        (1,20) # arguments to classify_score
    )
    print()
    print(f"Training set scores: {train_scores}")
    print()
    print(f"Test set scores: {test_scores}")

if __name__ == "__main__":
    asyncio.run(main())
