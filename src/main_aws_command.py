import asyncio

import meadowrun

async def main(): 
    await meadowrun.run_command(
        # the command to run
        ("python", "--version"), 
        # run on an AWS EC2 instance
        meadowrun.AllocEC2Instance(),
        # requirements for the EC2 instance
        meadowrun.Resources(logical_cpu=1, memory_gb=1, max_eviction_rate=80),
        # what to deploy on the VM - here an image in a container registry
        meadowrun.Deployment.container_image(
            repository="python", 
            tag="slim-bullseye"
        ),
    )

if __name__ == "__main__":
    asyncio.run(main())