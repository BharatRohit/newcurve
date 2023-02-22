import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [10.0, 30.50]
plt.rcParams["figure.autolayout"] = True
columns = ["FLOW","HEAD","EFF","NPSH"]
data = pd.read_csv("CSV.csv", usecols=columns)
# # print("Contents in csv file:
# # ", df)
# plt.subplot(df.FLOW, df.HEAD,)
# plt.subplot(df.FLOW, df.EFF,)
# plt.show()
fig, axs = plt.subplots(3, 1)

# axs[0].fill_between(data.index, data['FLOW'], data['HEAD'])
axs[0].fill_between(data.FLOW, data.HEAD)
axs[0].set_title("Flow vs Head")
axs[0].set_xlabel("flow(lps)")
axs[0].set_ylabel("head(m)")
axs[1].plot(data.FLOW, data.EFF)
axs[1].set_title("Flow vs EFF")
axs[1].set_xlabel("flow(lps)")
axs[1].set_ylabel("EFF")
axs[2].plot(data.FLOW, data.NPSH)
axs[2].set_title("Flow vs POWER")
axs[2].set_xlabel("flow(lps)")
axs[2].set_ylabel("POWER")

plt.show()