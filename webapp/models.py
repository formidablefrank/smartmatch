from django.db import models

# Create your models here.
class Organ(models.Model):
    name = models.CharField(unique = True, max_length = 10)
    description = models.CharField(max_length = 50, default = 'desc')
    #organ attributes here

class PersonType(models.Model):
    name = models.CharField(max_length = 10)
    description = models.CharField(max_length = 50)

class Matcher(models.Model):
    def isHlaOk(patient, donor):
        return patient.hla - donor.hla

    def isAgeOk(patient, donor):
        return patient.age - donor.age

    def isWeightOk(patient, donor):
        return patient.weight - donor.weight

    def isBloodOk(patient, donor):
        return patient.blood == donor.blood

    def isOrganOk(patient, donor):
        return patient.organ.name == donor.organ.name

    def match(patient, donor):
        #more error, less priority
        if isBloodOk and isOrganOk:
            #return
            return isHlaOk + isAgeOk + isWeightOk
        else:
            return -1

    def getMatches():
        match_list = []
        for recipient in Person.objects.filter(person_type__name='recipient'):
            for donor in Person.objects.filter(person_type__name='donor'):
                okay = self.match(recipient, donor)
                if okay:
                    row = {'recipient': recipient, 'donor': donor, 'error': okay}
                    match_list.append(row)
                else:
                    print('not okay')
        return match_list


class Person(models.Model):
    name = models.CharField(max_length = 50)
    hla = models.CharField(max_length = 20)
    age = models.IntegerField(default = 0)
    weight = models.DecimalField(decimal_places = 2, max_digits = 5)
    blood = models.CharField(max_length = 5)
    contact = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)
    organ = models.ForeignKey(Organ)
    person_type = models.ForeignKey(PersonType)

class User(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 100)
