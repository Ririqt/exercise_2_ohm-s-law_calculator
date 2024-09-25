def voltage_formula(current, resistance):
    return current * resistance

def current_formula(voltage, resistance):
    if resistance == 0:
        raise ZeroDivisionError("Sorry, Resistance cannot be Zero.")
    return voltage / resistance

def resistance_formula(voltage, current):
    