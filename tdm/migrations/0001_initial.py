# Generated by Django 5.0.8 on 2024-08-15 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlowHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('serialnumber', models.CharField(db_index=True, max_length=20)),
                ('partnumber', models.CharField(db_index=True, max_length=20)),
                ('flow_name', models.CharField(max_length=20)),
                ('fprocess_priority', models.IntegerField()),
                ('fprocess_step', models.CharField(db_index=True, max_length=20)),
                ('flow_status', models.BooleanField()),
                ('employee_id', models.IntegerField()),
                ('date_arrival', models.DateTimeField(auto_now=True)),
                ('date_departure', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for part numer', primary_key=True, serialize=False)),
                ('partnumber', models.CharField(db_index=True, max_length=20, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FlowProcessStep',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('fprocess_step', models.CharField(db_index=True, max_length=20, unique=True)),
                ('date_created', models.DateTimeField(blank=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecType',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('type', models.CharField(db_index=True, max_length=20)),
                ('date_created', models.DateTimeField(blank=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestResulstAchieve',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('serialnumber', models.CharField(db_index=True, max_length=20)),
                ('partnumber', models.CharField(db_index=True, max_length=20)),
                ('fprocess_step', models.CharField(db_index=True, max_length=20)),
                ('station_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=150)),
                ('evidence_link', models.CharField(max_length=100)),
                ('test_id', models.IntegerField()),
                ('test_name', models.CharField(db_index=True, max_length=100)),
                ('spec_type', models.CharField(max_length=20)),
                ('max_value', models.CharField(max_length=20)),
                ('min_value', models.CharField(max_length=20)),
                ('expected_value', models.CharField(max_length=20)),
                ('result', models.CharField(max_length=20)),
                ('test_time', models.TimeField(blank=True)),
                ('tc_outcome', models.BooleanField()),
                ('date_created', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FlowMatrix',
            fields=[
                ('partnumber_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tdm.partnumber')),
                ('flow_name', models.CharField(db_index=True, max_length=20)),
                ('employee_id', models.IntegerField()),
                ('date_created', models.DateTimeField(blank=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StationSiblings',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for stations', primary_key=True, serialize=False)),
                ('sibling_lname', models.CharField(db_index=True, max_length=20, unique=True)),
                ('date_created', models.DateTimeField(blank=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('fprocess_step_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tdm.flowprocessstep')),
            ],
        ),
        migrations.CreateModel(
            name='Stations',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for stations', primary_key=True, serialize=False)),
                ('station_name', models.CharField(db_index=True, max_length=20, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(blank=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('sibling_lname_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tdm.stationsiblings')),
            ],
        ),
        migrations.CreateModel(
            name='TestResultsOverAll',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('serialnumber', models.CharField(db_index=True, max_length=20, unique=True)),
                ('overall_outcome', models.BooleanField()),
                ('date_created', models.DateTimeField(blank=True)),
                ('partnumber_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tdm.partnumber')),
            ],
        ),
        migrations.CreateModel(
            name='TestResultsProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('station_id', models.IntegerField()),
                ('process_outcome', models.BooleanField()),
                ('employee_id', models.IntegerField()),
                ('test_time', models.TimeField(blank=True)),
                ('evidence_link', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(blank=True)),
                ('fprocess_step_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tdm.flowprocessstep')),
                ('overall_TR_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tdm.testresultsoverall')),
            ],
        ),
        migrations.CreateModel(
            name='FlowStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('serialnumber', models.CharField(db_index=True, max_length=20, unique=True)),
                ('flow_name', models.CharField(max_length=20)),
                ('fprocess_priority', models.IntegerField()),
                ('flow_status', models.BooleanField()),
                ('employee_id', models.IntegerField()),
                ('date_arrival', models.DateTimeField(auto_now=True)),
                ('date_departure', models.DateTimeField(blank=True)),
                ('curr_fprocess_step_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tdm.flowprocessstep')),
                ('partnumber_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tdm.partnumber')),
            ],
            options={
                'unique_together': {('flow_name', 'fprocess_priority')},
            },
        ),
        migrations.CreateModel(
            name='FlowTable',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('flow_name', models.CharField(db_index=True, max_length=20)),
                ('fprocess_priority', models.IntegerField()),
                ('date_created', models.DateTimeField(blank=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('fprocess_step_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tdm.flowprocessstep')),
            ],
            options={
                'unique_together': {('flow_name', 'fprocess_priority')},
            },
        ),
        migrations.CreateModel(
            name='TestMatrix',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('testplan_name', models.CharField(max_length=20)),
                ('employee_id', models.IntegerField()),
                ('date_created', models.DateTimeField(blank=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('partnumber_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tdm.partnumber')),
                ('sibling_lname_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tdm.stationsiblings')),
            ],
            options={
                'unique_together': {('partnumber_fk', 'sibling_lname_fk')},
            },
        ),
        migrations.CreateModel(
            name='TestPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('testplan_name', models.CharField(db_index=True, max_length=20)),
                ('group_id', models.IntegerField()),
                ('test_id', models.IntegerField()),
                ('test_name', models.CharField(max_length=100)),
                ('max_value', models.CharField(blank=True, max_length=20)),
                ('min_value', models.CharField(blank=True, max_length=20)),
                ('expected_value', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField(blank=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('spec_type_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tdm.spectype')),
            ],
            options={
                'unique_together': {('testplan_name', 'test_id')},
            },
        ),
        migrations.CreateModel(
            name='TestCaseResults',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='ID for test matrix', primary_key=True, serialize=False)),
                ('test_id', models.IntegerField()),
                ('test_name', models.CharField(max_length=100)),
                ('max_value', models.CharField(blank=True, max_length=20)),
                ('min_value', models.CharField(blank=True, max_length=20)),
                ('expected_value', models.CharField(max_length=20)),
                ('result', models.CharField(max_length=20)),
                ('tc_outcome', models.BooleanField()),
                ('date_created', models.DateTimeField(blank=True)),
                ('spec_type_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tdm.spectype')),
                ('process_TR_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tdm.testresultsprocess')),
            ],
            options={
                'unique_together': {('test_id', 'test_name')},
            },
        ),
    ]
