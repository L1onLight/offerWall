from django.db import models


# Create your models here.

class Exclusion(models.Model):
    click_id = models.CharField(max_length=100, unique=True, primary_key=True)
    excluded_offers = models.CharField(max_length=255, null=True)

    def exclude_offer(self, offer_id: int):
        if not self.excluded_offers:
            self.excluded_offers = str(offer_id)
        else:
            ids = [int(i) for i in self.excluded_offers.split(",")]
            ids.append(offer_id)
            ids = sorted(set(ids))
            self.excluded_offers = ",".join(str(i) for i in ids)
