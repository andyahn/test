pipeline {
    node {
        stage('Build') {
            def stdout = powershell(returnStdout: true, script: '''
               $env:path="$env:Path;C:\\Users\\andya\\AppData\\Local\\Programs\\Python\\Python38"
               cd ..
               cd test_pipe@script
               python 17%2.py
               echo ""
               python 근위병.py
            ''')
            println stdout
        }
    }
    stage('del') {
        post {
            cleanup {
                /* clean up our workspace */
                deleteDir()
                /* clean up tmp directory */
                dir("${workspace}@tmp") {
                    deleteDir()
                }
                /* clean up script directory */
                dir("${workspace}@script@tmp") {
                    deleteDir()
                }
            }
        }
    }
}
