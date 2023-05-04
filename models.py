from django.db import models

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=20)
    ticket_number = models.CharField(max_length=20)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField()

    def get_duration(self):
        return self.exit_time - self.entry_time

    def get_cost(self):
        duration = self.get_duration()
        total_hours = duration.total_seconds() / 3600
        total_cost = round(total_hours * 10, 2)
        return total_cost

    def print_receipt(self):
        total_cost = self.get_cost()

        print("--------------- Receipt ---------------")
        print(f"Vehicle Number)
