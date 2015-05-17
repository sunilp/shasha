from invoke import task, run

@task
def deploy():
    run('pip freeze > requirements.txt')
    run('git add .')
    print("enter your git commit comment: ")
    comment = input()
    run('git commit -m "%s"' % comment)
    run('git push -u origin master')
    run('heroku maintenance:on')
    run('git push heroku master')
    run('heroku maintenance:off')
