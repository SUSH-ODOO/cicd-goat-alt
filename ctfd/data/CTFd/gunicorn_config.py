import aikido_zen.decorators.gunicorn as aik


@aik.post_fork
def post_fork(server, worker):
    # If you already have a config file, replace pass with your own code.
    pass
