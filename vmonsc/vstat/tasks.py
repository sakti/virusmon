from celery import task


@task
def process_post_result(post_id):
    print post_id
