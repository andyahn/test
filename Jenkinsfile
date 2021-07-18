node {
    stage('Build') {
        def stdout = powershell(returnStdout: true, script: f'''
           $env:path="$env:Path;C:\\Users\\andya\\AppData\\Local\\Programs\\Python\\Python38"
           python {dir("${workspace}@script")}\\13,17%2.py
           echo ""
           python C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Jenkins\\.jenkins\\workspace\\test_pipe@script\\근위병.py
        ''')
        println stdout
    }
}
