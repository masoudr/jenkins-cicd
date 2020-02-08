pipeline {
    agent any
    stages {
        
        stage('Build') { 
            steps {
                echo 'This is a Django project so there is no need to build'
            }
        }

        stage('Test') { 
            steps {
                echo 'Testing Project...'
                sh 'docker-compose build'
                sh 'docker-compose run app sh -c "python manage.py test"'
            }
        }

        stage('Deploy') { 
            steps {
                echo 'Deploying to hub'
                sh 'docker-compose push'
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
