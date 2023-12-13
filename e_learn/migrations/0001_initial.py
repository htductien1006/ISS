# Generated by Django 5.0 on 2023-12-13 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='De_Thi',
            fields=[
                ('ma_de_thi', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('ten_de_thi', models.CharField(blank=True, max_length=50, null=True)),
                ('trang_thai_de_thi', models.CharField(blank=True, max_length=20, null=True)),
                ('thoi_gian_bat_dau', models.DateField(blank=True, null=True)),
                ('thoi_gian_ket_thuc', models.DateField(blank=True, null=True)),
                ('hinh_thuc_de_thi', models.CharField(blank=True, max_length=20, null=True)),
                ('huong_dan_lam_bai', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'de_thi',
            },
        ),
        migrations.CreateModel(
            name='Khoa',
            fields=[
                ('ma_khoa', models.IntegerField(primary_key=True, serialize=False)),
                ('ten_khoa', models.CharField(max_length=50)),
                ('ma_truong_bo_mon', models.IntegerField()),
            ],
            options={
                'db_table': 'khoa',
            },
        ),
        migrations.CreateModel(
            name='Cau_Hoi',
            fields=[
                ('ma_cau_hoi', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('noi_dung_cau_hoi', models.CharField(max_length=100)),
                ('dap_an', models.CharField(max_length=100)),
                ('diem_so', models.IntegerField()),
                ('ma_de_thi', models.ForeignKey(db_column='ma_de_thi', on_delete=django.db.models.deletion.CASCADE, to='e_learn.de_thi')),
            ],
            options={
                'db_table': 'cau_hoi',
            },
        ),
        migrations.CreateModel(
            name='Giang_Vien',
            fields=[
                ('mscb', models.IntegerField(primary_key=True, serialize=False)),
                ('ho_ten', models.CharField(max_length=50)),
                ('ngay_sinh', models.DateField()),
                ('gioi_tinh', models.CharField(max_length=30)),
                ('sdt', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('ma_khoa', models.ForeignKey(db_column='ma_khoa', on_delete=django.db.models.deletion.CASCADE, to='e_learn.khoa')),
            ],
            options={
                'db_table': 'giang_vien',
            },
        ),
        migrations.CreateModel(
            name='Khoa_Hoc',
            fields=[
                ('ma_khoa_hoc', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('ten_khoa_hoc', models.CharField(max_length=50)),
                ('mo_ta_khoa_hoc', models.CharField(max_length=100)),
                ('hoc_ki', models.CharField(max_length=20)),
                ('so_tin_chi', models.IntegerField()),
                ('noi_dung', models.CharField(max_length=100)),
                ('ma_khoa', models.ForeignKey(db_column='ma_khoa', on_delete=django.db.models.deletion.CASCADE, to='e_learn.khoa')),
                ('mscb', models.ForeignKey(db_column='mscb', on_delete=django.db.models.deletion.CASCADE, to='e_learn.giang_vien')),
            ],
            options={
                'db_table': 'khoa_hoc',
            },
        ),
        migrations.AddField(
            model_name='de_thi',
            name='ma_khoa_hoc',
            field=models.ForeignKey(db_column='ma_khoa_hoc', on_delete=django.db.models.deletion.CASCADE, to='e_learn.khoa_hoc'),
        ),
        migrations.CreateModel(
            name='Sinh_Vien',
            fields=[
                ('mssv', models.IntegerField(primary_key=True, serialize=False)),
                ('ho_ten', models.CharField(max_length=50)),
                ('ngay_sinh', models.DateField()),
                ('gioi_tinh', models.CharField(max_length=30)),
                ('sdt', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('trang_thai', models.CharField(max_length=30)),
                ('ma_khoa', models.ForeignKey(db_column='ma_khoa', on_delete=django.db.models.deletion.CASCADE, to='e_learn.khoa')),
            ],
            options={
                'db_table': 'sinh_vien',
            },
        ),
        migrations.CreateModel(
            name='Diem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diem', models.IntegerField()),
                ('trang_thai', models.CharField(max_length=20)),
                ('ma_de_thi', models.ForeignKey(db_column='ma_de_thi', on_delete=django.db.models.deletion.CASCADE, to='e_learn.de_thi')),
                ('mssv', models.ForeignKey(db_column='mssv', on_delete=django.db.models.deletion.CASCADE, to='e_learn.sinh_vien')),
            ],
            options={
                'db_table': 'diem',
                'unique_together': {('ma_de_thi', 'mssv')},
            },
        ),
        migrations.CreateModel(
            name='Dang_Ky',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ma_khoa_hoc', models.ForeignKey(db_column='ma_khoa_hoc', on_delete=django.db.models.deletion.CASCADE, to='e_learn.khoa_hoc')),
                ('mssv', models.ForeignKey(db_column='mssv', on_delete=django.db.models.deletion.CASCADE, to='e_learn.sinh_vien')),
            ],
            options={
                'db_table': 'dang_ky',
                'unique_together': {('mssv', 'ma_khoa_hoc')},
            },
        ),
    ]
