pipeline{
  agent any

  parameters {
    string(name: 'PRJ_NAME', defaultValue: 'app', description: 'Project name for build and deploy')
    string(name: 'EXTERNAL_PORT', defaultValue: '3000', description: 'External port for application')
    string(name: 'INTERNAL_PORT', defaultValue: '3000', description: 'Internal port for application')
  }

  environment{
    REPO = 'edy2010/node-app'
    DOCKER_TOKEN = credentials('dok-tok')
    DOCKER_IMAGE = "${REPO}:${params.PRJ_NAME}-${BUILD_NUMBER}"
  }

  stages{
    stage('Checkout'){
      steps{
        checkout scm
      }
    }
    stage('Build'){
      steps{
        script{
          sh"""
            docker build -t "${DOCKER_IMAGE}" .
          """
        }
      }
    }
    stage('Push to Docker Hab'){
      steps{
        script{
          sh"""
            docker login -u edy2010 -p ${env.DOCKER_TOKEN}
            docker push "${DOCKER_IMAGE}"
          """
        }
      }
    }
    stage('Deploy'){
      steps{
        script{
          sh"""
          docker pull "${DOCKER_IMAGE}"
          docker stop "${params.PRJ_NAME}" || true
          docker rm "${params.PJR_NAME}" || true
          docker run -d -it --name "${params.PRJ_NAME}" -p ${params.EXTERNAL_PORT}:${params.INTERNAL_PORT} "${DOCKER_IMAGE}"
          """
        }
      }
    }
  }  
}