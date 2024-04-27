from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now=True)
    descripcion = models.TextField(null=True)

    class Meta:
        db_table = 'tbl_categoria'

    def __str__(self):
        return self.nombre

class Projecto(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now=True)
    descripcion = models.TextField(null=True)
    pais_ubicacion_projecto = models.CharField(max_length=50)
    departamente_ubicacion_projecto = models.CharField(max_length=50)
    distrito_ubicacion_projecto = models.CharField(max_length=150)
    
    class Meta:
        db_table = 'tbl_projecto'
    
    def __str__(self):
        return self.nombre
    

class ProjectoImagen(models.Model):
    projecto = models.ForeignKey(Projecto,on_delete=models.RESTRICT)
    imagen = models.ImageField(upload_to ='galeria-projecto',blank=True)
    orden = models.IntegerField(default=1)
    fecha_registro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_projecto_imagen'
        verbose_name_plural = 'Imagenes del Projecto'
        verbose_name = 'Imagen del Projecto'

    def __str__(self):
        return str(self.imagen)

class CategoriaImagen(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    imagen = models.ImageField(upload_to='galeria-categoria',blank=True)
    orden = models.IntegerField(default=1)
    fecha_registro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_categoria_imagen'
        verbose_name_plural = 'Imagenes de las Categorias'

    def __str__(self):
        return str(self.imagen)

class Equipo(models.Model):
    nombre = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    facebook = models.CharField(max_length=250,null=True)
    twitter = models.CharField(max_length=250,null=True)
    linkedin = models.CharField(max_length=250,null=True)
    instagram = models.CharField(max_length=250,null=True)
    youtube = models.CharField(max_length=250,null=True)

    class Meta:
        db_table = 'tbl_equipo'
        verbose_name_plural = 'Equipo'

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    profesion = models.CharField(max_length=250)
    comentario = models.TextField(null=True)

    class Meta:
        db_table = 'tbl_cliente'

    def __str__(self):
        return self.nombre

class EquipoImagen(models.Model):
    equipo = models.ForeignKey(Equipo,on_delete=models.RESTRICT)
    imagen = models.ImageField(upload_to='galeria-equipo',blank=True)
    orden = models.IntegerField(default=1)
    fecha_registro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_equipo_imagen'
        verbose_name_plural = 'Imagenes del Equipo'

    def __str__(self):
        return str(self.imagen)

class ClienteImagen(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT)
    imagen = models.ImageField(upload_to='galeria-cliente',blank=True)
    orden = models.IntegerField(default=1)
    fecha_registro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_cliente_imagen'
        verbose_name_plural = 'Fotos del Cliente'

    def __str__(self):
        return str(self.imagen)

class InformacionIndex(models.Model):
    section_1_t1 = models.CharField(max_length=200)
    section_1_t2 = models.CharField(max_length=200)
    section_2_t1 = models.TextField(null=True)
    section_2_t2 = models.TextField(null=True)
    section_2_check1 = models.CharField(max_length=100)
    section_2_check2 = models.CharField(max_length=100)
    section_2_check3 = models.CharField(max_length=100)
    section_2_check4 = models.CharField(max_length=100)
    section_2_check5 = models.CharField(max_length=100)
    section_2_check6 = models.CharField(max_length=100)
    section_2_final = models.TextField(null=True)
    section_4_t1 = models.TextField(null=True)

    class Meta:
        db_table = 'tbl_info_index'

    def __str__(self):
        return self.section_1_t1