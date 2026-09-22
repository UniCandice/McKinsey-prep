import numpy as np

# BatteryTest Class Exercise

# Create a class called BatteryTest and complete the following tasks:

# 1. Give each BatteryTest object two attributes:
#    - name
#    - voltage
#    Convert the supplied voltage data into a NumPy array.

# 2. Create a method called average_voltage()
#    that returns the average voltage.

# 3. Create a property called voltage_min_max
#    that returns a dictionary containing:
#    - the minimum voltage
#    - the maximum voltage

# 4. Create a method called below_threshold(threshold)
#    that returns all voltage values below a
#    user-specified threshold.

# 5. Create a method called count_below_threshold(threshold)
#    that returns how many voltage measurements are
#    below the threshold.

# 6. Create a method called normalize()
#    that transforms the voltage values using
#    min-max normalization:
#
#    x_normalized = (x - x_min) / (x_max - x_min)


class BatteryTest:
    def __init__(self, name, voltage):
        self.name = name
        self.voltage = np.array(voltage)

    def average_voltage(self):
        aver = np.mean(self.voltage)
        return aver

    @property
    def voltage_min_max(self):
        a = {
            'min': np.min(self.voltage),
            'max': np.max(self.voltage)
        }
        return a

    def below_threshold(self, threshold):
        return self.voltage[self.voltage < threshold]

    def count_below_threshold(self, threshold):
        return np.sum(self.voltage < threshold)

    def normalize(self):
        x_norm = (self.voltage - np.min(self.voltage)) / (np.max(self.voltage) - np.min(self.voltage))
        return x_norm


# Module-level Functions

# 7. Create a module-level function called create_test(name, voltage)
#    that creates and returns a BatteryTest object.

def create_test(name, voltage):
    return BatteryTest(name, voltage)


# 8. Create a module-level function called compare_max_voltage(test1, test2)
#    that compares the maximum voltage of two BatteryTest objects
#    and prints which battery has the higher maximum voltage.

def compare_max_voltage(test1, test2):
    V1 = test1.voltage_min_max['max']
    V2 = test2.voltage_min_max['max']

    if V1 > V2:
        print(f"{test1.name} has the highest maximum voltage")
    elif V1 < V2:
        print(f"{test2.name} has the highest maximum voltage")
    else:
        print(f"{test1.name} and {test2.name} have the same maximum voltage")


# 9. Create a module-level function called find_lowest_voltage(test)
#    that returns the minimum voltage of a BatteryTest object.

def find_lowest_voltage(test):
    return test.voltage_min_max['min']


# 10. Create a module-level function called get_voltage_shape(test)
#     that returns the shape of the voltage array as a list.

def get_voltage_shape(test):
    return list(test.voltage.shape)




    

