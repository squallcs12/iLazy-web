from ilazy_web.celery import app


@app.task
def execute_app():
    pass
