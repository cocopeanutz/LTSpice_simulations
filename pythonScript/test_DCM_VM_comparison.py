from PyLTSpice import RawRead
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d


def interpolate(src_time, src_func, dst_time):
    f = interp1d(src_time, src_func, kind='linear')
    return f(dst_time)

averaging_model = RawRead("../test_DCM_VM.raw")
switching_model = RawRead("../test_DCM_VM_switching.raw")

print(averaging_model.get_trace_names())
print(averaging_model.get_raw_property())

y1 = averaging_model.get_trace("V(Vout)").get_wave()  # The Average Model
y2 = switching_model.get_trace("V(Vout)").get_wave()  #

time1 = averaging_model.get_trace('time').get_time_axis()  # Gets the time axis
time2 = switching_model.get_trace('time').get_time_axis()  # Gets the time axis

# Interpolate
y1 = interpolate(time1, y1, time2)
# y2 = interpolate(time2, y2, time1)

plt.plot(time2, y1, label="Averaged Model")
plt.plot(time2, y2, label="Switching Model")

plt.legend()  # order a legend
plt.show()
