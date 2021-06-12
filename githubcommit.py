import subprocess as cmd

def git_commit():
    
    cp = cmd.run("git add .", check=True, shell=True)
    #print(cp)

    message = "Datafeed updated"

    cp = cmd.run(f"git commit -m '{message}'", check=True, shell=True)
    cp = cmd.run("git push -u origin main -f", shell=True)
