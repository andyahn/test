node {
    stage('Build') {
        def stdout = powershell(returnStdout: true, script: '''
           $env:path="$env:Path;C:\\Users\\andya\\AppData\\Local\\Programs\\Python\\Python38"\n'''+
           'python ' + dir("${workspace}@script") + '\\17%2.py\n'+
           'echo ""\n'+
           'python ' + dir("${workspace}@script") '\\근위병.py'
        )
        println stdout
    }
}
