# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0010_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectBatchFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crowdsourcing.BatchFile')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectcomment_comment', to='crowdsourcing.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='bookmarkedprojects',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='bookmarkedprojects',
            name='project',
        ),
        migrations.RemoveField(
            model_name='module',
            name='batch_files',
        ),
        migrations.RemoveField(
            model_name='module',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='module',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='module',
            name='project',
        ),
        migrations.RemoveField(
            model_name='module',
            name='templates',
        ),
        migrations.AlterUniqueTogether(
            name='modulebatchfile',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='modulebatchfile',
            name='batch_file',
        ),
        migrations.RemoveField(
            model_name='modulebatchfile',
            name='module',
        ),
        migrations.AlterUniqueTogether(
            name='modulecategory',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='modulecategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='modulecategory',
            name='module',
        ),
        migrations.RemoveField(
            model_name='modulecomment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='modulecomment',
            name='module',
        ),
        migrations.AlterUniqueTogether(
            name='modulerating',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='modulerating',
            name='module',
        ),
        migrations.RemoveField(
            model_name='modulerating',
            name='worker',
        ),
        migrations.AlterUniqueTogether(
            name='modulereview',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='modulereview',
            name='module',
        ),
        migrations.RemoveField(
            model_name='modulereview',
            name='worker',
        ),
        migrations.AlterUniqueTogether(
            name='moduletemplate',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='moduletemplate',
            name='module',
        ),
        migrations.RemoveField(
            model_name='moduletemplate',
            name='template',
        ),
        migrations.AlterUniqueTogether(
            name='projectrequester',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='projectrequester',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectrequester',
            name='requester',
        ),
        migrations.RemoveField(
            model_name='workermoduleapplication',
            name='module',
        ),
        migrations.RemoveField(
            model_name='workermoduleapplication',
            name='worker',
        ),
        migrations.RemoveField(
            model_name='project',
            name='collaborators',
        ),
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='save_to_drive',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='qualification',
            name='module',
        ),
        migrations.RemoveField(
            model_name='task',
            name='module',
        ),
        migrations.RemoveField(
            model_name='workerrequesterrating',
            name='module',
        ),
        migrations.AddField(
            model_name='project',
            name='allow_feedback',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='data_set_location',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='feedback_permissions',
            field=models.IntegerField(choices=[(1, b'Others:Read+Write::Workers:Read+Write'), (2, b'Others:Read::Workers:Read+Write'), (3, b'Others:Read::Workers:Read'), (4, b'Others:None::Workers:Read')], default=1),
        ),
        migrations.AddField(
            model_name='project',
            name='has_data_set',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='is_micro',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='is_prototype',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='min_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='published_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='repetition',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.IntegerField(choices=[(1, b'Saved'), (2, b'Published'), (3, b'In Progress'), (4, b'Completed'), (5, b'Paused')], default=1),
        ),
        migrations.AddField(
            model_name='project',
            name='task_time',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='timeout',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='qualification',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='crowdsourcing.Project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_tasks', to='crowdsourcing.Project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workerrequesterrating',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rating_project', to='crowdsourcing.Project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(default=b'Untitled Project', error_messages={b'required': b'Please enter the milestone name!'}, max_length=128),
        ),
        migrations.AlterUniqueTogether(
            name='projectcategory',
            unique_together=set([('category', 'project')]),
        ),
        migrations.DeleteModel(
            name='BookmarkedProjects',
        ),
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.DeleteModel(
            name='ModuleBatchFile',
        ),
        migrations.DeleteModel(
            name='ModuleCategory',
        ),
        migrations.DeleteModel(
            name='ModuleComment',
        ),
        migrations.DeleteModel(
            name='ModuleRating',
        ),
        migrations.DeleteModel(
            name='ModuleReview',
        ),
        migrations.DeleteModel(
            name='ModuleTemplate',
        ),
        migrations.DeleteModel(
            name='ProjectRequester',
        ),
        migrations.DeleteModel(
            name='WorkerModuleApplication',
        ),
        migrations.AddField(
            model_name='projecttemplate',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_template', to='crowdsourcing.Project'),
        ),
        migrations.AddField(
            model_name='projecttemplate',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crowdsourcing.Template'),
        ),
        migrations.AddField(
            model_name='projectcomment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectcomment_project', to='crowdsourcing.Project'),
        ),
        migrations.AddField(
            model_name='projectbatchfile',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crowdsourcing.Project'),
        ),
        migrations.AddField(
            model_name='project',
            name='batch_files',
            field=models.ManyToManyField(through='crowdsourcing.ProjectBatchFile', to='crowdsourcing.BatchFile'),
        ),
        migrations.AddField(
            model_name='project',
            name='templates',
            field=models.ManyToManyField(through='crowdsourcing.ProjectTemplate', to='crowdsourcing.Template'),
        ),
        migrations.AlterUniqueTogether(
            name='projecttemplate',
            unique_together=set([('project', 'template')]),
        ),
        migrations.AlterUniqueTogether(
            name='projectbatchfile',
            unique_together=set([('batch_file', 'project')]),
        ),
    ]