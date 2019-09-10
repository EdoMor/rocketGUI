import numpy as np
import OpenGL
import numpy
import wx
import plotter as plt
import wx_obj_canvas as glc
from text_panels import numbers_panel
from text_panels import systems_check_list
from text_panels import video_panel


class main_frame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(main_frame, self).__init__(parent, *args, **kwargs)
        self.box_left_sizer = wx.BoxSizer(wx.VERTICAL)
        self.box3sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.box_right_sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel1 = plt.Plot(self, -1, style=wx.SUNKEN_BORDER)
        axes1 = self.panel1.figure.gca()
        axes1.plot([1, 2, 3], [2, 1, 4])
        self.panel2 = plt.Plot(self, -1, style=wx.SUNKEN_BORDER)
        axes2 = self.panel2.figure.gca()
        axes2.plot([3, 2, 1], [2, 1, 4])
        self.panel3 = plt.Plot(self, -1, style=wx.SUNKEN_BORDER)
        axes3 = self.panel3.figure.gca()
        axes3.plot([1, 2, 3], [1, 2, 3])
        self.panel4 = glc.GL_Canvas(self)  # , -1, style=wx.SUNKEN_BORDER)
        self.panel5 = numbers_panel(self, -1, style=wx.SUNKEN_BORDER)
        self.panel6 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        self.panel7 = systems_check_list(self, -1, style=wx.SUNKEN_BORDER)
        self.mainset = 7

        self.sizer1 = wx.BoxSizer()
        self.sizer2 = wx.BoxSizer()
        self.sizer3 = wx.BoxSizer()
        self.sizer4 = wx.BoxSizer()
        self.sizer5 = wx.BoxSizer()
        self.sizer6 = wx.BoxSizer()
        self.sizer7 = wx.BoxSizer()

        self.sizer1.Add(self.panel1, 1, wx.EXPAND)
        self.sizer2.Add(self.panel2, 1, wx.EXPAND)
        self.sizer3.Add(self.panel3, 1, wx.EXPAND)
        self.sizer4.Add(self.panel4, 1, wx.EXPAND)
        self.sizer5.Add(self.panel5, 1, wx.EXPAND)
        self.sizer6.Add(self.panel6, 1, wx.EXPAND)
        self.sizer7.Add(self.panel7, 1, wx.EXPAND)

        self.mainsizer.Add(self.box3sizer, 1, wx.EXPAND)
        self.box3sizer.AddMany(
            [(self.box_left_sizer, 1, wx.EXPAND), (self.sizer7, 3, wx.EXPAND), (self.box_right_sizer, 1, wx.EXPAND)])
        self.box_left_sizer.AddMany(
            [(self.sizer1, 1, wx.EXPAND), (self.sizer2, 1, wx.EXPAND), (self.sizer3, 1, wx.EXPAND), ])
        self.box_right_sizer.AddMany(
            [(self.sizer4, 1, wx.EXPAND), (self.sizer5, 1, wx.EXPAND), (self.sizer6, 1, wx.EXPAND), ])

        self.panel1.canvas.Bind(wx.EVT_LEFT_DCLICK, self.onClick1)
        self.panel2.canvas.Bind(wx.EVT_LEFT_DCLICK, self.onClick2)
        self.panel3.canvas.Bind(wx.EVT_LEFT_DCLICK, self.onClick3)
        self.panel4.Bind(wx.EVT_LEFT_DCLICK, self.onClick4)
        self.panel5.Bind(wx.EVT_LEFT_DCLICK, self.onClick5)
        self.panel6.Bind(wx.EVT_LEFT_DCLICK, self.onClick6)
        self.panel7.Bind(wx.EVT_LEFT_DCLICK, self.onClick7)

        self.SetAutoLayout(True)
        self.SetSizer(self.mainsizer)
        self.Layout()
        self.Center()
        self.Show()

    def cleanall(self):
        self.mainsizer.Show(self.box3sizer, show=False)
        # self.mainsizer.Clear(delete_windows=False)
        self.box_left_sizer.Detach(self.sizer1)
        self.box_left_sizer.Detach(self.sizer2)
        self.box_left_sizer.Detach(self.sizer3)
        self.box_left_sizer.Detach(self.sizer4)
        self.box_left_sizer.Detach(self.sizer5)
        self.box_left_sizer.Detach(self.sizer6)
        self.box_left_sizer.Detach(self.sizer7)
        self.box_right_sizer.Detach(self.sizer1)
        self.box_right_sizer.Detach(self.sizer2)
        self.box_right_sizer.Detach(self.sizer3)
        self.box_right_sizer.Detach(self.sizer4)
        self.box_right_sizer.Detach(self.sizer5)
        self.box_right_sizer.Detach(self.sizer6)
        self.box_right_sizer.Detach(self.sizer7)
        self.box3sizer.Detach(self.box_right_sizer)
        self.box3sizer.Detach(self.box_left_sizer)
        self.box3sizer.Detach(self.sizer1)
        self.box3sizer.Detach(self.sizer2)
        self.box3sizer.Detach(self.sizer3)
        self.box3sizer.Detach(self.sizer4)
        self.box3sizer.Detach(self.sizer5)
        self.box3sizer.Detach(self.sizer6)
        self.box3sizer.Detach(self.sizer7)
        self.mainsizer.Detach(self.box3sizer)

    def onClick1(self, event):
        if not self.mainset == 1:
            self.cleanall()
            self.mainsizer.Add(self.box3sizer, 1, wx.EXPAND)
            self.box3sizer.AddMany(
                [(self.box_left_sizer, 1, wx.EXPAND), (self.sizer1, 3, wx.EXPAND),
                 (self.box_right_sizer, 1, wx.EXPAND)])
            self.box_left_sizer.AddMany(
                [(self.sizer2, 1, wx.EXPAND), (self.sizer3, 1, wx.EXPAND), (self.sizer4, 1, wx.EXPAND), ])
            self.box_right_sizer.AddMany(
                [(self.sizer5, 1, wx.EXPAND), (self.sizer6, 1, wx.EXPAND), (self.sizer7, 1, wx.EXPAND), ])
            self.mainsizer.Show(self.box3sizer, show=True)
            self.mainset = 1
        else:
            pass
        self.Layout()
        print('ouch!')

    def onClick2(self, event):
        if not self.mainset == 2:
            self.cleanall()
            self.mainsizer.Add(self.box3sizer, 1, wx.EXPAND)
            self.box3sizer.AddMany(
                [(self.box_left_sizer, 1, wx.EXPAND), (self.sizer2, 3, wx.EXPAND),
                 (self.box_right_sizer, 1, wx.EXPAND)])
            self.box_left_sizer.AddMany(
                [(self.sizer1, 1, wx.EXPAND), (self.sizer3, 1, wx.EXPAND), (self.sizer4, 1, wx.EXPAND), ])
            self.box_right_sizer.AddMany(
                [(self.sizer5, 1, wx.EXPAND), (self.sizer6, 1, wx.EXPAND), (self.sizer7, 1, wx.EXPAND), ])
            self.mainsizer.Show(self.box3sizer, show=True)
            self.mainset = 2
        else:
            pass
        self.Layout()
        print('ouch!')

    def onClick3(self, event):
        if not self.mainset == 3:
            self.cleanall()
            self.mainsizer.Add(self.box3sizer, 1, wx.EXPAND)
            self.box3sizer.AddMany(
                [(self.box_left_sizer, 1, wx.EXPAND), (self.sizer3, 3, wx.EXPAND),
                 (self.box_right_sizer, 1, wx.EXPAND)])
            self.box_left_sizer.AddMany(
                [(self.sizer1, 1, wx.EXPAND), (self.sizer2, 1, wx.EXPAND), (self.sizer4, 1, wx.EXPAND), ])
            self.box_right_sizer.AddMany(
                [(self.sizer5, 1, wx.EXPAND), (self.sizer6, 1, wx.EXPAND), (self.sizer7, 1, wx.EXPAND), ])
            self.mainsizer.Show(self.box3sizer, show=True)
            self.mainset = 3
        else:
            pass
        self.Layout()
        print('ouch!')

    def onClick4(self, event):
        if not self.mainset == 4:
            self.cleanall()
            self.mainsizer.Add(self.box3sizer, 1, wx.EXPAND)
            self.box3sizer.AddMany(
                [(self.box_left_sizer, 1, wx.EXPAND), (self.sizer4, 3, wx.EXPAND),
                 (self.box_right_sizer, 1, wx.EXPAND)])
            self.box_left_sizer.AddMany(
                [(self.sizer1, 1, wx.EXPAND), (self.sizer2, 1, wx.EXPAND), (self.sizer3, 1, wx.EXPAND), ])
            self.box_right_sizer.AddMany(
                [(self.sizer5, 1, wx.EXPAND), (self.sizer6, 1, wx.EXPAND), (self.sizer7, 1, wx.EXPAND), ])
            self.mainsizer.Show(self.box3sizer, show=True)
            self.mainset = 4
        else:
            pass
        self.Layout()
        print('ouch!')

    def onClick5(self, event):
        if not self.mainset == 5:
            self.cleanall()
            self.mainsizer.Add(self.box3sizer, 1, wx.EXPAND)
            self.box3sizer.AddMany(
                [(self.box_left_sizer, 1, wx.EXPAND), (self.sizer5, 3, wx.EXPAND),
                 (self.box_right_sizer, 1, wx.EXPAND)])
            self.box_left_sizer.AddMany(
                [(self.sizer1, 1, wx.EXPAND), (self.sizer2, 1, wx.EXPAND), (self.sizer3, 1, wx.EXPAND), ])
            self.box_right_sizer.AddMany(
                [(self.sizer4, 1, wx.EXPAND), (self.sizer6, 1, wx.EXPAND), (self.sizer7, 1, wx.EXPAND), ])
            self.mainsizer.Show(self.box3sizer, show=True)
            self.mainset = 5
        else:
            pass
        self.Layout()
        print('ouch!')

    def onClick6(self, event):
        if not self.mainset == 6:
            self.cleanall()
            self.mainsizer.Add(self.box3sizer, 1, wx.EXPAND)
            self.box3sizer.AddMany(
                [(self.box_left_sizer, 1, wx.EXPAND), (self.sizer6, 3, wx.EXPAND),
                 (self.box_right_sizer, 1, wx.EXPAND)])
            self.box_left_sizer.AddMany(
                [(self.sizer1, 1, wx.EXPAND), (self.sizer2, 1, wx.EXPAND), (self.sizer3, 1, wx.EXPAND), ])
            self.box_right_sizer.AddMany(
                [(self.sizer4, 1, wx.EXPAND), (self.sizer5, 1, wx.EXPAND), (self.sizer7, 1, wx.EXPAND), ])
            self.mainsizer.Show(self.box3sizer, show=True)
            self.mainset = 6
        else:
            pass
        self.Layout()
        print('ouch!')

    def onClick7(self, event):
        if not self.mainset == 7:
            self.cleanall()
            self.mainsizer.Add(self.box3sizer, 1, wx.EXPAND)
            self.box3sizer.AddMany(
                [(self.box_left_sizer, 1, wx.EXPAND), (self.sizer7, 3, wx.EXPAND),
                 (self.box_right_sizer, 1, wx.EXPAND)])
            self.box_left_sizer.AddMany(
                [(self.sizer1, 1, wx.EXPAND), (self.sizer2, 1, wx.EXPAND), (self.sizer3, 1, wx.EXPAND), ])
            self.box_right_sizer.AddMany(
                [(self.sizer4, 1, wx.EXPAND), (self.sizer5, 1, wx.EXPAND), (self.sizer6, 1, wx.EXPAND), ])
            self.mainsizer.Show(self.box3sizer, show=True)
            self.mainset = 7
        else:
            pass
        self.Layout()
        print('ouch!')


def set_sensor_value(sensor, value):
    pass


def set_plot_point(plot, point):
    pass


if __name__ == '__main__':
    app = wx.App()
    frame = main_frame(None, title="huji rocketry club", size=(500, 500), )
    app.MainLoop()
