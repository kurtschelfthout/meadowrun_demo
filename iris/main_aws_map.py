import asyncio

from meadowrun import AllocCloudInstances, Deployment, run_map

from iris.knn import classify_score


async def main():
    results = await run_map(
        # the function to run
        classify_score, 
        # the list of arguments - function is called once for each argument
        list(range(1,21)),
        # properties of the VMs on which to run the function
        AllocCloudInstances( 
            logical_cpu_required_per_task=1,
            memory_gb_required_per_task=4,
            interruption_probability_threshold=15,
            cloud_provider="EC2",
            num_concurrent_tasks=4),
        # what to deploy on the VM - here local code and activated conda env
        await Deployment.mirror_local(), 
    )
    print()
    print(f"Scores: {tuple(results)}")
    

if __name__ == "__main__":
    asyncio.run(main())
