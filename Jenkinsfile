pipeline {
    // agent any
    agent {
        docker {
            image 'python:3.8'  // Use an appropriate Python Docker image
            args '-u root:root' // Run as root to install packages
        }
    }

    environment {
        DOCKER_IMAGE = 'your_docker_username/flask_app:latest'
        FLASK_APP_DIR = 'proj_xgb'
    }

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    echo 'Setting up the environment...'
                    sh 'pip install flake8 bandit pytest'
                }
            }
        }

        stage('Checkout') {
            steps {
                script {
                    // withCredentials([string(credentialsId: 'edaraanand', variable: 'anand-pat')]) {
                        // git url: 'https://github.com/edaraanand/proj_xgb.git', credentialsId: 'anand-pat'
                    git branch: 'main', credentialsId: 'edaraanand', url: 'https://github.com/edaraanand/proj_xgb.git'
                    // }
                }
            }
        }

        stage('Check Syntax') {
            steps {
                script {
                    echo 'Checking Python syntax...'
                    sh 'ls -ltr'
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
