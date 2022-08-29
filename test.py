import time
import matplotlib.pyplot as plt

epoch = 20  #x軸の最大値
fig, axes = plt.subplots(nrows=1, ncols=2, sharex=False)   #プロットエリアの生成
loss, acc = [], []    #プロットする値を格納するリスト
ax_x_list = []


axes[0].set_xlim(0, epoch)    #loss, x軸の最大値を設定
axes[1].set_xlim(0, epoch)    #acc,  x軸の最大値を設定
ax_x_list.append(0)
loss.append(1)
acc.append(1)

lines_loss,  = axes[0].plot(ax_x_list, loss, '-ok')
lines_acc,  = axes[1].plot(ax_x_list, acc, '-ok')

for n in range(1, epoch):
    #ここにloss, acc取得コード
    ax_x_list.append(n)
    loss.append(1/n)
    acc.append(1/n)
    #ここまで取得コード
    time.sleep(2)

    axes[0].set_ylim(min(loss)-1, max(loss)+1)
    axes[1].set_ylim(min(acc)-1, max(acc)+1)

    lines_loss.set_data(ax_x_list, loss)
    lines_acc.set_data(ax_x_list, acc)
    plt.pause(0.01)

plt.show()
