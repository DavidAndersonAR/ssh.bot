# Generated by Django 4.2.9 on 2024-01-08 19:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('acesso_ssh', '0003_tabelaarp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tabelaarp',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='tabelaarp',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ShowRuning',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comando', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acesso_ssh.ativoenel')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ShowMacAddres',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comando', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acesso_ssh.ativoenel')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ShowLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comando', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acesso_ssh.ativoenel')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ShowIpOsNei',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comando', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acesso_ssh.ativoenel')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ShowInterTran',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comando', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acesso_ssh.ativoenel')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ShowIntDes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comando', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acesso_ssh.ativoenel')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ShowInStatus',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comando', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acesso_ssh.ativoenel')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ShowCdpNeiDet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comando', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acesso_ssh.ativoenel')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ShowBgpSu',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comando', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acesso_ssh.ativoenel')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]