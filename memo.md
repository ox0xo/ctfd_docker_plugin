https://docker-py.readthedocs.io/en/stable/index.html
https://docs.ctfd.io/docs/plugins/overview


docker build -t mydns .
docker network create wetty-mydns
docker run -d --rm --name wetty --network wetty-mydns -p 3000:3000 wettyoss/wetty --ssh-host=mydns
docker run -d --rm --name mydns --network wetty-mydns mydns
docker stop wetty
docker stop mydns
docker network rm wetty-mydns


import docker
client = docker.from_env()
client.networks.create("wetty-mydns")
client.containers.run(detach=True, remove=True, network="wetty-mydns", image="mydns", name="mydns")
client.containers.run(detach=True, remove=True, network="wetty-mydns", image="wettyoss/wetty", name="wetty", ports={"3000/tcp":3000}, environment=["SSHUSER=root","SSHHOST=mydns","SSHPORT=22","SSHPASS=P@ssw0rd"])
client.containers.get("wetty").stop()
client.containers.get("mydns").stop()
client.networks.get("wetty-mydns").remove()

