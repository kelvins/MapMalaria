from django.db import models

# Create your models here.
class CIDADE(models.Model):
    CID_CODIGO    = models.IntegerField(primary_key=True, unique=True)
    CID_NOME      = models.CharField(max_length=100, null=True)
    CID_UF        = models.CharField(max_length=2, null=True)
    CID_LATITUDE  = models.DecimalField(max_digits=10, decimal_places=8, null=True)
    CID_LONGITUDE = models.DecimalField(max_digits=10, decimal_places=8, null=True)

class SINTOMA(models.Model):
    SIT_CODIGO    = models.IntegerField(primary_key=True, unique=True)
    SIT_DESCRICAO = models.CharField(max_length=100, null=True)

class OCUPACAO(models.Model):
    OCU_CODIGO    = models.IntegerField(primary_key=True, unique=True)
    OCU_DESCRICAO = models.CharField(max_length=100, null=True)

class TRATAMENTO(models.Model):
    TRA_CODIGO    = models.IntegerField(primary_key=True, unique=True)
    TRA_DESCRICAO = models.CharField(max_length=250, null=True)

class GESTANTE(models.Model):
    GES_CODIGO    = models.IntegerField(primary_key=True, unique=True)
    GES_DESCRICAO = models.CharField(max_length=100, null=True)

class ESCOLARIDADE(models.Model):
    ESC_CODIGO    = models.IntegerField(primary_key=True, unique=True)
    ESC_DESCRICAO = models.CharField(max_length=100, null=True)

class EXAMERESULTADO(models.Model):
    EXR_CODIGO    = models.IntegerField(primary_key=True, unique=True)
    EXR_DESCRICAO = models.CharField(max_length=100, null=True)

class PACIENTE(models.Model):
	PAC_CODIGO       = models.AutoField(primary_key=True, unique=True)
	PAC_DTNASC       = models.DateField(null=True)
	PAC_SEXO         = models.CharField(max_length=1, null=True)
	PAC_RACA         = models.CharField(max_length=1, null=True)
	PAC_DTMALARIA    = models.DateField(null=True) 	
	CID_CODIGO_NOT   = models.ForeignKey(CIDADE, related_name='CID_NOT', null=True)
	CID_CODIGO_VIVE  = models.ForeignKey(CIDADE, related_name='CID_VIVE', null=True)
	CID_CODIGO_PEGOU = models.ForeignKey(CIDADE, related_name='CID_PEGOU', null=True)
	SIT_CODIGO       = models.ForeignKey(SINTOMA, null=True)
	PAC_DTSINTOMA    = models.DateField(null=True)
	TRA_CODIGO       = models.ForeignKey(TRATAMENTO, null=True)
	GES_CODIGO       = models.ForeignKey(GESTANTE, null=True)
	OCU_CODIGO       = models.ForeignKey(OCUPACAO, null=True)
	ESC_CODIGO       = models.ForeignKey(ESCOLARIDADE, null=True)
	EXR_CODIGO       = models.ForeignKey(EXAMERESULTADO, null=True)
	PAC_DTEXAME      = models.DateField(null=True)