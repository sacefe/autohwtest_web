# Generated by Django 5.0.8 on 2024-08-13 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tdm', '0003_stations_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlowHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('serialnumber', models.CharField(db_index=True, max_length=20)),
                ('partnumber_id', models.IntegerField(db_index=True)),
                ('flow_name', models.CharField(max_length=20)),
                ('fprcess_Id', models.IntegerField()),
                ('fprocess_step', models.IntegerField()),
                ('flow_status', models.BooleanField()),
                ('employee_id', models.IntegerField()),
                ('date_arrival', models.DateTimeField(auto_now=True)),
                ('date_departure', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TestResulstAchieve',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('serialnumber', models.CharField(db_index=True, max_length=20)),
                ('partnumber_id', models.IntegerField(db_index=True)),
                ('fprocess_step', models.IntegerField(db_index=True)),
                ('station_id', models.IntegerField()),
                ('employee_id', models.IntegerField()),
                ('evidence_link', models.CharField(max_length=100)),
                ('test_id', models.IntegerField()),
                ('test_name', models.CharField(db_index=True, max_length=20)),
                ('spec_type', models.CharField(max_length=20)),
                ('max_value', models.CharField(max_length=20)),
                ('min_value', models.CharField(max_length=20)),
                ('expected_value', models.CharField(max_length=20)),
                ('result', models.CharField(max_length=20)),
                ('test_time', models.TimeField()),
                ('tc_outcome', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='testmatrix',
            old_name='flow_step',
            new_name='fprocess_step',
        ),
        migrations.RemoveField(
            model_name='testplan',
            name='operator',
        ),
        migrations.RemoveField(
            model_name='testplan',
            name='tolerance',
        ),
        migrations.AddField(
            model_name='stations',
            name='station_name',
            field=models.CharField(db_index=True, default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testplan',
            name='max_value',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testplan',
            name='min_value',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testplan',
            name='spec_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='testmatrix',
            unique_together={('partnumber_id', 'station_family', 'fprocess_step')},
        ),
        migrations.CreateModel(
            name='FlowMatrix',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('flow_name', models.CharField(db_index=True, max_length=20)),
                ('employee_id', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField()),
                ('partnumber_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tdm.partnumber')),
            ],
        ),
        migrations.CreateModel(
            name='FlowStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('serialnumber', models.CharField(db_index=True, max_length=20, unique=True)),
                ('flow_name', models.CharField(max_length=20)),
                ('fprcess_Id', models.IntegerField()),
                ('current_fprocess_step', models.IntegerField()),
                ('flow_status', models.BooleanField()),
                ('employee_id', models.IntegerField()),
                ('date_arrival', models.DateTimeField(auto_now=True)),
                ('date_departure', models.DateTimeField()),
                ('partnumber_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tdm.partnumber')),
            ],
        ),
        migrations.CreateModel(
            name='FlowTable',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('flow_name', models.CharField(db_index=True, max_length=20)),
                ('fprcess_Id', models.IntegerField()),
                ('fprocess_step', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField()),
            ],
            options={
                'unique_together': {('flow_name', 'fprcess_Id')},
            },
        ),
        migrations.CreateModel(
            name='TestResultsOverAll',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('serialnumber', models.CharField(db_index=True, max_length=20, unique=True)),
                ('overall_outcome', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('partnumber_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tdm.partnumber')),
            ],
        ),
        migrations.CreateModel(
            name='TestResultsProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('fprocess_step', models.IntegerField()),
                ('station_id', models.IntegerField()),
                ('process_outcome', models.BooleanField()),
                ('employee_id', models.IntegerField()),
                ('test_time', models.TimeField()),
                ('evidence_link', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('overall_TR_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tdm.testresultsoverall')),
            ],
        ),
        migrations.CreateModel(
            name='TestCaseResults',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('test_id', models.IntegerField()),
                ('test_name', models.CharField(max_length=20)),
                ('spec_type', models.CharField(max_length=20)),
                ('max_value', models.CharField(max_length=20)),
                ('min_value', models.CharField(max_length=20)),
                ('expected_value', models.CharField(max_length=20)),
                ('result', models.CharField(max_length=20)),
                ('tc_outcome', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('process_TR_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tdm.testresultsprocess')),
            ],
            options={
                'unique_together': {('test_id', 'test_name')},
            },
        ),
    ]
