node {
    customWorkspace "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Jenkins\\.jenkins\\workspace\\test_pipe"
    stage('Build') {
        def stdout = powershell(returnStdout: true: '''
           $env:path="$env:Path;C:\\Users\\andya\\AppData\\Local\\Programs\\Python\\Python38"
           python 13,17%2.py
           echo ""
           python 근위병.py
        ''')
        println stdout
    }
}
