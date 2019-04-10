import os
from swiper import settings,config
from lib.qiniu_cloud import upload_to_qiniu
from urllib.parse import urljoin
from worker import celery_app


def upload_avatar_to_server(uid,avatar):
    filename = 'avatar-%s' % uid + os.path.split(avatar.name)[1]
    save_path = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, filename)

    with open(save_path, 'wb') as fp:
        for chunk in avatar.chunks():
            fp.write(chunk)
    return filename,save_path

@celery_app.task
def upload_avatar(user, avatar):

    file_name, saved_path = upload_avatar_to_server(user.id, avatar)
    upload_to_qiniu(file_name, saved_path)
    avatar_url = urljoin(config.QINIU_BUCKET_URL,file_name)
    user.avatar = avatar_url
    user.save()