pipeline {
    agent any 
    stages {
        stage('Tests') {
            steps {
                dir('flask-app'){
                    sh "echo this is a test"
                    // sh "rm application/test/test_int*"
                    // sh "bash test.sh"
                }
            }
        }

        stage('docker push') {
            steps {
                sh "/bin/bash -c 'docker rmi \$(docker images -q)'"
                sh "docker-compose build --parallel"
                sh "docker login -u ${DOCKER_CRED_USR} -p ${DOCKER_CRED_PSW}"
                sh "docker-compose push" 
            }
        }
        stage('docker swarm) { 
            sh "docker stack deploy --compose-file docker-compose.yaml flask-app"    
        }
    }
}
