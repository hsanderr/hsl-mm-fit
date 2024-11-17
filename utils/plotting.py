from matplotlib import pyplot as plt
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42


def plot_sensor(data, data_type, title='', filepath=None, size=(15, 6), overlay=True,
                use_timestamps=False):
    if data.shape[-1] == 5:
        data = data[:, (0, 2, 3, 4)]
    else:
        data = data[:, (0, 2)]

    if use_timestamps != False:
        data_x = data[:, 0] - data[0, 0]
    else:
        data_x = range(len(data))

    if data_type == 'acc':
        text = 'Accelerometer'
        ylabel = 'm/s^2'
    elif data_type == 'gyr':
        text = 'Gyroscope'
        ylabel = 'radians/s'
    elif data_type == 'mag':
        text = 'Magnetometer'
        ylabel = 'µT'
    elif data_type == 'hr':
        text = 'Heart Rate'
        ylabel = 'HR/min'
        overlay = True
    else:
        raise Exception('The data_type argument, {}, is not valid. Must be acc, gyr, mag, or hr'.format(data_type))

    if overlay:
        fig, ax = plt.subplots(1, 1, figsize=size, sharex=True)
        if data_type == 'hr':
            ax.plot(data_x, data[:, 1], 'r-')
        else:
            ax.plot(data_x, data[:, 1], 'r-', label='X')
            ax.plot(data_x, data[:, 2], 'g-', label='Y')
            ax.plot(data_x, data[:, 3], 'b-', label='Z')
        ax.set_ylabel(ylabel)
        ax.set_xlabel('Frame')
        if data_type != 'hr':
            ax.legend()
    else:
        fig, ax = plt.subplots(3, 1, figsize=size, sharex=True)
        ax[0].plot(data_x, data[:, 1], 'r-', label='X')
        ax[1].plot(data_x, data[:, 2], 'g-', label='Y')
        ax[2].plot(data_x, data[:, 3], 'b-', label='Z')
        ax[0].title.set_text(text + ' X-axis')
        ax[0].set_ylabel(ylabel)
        ax[1].title.set_text(text + ' Y-axis')
        ax[1].set_ylabel(ylabel)
        ax[2].title.set_text(text + ' Z-axis')
        ax[2].set_ylabel(ylabel)
        ax[2].set_xlabel('Frame')

    fig.suptitle(title, size=16)
    if filepath is not None:
        fig.savefig(filepath, bbox_inches='tight')
    plt.show()