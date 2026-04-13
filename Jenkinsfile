pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                . venv/bin/activate
                python scripts/train.py
                '''
            }
        }

        stage('Read Metrics') {
            steps {
                sh '''
                . venv/bin/activate
                echo "===== MODEL METRICS ====="
                echo "btach2_2022bcs0098"

                python -c "
import json
m=json.load(open('metrics.json'))
print('R2:',m['r2'])
print('MSE:',m['mse'])
"
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                docker build -t kushal2022bcs0098/btach2_2022bcs0098:latest .
                '''
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([
                    string(credentialsId: 'DOCKER_USERNAME', variable: 'DOCKER_USERNAME'),
                    string(credentialsId: 'DOCKER_PASSWORD', variable: 'DOCKER_PASSWORD')
                ]) {
                    sh '''
                    echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                    docker push kushal2022bcs0098/batch2_2022bcs0098:latest
                    '''
                }
            }
        }
    }
}
