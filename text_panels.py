import time
import math

import wx
import sensor_check_place_holder as sc

SENSOR_NUMBER = 10


class sensors():
    def __init__(self, text_object, name, func):
        self.name = name
        self.status = None
        self.checked = False
        self.value = None
        self.check_function = func
        self.text_object = text_object

    def check(self):
        self.status = self.check_function()
        if self.status == True:
            self.text_object.SetBackgroundColour("GREEN")
            self.text_object.Update()
            self.text_object.SetLabel(
                self.name, )  # TODO: current method (.SetLabel()) creates a new object and needs replacing

        else:
            self.text_object.SetBackgroundColour("RED")
            self.text_object.SetLabel(self.name + "\n" + str(
                self.status))  # TODO: current method (.SetLabel()) creates a new object and needs replacing
            self.text_object.Update()

        self.checked = True


class numbers_panel(wx.Panel):
    def __init__(self, parent, id=-1, *args, **kwargs):
        super(numbers_panel, self).__init__(parent, id=-1, *args, **kwargs)
        self.panel_sizer = wx.FlexGridSizer(3, 10, 10)
        for i in range(3):
            self.panel_sizer.AddGrowableCol(i)
        for i in range(math.ceil(SENSOR_NUMBER / 3)):
            self.panel_sizer.AddGrowableRow(i)
        self.sensor = list()
        self.SetSizer(self.panel_sizer)
        for i in range(SENSOR_NUMBER):
            sensor_name = 'sensor ' + str(i + 1)
            sensor = sensors(wx.StaticText(self, -1, label=sensor_name, style=wx.ALIGN_CENTER), sensor_name,
                             sc.check_functions[i])
            self.sensor.append(sensor)
            self.panel_sizer.Add(self.sensor[i].text_object, 1, wx.EXPAND)
            self.sensor[i].text_object.Center()
            if not i % 2 == 0:
                self.sensor[i].text_object.SetBackgroundColour("LIGHT GRAY")


class video_panel(wx.Panel):
    def __init__(self, parent, id=-1, *args, **kwargs):
        super(video_panel, self).__init__(parent, id=-1, *args, **kwargs)


class systems_check_list(wx.Panel):
    def __init__(self, parent, id=-1, *args, **kwargs):
        super(systems_check_list, self).__init__(parent, id=-1, *args, **kwargs)
        self.panel_sizer = wx.BoxSizer(wx.VERTICAL)
        self.sensor = list()
        self.SetSizer(self.panel_sizer)
        for i in range(SENSOR_NUMBER):
            sensor_name = 'sensor ' + str(i + 1)
            sensor = sensors(wx.StaticText(self, -1, label=sensor_name, style=wx.ALIGN_CENTER), sensor_name,
                             sc.check_functions[i])
            self.sensor.append(sensor)
            self.panel_sizer.Add(self.sensor[i].text_object, 1, wx.EXPAND)
            self.sensor[i].text_object.Center()
            if not i % 2 == 0:
                self.sensor[i].text_object.SetBackgroundColour("LIGHT GRAY")
        self.check_btn = wx.Button(self, -1, label="check")
        self.check_btn.Bind(wx.EVT_BUTTON, self.check)
        self.panel_sizer.Add(self.check_btn, 1, wx.EXPAND)

    def check(self, event):
        for sensor in self.sensor:
            sensor.check()


class main_frame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(main_frame, self).__init__(parent, *args, **kwargs)
        self.panel = numbers_panel(self, -1, style=wx.SUNKEN_BORDER)
        self.panel.Center()


if __name__ == '__main__':
    app = wx.App()
    frame = main_frame(None)
    frame.Show()
    app.MainLoop()
