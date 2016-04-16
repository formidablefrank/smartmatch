# smartmatch

kidney = Organ.objects.get(name='kidney')
donor = PersonType.objects.get(name='donor')
liver = Organ.objects.get(name='liver')
rec = PersonType.objects.get(name='recipient')
p1 = Person.objects.create(name='AA', hla='hla-a', age=19, weight=86, blood='a', enrollmentDate=3, organ=kidney, person_type=donor)
p2 = Person.objects.create(name='AA', hla='hla-a', age=19, weight=86, blood='a', enrollmentDate=3, organ=kidney, person_type=rec)

from webapp.models import *
Person.objects.all().delete()
kidney = Organ.objects.get(name='kidney')
donor = PersonType.objects.get(name='donor')
liver = Organ.objects.get(name='liver')
rec = PersonType.objects.get(name='recipient')
p1 = Person.objects.create(name='BB', hla='hla-a', age=19, weight=86, blood='a', enrollmentDate=3, organ=kidney, person_type=donor)
p2 = Person.objects.create(name='AA', hla='hla-a', age=19, weight=86, blood='a', enrollmentDate=3, organ=kidney, person_type=rec)
p3 = Person.objects.create(name='CC', hla='hla-a', age=19, weight=86, blood='a', enrollmentDate=3, organ=kidney, person_type=donor)
p4 = Person.objects.create(name='DD', hla='hla-a', age=17, weight=86, blood='a', enrollmentDate=3, organ=kidney, person_type=rec, prevKidneyDonor=True)
p5 = Person.objects.create(name='EE', hla='hla-a', age=19, weight=86, blood='b', enrollmentDate=3, organ=kidney, person_type=rec)
m = Matcher()
m.getMatches()
