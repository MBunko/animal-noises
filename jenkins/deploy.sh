#!/bin/bash
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@swarm-master:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/ansible_id_rsa jenkins@swarm-master << EOF
    export DATABASE_URI=${DATABASE_URI} app_version=${app_version} replicas=${replicas}
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml animal-noises
EOF