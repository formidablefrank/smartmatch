from django.db import models

# Create your models here.
class Organ(models.Model):
    name = models.CharField(unique = True, max_length = 10)
    description = models.CharField(max_length = 50, default = 'desc')
    #organ attributes here

    def __unicode__(self):
        return self.name

class PersonType(models.Model):
    name = models.CharField(max_length = 10)
    description = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.name

class Matcher(models.Model):
    def pointSystem(self,patient):
      point = 0

      if patient.reactiveAntibodies >= 50:
        point = point + 4
      elif patient.reactiveAntibodies < 50:
        point = point + 2

      if patient.enrollmentDate > 3:
        point = point + 4
      elif  patient.enrollmentDate > 2 and patient.enrollmentDate <= 3:
        point = point + 3
      elif  patient.enrollmentDate > 1 and patient.enrollmentDate <= 2:
        point = point + 2
      elif patient.enrollmentDate <= 1:
        point = point + 1

      if patient.age < 18:
        point = point + 2
      elif patient.age >= 19 and patient.age <= 65:
        point = point + 1
      else:
        point = point

      if patient.prevKidneyDonor == True:
          point = point + 15

      print 'point ' + str(point)

      return point

    def isCompatible(self, patient, donor):
        if patient.hla == donor.hla and patient.blood == donor.blood:
          print "Hello"
          pt = self.pointSystem(patient)
          print 'pt ' + str(pt)
          return pt
        else:
          return -1

    def getMatches(self):
        data = []
        sumthing = Person.objects.filter(person_type__name='donor')
        print len(sumthing)
        for donor in sumthing:
            # donor = {'donor': donor}
            donorxrecip = []
            match_list = []
            donordict = {'donor' : donor.name, 'organ' : donor.organ.name }
            for recipient in Person.objects.filter(person_type__name='recipient'):
                okay = self.isCompatible(recipient, donor)
                print 'okay ' + str(okay)
                if okay > 0:
                    #if okay compute for points
                    row = {'recipient': recipient.name, 'id': recipient.id, 'score': okay, 'contact_cell': recipient.contact}
                    match_list.append(row)
                    match_list = sorted(match_list, key=lambda key: key['score'], reverse=True)
                else:
                    print('not okay')
            donorxrecip.append(donordict)
            donorxrecip.append(match_list)
            data.append(donorxrecip)
        return data #data[Donor X Recipient][Donor / Recipient] [Recipients]

class Person(models.Model):
    name = models.CharField(max_length = 50, default = '')
    hla = models.CharField(max_length = 20, default = '')
    age = models.IntegerField(default = 0)
    weight = models.DecimalField(decimal_places = 2, max_digits = 5, default = 0)
    blood = models.CharField(max_length = 5, default = '')
    contact = models.IntegerField(default = 0)
    date = models.DateTimeField(auto_now_add = True)
    enrollmentDate = models.IntegerField(default = 0)
    organ = models.ForeignKey(Organ)
    person_type = models.ForeignKey(PersonType)
    reactiveAntibodies = models.DecimalField(decimal_places = 2, max_digits = 5,default = 0)
    prevKidneyDonor = models.BooleanField(default = False)

    def __unicode__(self):
        return unicode(self.person_type)

class User(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 100)

    def __unicode__(self):
        return unicode(self.username)
