# Generated by Django 4.1.7 on 2023-08-12 09:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaignquestionresponse',
            fields=[
                ('response', models.CharField(db_column='response', max_length=2000, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'campaignquestionresponse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Campaignvideo',
            fields=[
                ('campaignvideoid', models.CharField(db_column='campaignvideoid', max_length=255, primary_key=True, serialize=False)),
                ('campaignid', models.CharField(blank=True, db_column='campaignid', max_length=255, null=True)),
                ('previousvideoid', models.CharField(blank=True, db_column='previousvideoid', max_length=255, null=True)),
            ],
            options={
                'db_table': 'campaignvideo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbApprove',
            fields=[
                ('videoid', models.CharField(db_column='videoid', max_length=250, primary_key=True, serialize=False)),
                ('videotitle', models.CharField(blank=True, db_column='videotitle', max_length=255, null=True)),
                ('videopath', models.CharField(blank=True, db_column='videopath', max_length=255, null=True)),
                ('uploadername', models.CharField(blank=True, db_column='uploadername', max_length=255, null=True)),
                ('approveddate', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'tb_approve',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbapproverQuestion',
            fields=[
                ('questionid', models.CharField(db_column='questionid', max_length=255, primary_key=True, serialize=False)),
                ('questiontext', models.CharField(db_column='questiontext', max_length=2000)),
            ],
            options={
                'db_table': 'tb_approverquestion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbCampaignquestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaignquestionid', models.CharField(db_column='campaignquestionid', max_length=255)),
            ],
            options={
                'db_table': 'tb_campaignquestion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbQuestion',
            fields=[
                ('questionid', models.CharField(db_column='questionid', max_length=255, primary_key=True, serialize=False)),
                ('questiontext', models.CharField(db_column='questiontext', max_length=2000)),
                ('questionresponse', models.CharField(db_column='questionresponse', max_length=4000)),
            ],
            options={
                'db_table': 'tb_question',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbStatus',
            fields=[
                ('videoid', models.CharField(db_column='videoid', max_length=250, primary_key=True, serialize=False)),
                ('reason', models.CharField(blank=True, db_column='reason', max_length=255, null=True)),
                ('videoname', models.CharField(blank=True, db_column='videoname', max_length=255, null=True)),
                ('approver', models.CharField(blank=True, db_column='approver', max_length=255, null=True)),
                ('status', models.CharField(blank=True, db_column='status', max_length=255, null=True)),
                ('uploadername', models.CharField(blank=True, db_column='uploadername', max_length=255, null=True)),
                ('platform', models.CharField(db_column='platform', max_length=2000)),
                ('createddate', models.DateTimeField(default=datetime.datetime.now)),
                ('videoPath1', models.CharField(blank=True, db_column='videopath1', max_length=2000, null=True)),
                ('videoPath', models.CharField(blank=True, db_column='videopath', max_length=2000, null=True)),
                ('Imageurl', models.CharField(blank=True, db_column='imgurl', max_length=255, null=True)),
                ('Gifurl', models.CharField(blank=True, db_column='gifurl', max_length=255, null=True)),
                ('creative', models.CharField(db_column='creative', max_length=255)),
                ('MainReason', models.CharField(blank=True, db_column='mainreason', max_length=2000, null=True)),
            ],
            options={
                'db_table': 'tb_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbUser',
            fields=[
                ('userid', models.CharField(db_column='userid', max_length=255, primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='username', max_length=250)),
                ('password', models.CharField(blank=True, db_column='password', max_length=255, null=True)),
                ('vendor', models.CharField(blank=True, db_column='vendor', max_length=255, null=True)),
            ],
            options={
                'db_table': 'tb_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbUserrole',
            fields=[
                ('userroleid', models.CharField(db_column='userroleid', max_length=255, primary_key=True, serialize=False)),
                ('userrolename', models.CharField(db_column='userrolename', max_length=250)),
            ],
            options={
                'db_table': 'tb_userrole',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbVideo',
            fields=[
                ('videoid', models.CharField(db_column='videoid', max_length=255, primary_key=True, serialize=False)),
                ('previousvideoid', models.CharField(blank=True, db_column='previousvideoid', max_length=255, null=True)),
                ('videoname', models.CharField(db_column='videoname', max_length=2000)),
                ('videopath', models.CharField(db_column='videopath', max_length=2000)),
                ('videotranscription', models.TextField(db_column='videotranscription')),
                ('vendor', models.CharField(db_column='vendor', max_length=2000)),
                ('lob', models.CharField(db_column='lob', max_length=2000)),
                ('creative', models.CharField(db_column='creative', max_length=2000)),
                ('platform', models.CharField(db_column='platform', max_length=2000)),
                ('videopath1', models.CharField(blank=True, db_column='videopath1', max_length=2000, null=True)),
                ('videotranscription1', models.TextField(db_column='videotranscribeone')),
                ('creater', models.CharField(blank=True, db_column='creater', max_length=255, null=True)),
                ('Imageurl', models.CharField(blank=True, db_column='imgurl', max_length=255, null=True)),
                ('Gifurl', models.CharField(blank=True, db_column='gifurl', max_length=255, null=True)),
            ],
            options={
                'db_table': 'tb_video',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='video_Details',
            fields=[
                ('VideoPath', models.CharField(db_column='videopath', max_length=2000, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'videodetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='cVideoId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VideoID', models.CharField(db_column='videoID', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(blank=True, db_column='UserID', max_length=255)),
                ('username', models.CharField(blank=True, db_column='UserName', max_length=255)),
                ('userroleid', models.CharField(blank=True, db_column='UserRoleId', max_length=255)),
                ('vendor', models.CharField(blank=True, db_column='Vendor', max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
