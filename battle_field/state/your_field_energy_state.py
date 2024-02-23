class YourFieldEnergyState:
    def __init__(self):
        self.your_field_energy_count = 0

    def increase_field_energy(self, count):
        self.your_field_energy_count += count

    def decrease_field_energy(self, count):
        self.your_field_energy_count -= count

    def get_your_field_energy_count(self):
        return self.your_field_energy_count
