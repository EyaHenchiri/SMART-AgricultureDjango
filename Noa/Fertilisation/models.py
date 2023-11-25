from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Modéle_Variante(models.Model):
    CATEGORIE_CHOICES = [
        ('plante', 'Plante'),
        ('arbre', 'Arbre'),
        ('semis', 'Semis'),
    ]

    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)
    sous_categorie = models.CharField(max_length=200)
    nom_variante = models.CharField(max_length=200)
    nombre_etape = models.IntegerField()
    description = models.TextField()
    debut_saison = models.DateField()
    fin_saison = models.DateField()

    def __str__(self):
        return self.nom_variante


class Fertilisation(models.Model):
    Nom_Commercial = models.CharField(max_length=200)
    image = models.ImageField(upload_to= 'photos/%y/%m/%d')
    QuantiteTotal = models.FloatField()
    Quantite_H = models.FloatField()
    N = models.DecimalField(max_digits=5 , decimal_places=2)
    K2O = models.DecimalField(max_digits=5 , decimal_places=2)
    P2O5 = models.DecimalField(max_digits=5 , decimal_places=2)
    #created_at = models.DateTimeField(auto_now_add=True)
    #due_date = models.DateTimeField()
    Pour_Plante = models.BooleanField(default=False)
    Pour_Arbre = models.BooleanField(default=False)
    Pour_Semis = models.BooleanField(default=False)
    

    def __str__(self):
        return self.Nom_Commercial




class Etape(models.Model):
    ACTION_TERRE_CHOICES = [
        ('labourage', 'Labourage'),
        ('ameublissement', 'Ameublissement'),
        ('bbbbbb', 'bbbbbbb'),
        # Ajoutez d'autres actions si nécessaire
    ]

    variante = models.ForeignKey(Modéle_Variante, on_delete=models.CASCADE)
    nom_etape = models.CharField(max_length=200)
    periode_min = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    periode_max = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    action_sur_terre = models.CharField(max_length=20, choices=ACTION_TERRE_CHOICES)
    irrigation_quantite = models.FloatField(null=True, blank=True)
    irrigation_periode = models.CharField(max_length=200, null=True, blank=True)
    type_fertilisation = models.ForeignKey(Fertilisation, on_delete=models.SET_NULL, null=True, blank=True)
    type_fertilisation_quantite = models.FloatField(null=True, blank=True)
    type_fertilisation_periode = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='etapes/%y/%m/%d', null=True, blank=True)

    def __str__(self):
        return f"{self.variante.nom_variante} - Étape {self.nom_etape}"
