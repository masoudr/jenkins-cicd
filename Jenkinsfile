pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                echo 'This is Django project so there is no need to build'
            }
        }
        stage('Test') { 
            steps {
                echo 'Testing Project...'
                sh 'docker-compose up --build'
            }
        }
        stage('Deploy') { 
            steps {
                // 
                echo 'Currently there is no deploy method'
            }
        }
        stage('Clean Up') {
            steps {
                echo 'Cleaning up project'
                sh 'docker-compose down -v --rmi all'
            }
        }
    }
}
