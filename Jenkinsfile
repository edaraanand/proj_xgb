pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'your_docker_username/flask_app:latest'
        FLASK_APP_DIR = 'path/to/your/flask/app'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'edaraanand', variable: 'edaraanand')]) {
                        git url: 'https://github.com/edaraanand/proj_xgb.git', credentialsId: 'edaraanand'
                    }
                }
            }
        }

        stage('Check Syntax') {
            steps {
                script {
                    echo 'Checking Python syntax...'
                    sh 'flake8 ${FLASK_APP_DIR}'
                }
            }
        }

        stage('Security Scan') {
            steps {
                script {
                    echo 'Running security scan...'
                    sh 'bandit -r ${FLASK_APP_DIR}'
                }
            }
        }

        stage('Unit Test') {
            steps {
                script {
                    echo 'Running unit tests...'
                    sh 'pytest ${FLASK_APP_DIR}'
                }
            }
        }

        stage('Build Application') {
            steps {
                script {
                    echo 'Building the Flask application...'
                    sh 'python ${FLASK_APP_DIR}/setup.py build'
                }
            }
        }

        stage('Create Docker Image') {
            steps {
                script {
                    echo 'Creating Docker image...'
                    sh 'docker build -t ${DOCKER_IMAGE} ${FLASK_APP_DIR}'
                    sh 'docker push ${DOCKER_IMAGE}'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            cleanWs()
        }
    }
}
