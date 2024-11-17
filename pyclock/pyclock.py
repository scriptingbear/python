#Call time.get_clock_info() for the 4 different clock types discussed
#in the lecture: 'clock', 'monotonic', 'perf_counter', 'process_time'

import time

#declare list of name spaces in object returned by time.get_clock_info()
clock_types = ['clock', 'monotonic', 'perf_counter', 'process_time', 'time']

#declare list of clock types
clock_attributes = ['adjustable', 'implementation', 'monotonic', 'resolution']

print('{:=^80}'.format('WELCOME TO THE PYCLOCK™ SYSTEM CLOCK REPORT!'))

for clock_type in clock_types:
    print('CLOCK TYPE: {}'.format(clock_type))
    clock_info = time.get_clock_info(clock_type)
    for clock_attribute in clock_attributes:
        print('\t{}: {}'.format(clock_attribute.capitalize(), getattr(clock_info, \
                                                       clock_attribute)))
    print()
