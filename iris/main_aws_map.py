import asyncio

from meadowrun import AllocCloudInstances, Deployment, run_map

from iris.knn import classify_score


async def main():
    results = await run_map(
        classify_score, # the function to run
        list(range(1,21)),
        AllocCloudInstances( # properties of the VM on which to run the function
            logical_cpu_required_per_task=1,
            memory_gb_required_per_task=4,
            interruption_probability_threshold=15,
            cloud_provider="EC2",
            num_concurrent_tasks=4),
        await Deployment.mirror_local(), # what to deploy on the VM - here local code and conda env
    )
    print()
    print(f"Scores: {tuple(results)}")
    

if __name__ == "__main__":
    asyncio.run(main())
