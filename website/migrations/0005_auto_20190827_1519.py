# Generated by Django 2.2.4 on 2019-08-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20190810_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sanpham',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sanpham_ten', models.CharField(max_length=200, verbose_name='Tên sản phẩm')),
                ('sanpham_duongdan', models.CharField(max_length=200, verbose_name='Đường dẫn hình ảnh')),
                ('sanpham_giatien', models.CharField(max_length=50, verbose_name='Giá tiền')),
            ],
        ),
        migrations.DeleteModel(
            name='MenuTop',
        ),
    ]