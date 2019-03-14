from django.db import models


class VideoDetail(models.Model):

    title = models.CharField(max_length=100)
    detail_description = models.CharField(max_length=5000)
    short_description = models.CharField(max_length=1000)
    img_url = models.CharField(max_length=255)
    video_url = models.CharField(max_length=255)
    video_id = models.CharField(max_length=200)

    class Meta:
        db_table = 'video_detail'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.titles

    @classmethod
    def add_detail(cls, obj):

        video_id = obj['video_url']
        video_id = video_id.split('/')[-1]
        video_id = video_id.split('?')[0]

        return cls.objects.create(title=obj['title'], detail_description=obj['description'],
                                  short_description= obj['short_description'],
                                    img_url=obj['img_url'], video_url=obj['video_url'],
                                  video_id=video_id)
