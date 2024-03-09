# Generated by Django 4.2.10 on 2024-02-17 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=50)),
                ('descripcion_categoria', models.TextField(blank=True)),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_cedula', models.CharField(max_length=20, unique=True)),
                ('nombres', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Itemcarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_productos', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_productos', models.CharField(default='SOME STRING', max_length=100)),
                ('nombre_productos', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=0, max_digits=10)),
                ('fecha_ingreso', models.DateTimeField(default=django.utils.timezone.now)),
                ('cantidad', models.PositiveIntegerField(null=True)),
                ('descripcion', models.TextField(max_length=50)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_neto', models.IntegerField()),
                ('valor_total', models.DecimalField(decimal_places=0, max_digits=10)),
                ('Id_cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.clientes')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.productos')),
            ],
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datecompleted', models.DateTimeField(blank=True, null=True)),
                ('important', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_disponible', models.IntegerField()),
                ('cantidad_nueva', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.productos')),
            ],
        ),
    ]
