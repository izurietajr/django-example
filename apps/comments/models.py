from django.db import models


class Entity(models.Model):

    name = models.CharField(
        verbose_name='Nombre',
        max_length=100,
        null=False, blank=False
    )

    description = models.CharField(
        verbose_name='Descripción',
        max_length=500,
        null=True, blank=True
    )

    def __str__(self):
        return self.name


class Comment(models.Model):

    text = models.CharField(
        verbose_name="Comentario",
        max_length=500,
        null=False, blank=False
    )

    date = models.DateTimeField(
        verbose_name="Fecha",
        null=True, blank=True
    )

    entity = models.ForeignKey(
        to=Entity,
        related_name="comments",
        verbose_name="Entidad",
        null=False, blank=False,
        on_delete=models.CASCADE,
    )


class Score(models.Model):

    punctuation = models.IntegerField(
        verbose_name="Puntuación",
        null=False, blank=True
    )

    entity = models.ForeignKey(
        to=Entity,
        related_name="score_list",
        verbose_name="Entidad",
        null=False, blank=False,
        on_delete=models.CASCADE,
    )