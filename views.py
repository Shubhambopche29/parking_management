from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle

def index(request):
    if request.method == 'POST':
        # Get user input for vehicle details
        vehicle_number = request.POST.get('vehicle_number')

        # Get user input for vehicle type
        vehicle_type_choice = request.POST.get('vehicle_type')
        vehicle_type_map = {"1": "Bike", "2": "Car", "3": "Truck", "4": "Physically disabled"}
        vehicle_type = vehicle_type_map.get(vehicle_type_choice)

        contact_number = request.POST.get('contact_number')

        # Generate random ticket number
        ticket_chars = string.ascii_uppercase + string.digits
        ticket_number = ''.join(random.choice(ticket_chars) for _ in range(8))

        entry_time_str = request.POST.get('entry_time')
        entry_time = datetime.datetime.strptime(entry_time_str, '%Y-%m-%d %H:%M:%S')
        exit_time_str = request.POST.get('exit_time')
        exit_time = datetime.datetime.strptime(exit_time_str, '%Y-%m-%d %H:%M:%S')

        # Create Vehicle object and print receipt
        vehicle = Vehicle(vehicle_number=vehicle_number, vehicle_type=vehicle_type, contact_number=contact_number, ticket_number=ticket_number, entry_time=entry_time, exit_time=exit_time)
        vehicle.print_receipt()

        # Insert parking record into the database
        vehicle.save()

        # Render the receipt template with the vehicle object
        return render(request, 'receipt.html', {'vehicle': vehicle})
    else:
        # Render the index template with the form
        return render(request, 'index.html')

