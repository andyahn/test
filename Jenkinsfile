node {
    stage('Build') {
        def stdout = powershell(returnStdout: true, script: '''
           $env:path="$env:Path;C:\\Users\\andya\\AppData\\Local\\Programs\\Python\\Python38"
           cd ..
           cd test_pipe@script
           python 17%2.py
           echo ""
           python 근위병.py
           del ../test_pipe@script@tmp
           del ../test_pipe@tmp
           del ../test_pipe
        ''')
        println stdout
    }
}
