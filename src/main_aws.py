import asyncio

from meadowrun import AllocCloudInstance, Deployment, Resources, run_function

from iris.knn import classify_score


async def main():
    train_scores, test_scores = await run_function(
        # the function to run
        lambda: classify_score(1,20), 
        # run on an AWS EC2 instance
        AllocCloudInstance(cloud_provider="EC2"),
        # requirements for the EC2 instance
        Resources(logical_cpu=1, memory_gb=4, max_eviction_rate=80),
        # what to deploy on the VM - in this case local code and env
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
