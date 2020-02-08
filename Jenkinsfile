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
                docker-compose up --build
            }
        }
        stage('Deploy') { 
            steps {
                // 
                echo 'Currently there is no deploy method'
            }
        }
    }
}
