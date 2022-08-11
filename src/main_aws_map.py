import asyncio

from meadowrun import AllocCloudInstance, Deployment, Resources, run_map

from iris.knn import classify_score


async def main():
    results = await run_map(
        # the function to run
        classify_score, 
        # the list of arguments - function is called once for each argument
        list(range(1,21)),
        # run on AWS EC2 instances
        AllocCloudInstance(cloud_provider="EC2"),
        # run 4 workers
        num_concurrent_tasks=4,
        # resources required per worker
        resources_per_task = Resources( 
            logical_cpu=1,
            memory_gb=1,
            max_eviction_rate=80),
        # what to deploy - in this case local code and conda env
        deployment=await Deployment.mirror_local(), 
    )
    print()
    print(f"Scores: {tuple(results)}")
    

if __name__ == "__main__":
    asyncio.run(main())
