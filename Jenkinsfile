node {
    stage('Build') {
        def stdout = powershell(returnStdout: true, script: '''
           $env:path="$env:Path;C:\\Users\\andya\\AppData\\Local\\Programs\\Python\\Python38"
           python ${workspace}@script\\17%2.py
           echo ""
           python ${workspace}@script\\근위병.py
        ''')
        println stdout;
        println '${workspace}@script'
    }
}
