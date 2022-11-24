# Generated by Django 4.1.2 on 2022-11-24 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto_pt', '0002_alter_notify_name_alter_taskjob_expression_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskjob',
            name='name',
            field=models.CharField(default='', help_text='任务名称具有唯一性，修改任务时不要修改此项，如果确实需要修改此项，请删除后重新添加', max_length=16, verbose_name='任务名称'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taskjob',
            name='args',
            field=models.CharField(blank=True, help_text='执行代码所需要的参数。默认不需要填写，有需要填写参数的任务会特别说明', max_length=128, null=True, verbose_name='任务参数'),
        ),
        migrations.AlterField(
            model_name='taskjob',
            name='end_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='任务结束时间'),
        ),
        migrations.AlterField(
            model_name='taskjob',
            name='jitter',
            field=models.IntegerField(default=1200, editable=False, help_text='增强时间随机性', verbose_name='时间浮动参数'),
        ),
        migrations.AlterField(
            model_name='taskjob',
            name='job_id',
            field=models.CharField(editable=False, help_text='任务名称具有唯一性，修改任务时不要修改此项，如果确实需要修改此项，请删除后重新添加', max_length=16, unique=True, verbose_name='任务id'),
        ),
        migrations.AlterField(
            model_name='taskjob',
            name='misfire_grace_time',
            field=models.IntegerField(default=600, editable=False, help_text='强制执行结束的时间, 为避免撞车导致任务丢失, 没执行完就别执行了', verbose_name='任务运行时间'),
        ),
        migrations.AlterField(
            model_name='taskjob',
            name='start_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='任务开始时间'),
        ),
        migrations.AlterField(
            model_name='taskjob',
            name='task',
            field=models.ForeignKey(help_text='在这里选择你要执行的任务', on_delete=django.db.models.deletion.CASCADE, to='auto_pt.task', verbose_name='选择任务'),
        ),
    ]
