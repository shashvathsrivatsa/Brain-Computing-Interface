import AggregateData
import matplotlib.pyplot as plt

data = AggregateData.getData()

plt.plot(data)
plt.xlabel('Sample Number')
plt.ylabel('Voltage (μV)')
plt.show()
