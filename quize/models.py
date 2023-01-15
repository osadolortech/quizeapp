from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=125, verbose_name="")

    def __str__(self):
        return self.name


class Quizes(models.Model):

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ["id"]
    title = models.CharField(max_length=125, default= _("New qiuze"), verbose_name= _('Quize title'))
    category = models.ForeignKey(Category,default=1, on_delete=models.DO_NOTHING, related_name="quize")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("last updated"))

    def __str__(self):
        return self.title
    
class Updated(models.Model):
    updated_at = models.DateTimeField(auto_now=True,)

    class Meta:
        abstract = True

class Quesion(Updated):

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ["id"]

    SCALE = (
        (0, _("Fundamentals")),
        (1, _("Beginner")),
        (2, _("Intermediate")),
        (3, _("Advance")),
        (4, _("Expert")),
    )
    Type = (
        (0,_("Multi Choice")),
    )
    quize = models.ForeignKey(Quizes, on_delete=models.DO_NOTHING, related_name="question")
    technique = models.IntegerField(choices=Type,default=0,verbose_name=_("Type of Question"))
    title = models.CharField(max_length=125,verbose_name=_("title"))
    difficuty = models.IntegerField(choices=SCALE,default=0, verbose_name=_("Difficult"))
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Answers(Updated):

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ["id"]
    question = models.ForeignKey(Quesion,on_delete=models.DO_NOTHING,related_name="answers")
    answer_text = models.CharField(max_length=125,verbose_name=_("Answer_text"))
    is_right = models.BooleanField(default=False,)
