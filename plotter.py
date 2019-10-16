"""
==================
Embedding in wx #5
==================

"""

import wx
import wx.lib.agw.aui as aui
import wx.lib.mixins.inspection as wit

import matplotlib as mpl
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.widgets import Slider
import numpy as np
import time


class Plot(wx.Panel):
    def __init__(self, parent, id=-1, dpi=None, **kwargs):
        wx.Panel.__init__(self, parent, id=id, **kwargs)
        self.figure = mpl.figure.Figure(dpi=dpi, figsize=(2, 2))
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()
        self.timeslider = wx.Slider(self, value=100, minValue=0, maxValue=100, name='time')
        self.zoomslider = wx.Slider(self, value=50, minValue=2, maxValue=50, name='zoom')

        self.timeslider.Bind(wx.EVT_SLIDER, self.OnSliderScrolltime)
        self.zoomslider.Bind(wx.EVT_SLIDER, self.OnSliderScrollzoom)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 5, wx.EXPAND)
        sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        sizer.Add(self.timeslider, 0, wx.EXPAND)
        sizer.Add(self.zoomslider, 0, wx.EXPAND)
        self.SetSizer(sizer)

    def OnSliderScrolltime(self, event):
        pass

    def OnSliderScrollzoom(self, event):
        pass


class PlotNotebook(wx.Panel):
    def __init__(self, parent, id=-1, *args, **kwargs):
        wx.Panel.__init__(self, parent, id=id, *args, **kwargs)
        self.nb = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        sizer = wx.BoxSizer()
        sizer.Add(self.nb, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def add(self, name="plot"):
        page = Plot(self.nb)
        self.nb.AddChild(page, name, wx.NB_LEFT)
        return page.figure


class live_plot(Plot):
    def __init__(self, parent, id=-1, dpi=None, data_file=None, **kwargs):
        super(live_plot, self).__init__(parent, id=id, dpi=dpi, **kwargs)
        self.zval = 50
        self.tval = 1
        self.data_file = data_file
        axes1 = self.figure.gca()

        DATA_FILE = self.data_file

        style.use('fivethirtyeight')
        self.fig = self.figure
        self.ax1 = axes1
        # self.fig.subplots_adjust(bottom=0.25)

        graph_data = open(DATA_FILE, 'r').read()
        lines = graph_data.split('\n')
        self.xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                self.xs.append(float(x))
                ys.append(float(y))
        self.ax1.clear()
        self.l, = self.ax1.plot(self.xs, ys)

        # axcolor = 'lightgoldenrodyellow'
        # self.axzoom = plt.axes([0.2, 0.02, 0.5, 0.04], facecolor=axcolor)
        # # Slider
        # self.szoom = Slider(self.axzoom, 'zoom', 5, 50, valinit=20, valstep=1)
        #
        # self.axtime = plt.axes([0.2, 0.08, 0.5, 0.04], facecolor=axcolor)
        # # Slider
        # self.stime = Slider(self.axtime, 'time', 0, 1, valinit=1, valstep=0.1)

        # Animation controls
        self.is_manual = False  # True if user has taken control of the animation
        interval = 100  # ms, time between animation frames

        def update_slider(val):
            self.is_manual = True
            update_plot(val)

        def update(val):
            # update curve
            # l.set_ydata(val*np.sin(t))
            # redraw canvas while idle
            self.fig.canvas.draw_idle()

        def update_plot(num):
            if self.is_manual:
                return self.l,  # don't change

            # val = (samp.val + scale) % samp.valmax
            # zval = self.szoom.val
            # tval = self.stime.val
            # self.szoom.set_val(zval)
            # self.stime.set_val(tval)
            self.animate(0, self.tval, self.zval)
            self.is_manual = False  # the above line called update_slider, so we need to reset this
            return self.l,


        def on_click(event):
            # Check where the click happened
            # (xm, ym), (xM, yM) = self.szoom.label.clipbox.get_points()
            # (xt, yt), (xT, yT) = self.stime.label.clipbox.get_points()
            # if (xm < event.x < xM and ym < event.y < yM) or (xt < event.x < xT and yt < event.y < yT):
            #     # Event happened within the slider, ignore since it is handled in update_slider
            #     self.is_manual = False
            # else:
            # user clicked somewhere else on canvas = unpause
            self.is_manual = True

        # self.szoom.on_changed(update_slider)
        # self.stime.on_changed(update_slider)

        self.fig.canvas.mpl_connect('button_press_event', on_click)

        self.ani = animation.FuncAnimation(self.fig, update_plot, interval=interval)

        # axes1

    def animate(self, i, time, zoom):
        try:
            graph_data = open(self.data_file, 'r').read()
            lines = graph_data.split('\n')
            self.xs = []
            ys = []
            for line in lines:
                if len(line) > 1:
                    x, y = line.split(',')
                    self.xs.append(float(x))
                    ys.append(float(y))
            self.ax1.clear()
            self.ax1.plot(self.xs, ys)
            self.is_manual = False

            try:
                self.ax1.set_xlim(time * np.ceil(self.xs[-1]) - zoom, time * np.ceil(self.xs[-1]))
            except:
                pass
            return self.l
        except:
            pass

    def OnSliderScrolltime(self, e):
        obj = e.GetEventObject()
        self.tval = obj.GetValue() / 100

    def OnSliderScrollzoom(self, e):
        obj = e.GetEventObject()
        self.zval = obj.GetValue()


class main_frame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(main_frame, self).__init__(parent, *args, **kwargs)
        self.panel1 = live_plot(self, -1, style=wx.SUNKEN_BORDER, data_file='example.txt')
        self.mainsizer = wx.BoxSizer()
        self.mainsizer.Add(self.panel1, 1, wx.EXPAND)
        self.SetAutoLayout(True)
        self.SetSizer(self.mainsizer)
        self.Layout()
        self.Center()
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = main_frame(None, title="huji rocketry club", size=(500, 500), )
    app.MainLoop()
