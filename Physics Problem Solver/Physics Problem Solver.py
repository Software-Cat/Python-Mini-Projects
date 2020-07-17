import math

class OneDimentionalMotion:
    def dispalcement(self, initial_pos, final_pos):
        return final_pos - initial_pos

    def average_velocity(self, displacement, time_interval):
        return displacement / float(time_interval)

    def average_speed(self, diatance_travelled, time_interval):
        return diatance_travelled / float(time_interval)

    def displacement(self, time_interval=None, initial_velocity=None, final_velocity=None, constant_acceleration=None):
        known_variables = {}
        if time_interval != None:
            known_variables['t'] = time_interval
        if initial_velocity != None:
            known_variables['initialV'] = initial_velocity
        if final_velocity != None:
            known_variables['finalV'] = final_velocity
        if constant_acceleration != None:
            known_variables['a'] = constant_acceleration

        if len(known_variables) < 3:
            raise ValueError('Not enough known variables to calculate the displacement (need at least 3 known variables, got ' + str(len(known_variables)))

        if 't' in known_variables and 'initialV' in known_variables and 'finalV' in known_variables: #Don't need acceleration
            return ((known_variables['initialV'] + known_variables['finalV']) / 2.0) * known_variables['t']
        if 't' in known_variables and 'initialV' in known_variables and 'a' in known_variables: #Don't need final velocity
            return known_variables['initialV'] * known_variables['t'] + (known_variables['a'] * known_variables['t'] ** 2) / 2.0
        if 'finalV' in known_variables and 'initialV' in known_variables and 'a' in known_variables: #Don't need time
            return ((known_variables['finalV'] ** 2 - known_variables['finalV'] ** 2) / 2.0) / float(known_variables['finalV'])
        if 'finalV' in known_variables and 't' in known_variables and 'a' in known_variables: #Don't need initial velocity
            return known_variables['finalV'] * known_variables['t'] - (known_variables['a'] * known_variables['t'] ** 2) / 2.0

    def time_interval(self, displacement=None, initial_velocity=None, final_velocity=None, constant_acceleration=None):
        known_variables = {}
        if displacement != None:
            known_variables['displacement'] = displacement
        if initial_velocity != None:
            known_variables['initialV'] = initial_velocity
        if final_velocity != None:
            known_variables['finalV'] = final_velocity
        if constant_acceleration != None:
            known_variables['a'] = constant_acceleration

        if len(known_variables) < 3:
            raise ValueError('Not enough known variables to calculate the time interval (need at least 3 known variables, got ' + str(len(known_variables)))

        if 'initialV' in known_variables and 'finalV' in known_variables and 'a' in known_variables: #Don't need displacement
            return (known_variables['finalV'] - known_variables['initialV']) / float(known_variables['a'])
        if 'displacement' in known_variables and 'finalV' in known_variables and 'initialV' in known_variables: #Don't need acceleration
            return known_variables['displacement'] / ((known_variables['finalV'] + known_variables['initialV']) / 2.0)
        if 'displacement' in known_variables and 'initialV' in known_variables and 'a' in known_variables: #Don't need final velocity
            a = known_variables['a'] / 2.0              #Using quadratic formula --> ax**2 + bx + c = 0, x = (-b +- sqrt(b**2 - 4ac)) / 2a
            b = known_variables['initialV']
            c = -known_variables['displacement']

            answers = []                                #There are two answers to  a quadratic equation
            answers.append((-b + math.sqrt(b**2 - 4 * a * c)) / 2.0 * a)
            answers.append((-b - math.sqrt(b**2 - 4 * a * c)) / 2.0 * a)
            return answers
        if 'displacement' in known_variables and 'finalV' in known_variables and 'a' in known_variables: #Don't need initial velocity
            a = -(known_variables['a'] / 2.0)           #Using quadratic formula --> ax**2 + bx + c = 0, x = (-b +- sqrt(b**2 - 4ac)) / 2a
            b = known_variables['finalV']
            c = -known_variables['displacement']

            answers = []                                #There are two answers to  a quadratic equation
            answers.append((-b + math.sqrt(b**2 - 4 * a * c)) / 2.0 * a)
            answers.append((-b - math.sqrt(b**2 - 4 * a * c)) / 2.0 * a)
            return answers

    def initial_velocity(self, displacement=None, time_interval=None, final_velocity=None, constant_acceleration=None):
        known_variables = {}
        if displacement != None:
            known_variables['displacement'] = displacement
        if time_interval != None:
            known_variables['t'] = time_interval
        if final_velocity != None:
            known_variables['finalV'] = final_velocity
        if constant_acceleration != None:
            known_variables['a'] = constant_acceleration

        if len(known_variables) < 3:
            raise ValueError('Not enough known variables to calculate the initial velocity (need at least 3 known variables, got ' + str(len(known_variables)))

        if 'finalV' in known_variables and 'a' in known_variables and 't' in known_variables: #Don't need displacement
            return known_variables['finalV'] - known_variables['a'] * known_variables['t']
        if 'displacement' in known_variables and 'finalV' in known_variables and 't' in known_variables: #Don't need acceleration
            return known_variables['displacement'] / float(known_variables['t']) * 2 - known_variables['finalV']
        if 'displacement' in known_variables and 't' in known_variables and 'a' in known_variables: #Don't need final velocity
            return (known_variables['displacement'] - 0.5 * known_variables['a'] * known_variables['t'] ** 2) / float(known_variables['t'])
        if 'finalV' in known_variables and 'a' in known_variables and 'displacement' in known_variables: #Don't need time
            answers = []                                #There are two answers to  a quadratic equation
            answers.append(math.sqrt(known_variables['finalV']**2 - 2 * known_variables['a'] * known_variables['displacement']))
            answers.append(-math.sqrt(known_variables['finalV']**2 - 2 * known_variables['a'] * known_variables['displacement']))
            return answers

    def final_velocity(self, displacement=None, time_interval=None, initial_velocity=None, constant_acceleration=None):
        known_variables = {}
        if displacement != None:
            known_variables['displacement'] = displacement
        if time_interval != None:
            known_variables['t'] = time_interval
        if initial_velocity != None:
            known_variables['initialV'] = initial_velocity
        if constant_acceleration != None:
            known_variables['a'] = constant_acceleration

        if len(known_variables) < 3:
            raise ValueError('Not enough known variables to calculate the final velocity (need at least 3 known variables, got ' + str(len(known_variables)))

        if 'initialV' in known_variables and 'a' in known_variables and 't' in known_variables: #Don't need displacement
            return known_variables['initialV'] + known_variables['a'] * known_variables['t']
        if 'displacement' in known_variables and 'initialV' in known_variables and 't' in known_variables: #Don't need acceleration
            return known_variables['displacement'] / float(known_variables['t']) * 2 - known_variables['initialV']
        if 'initialV' in known_variables and 'a' in known_variables and 'displacement' in known_variables: #Don't need time
            answers = []                                #There are two answers to  a quadratic equation
            
            
            













myCal = OneDimentionalMotion()
