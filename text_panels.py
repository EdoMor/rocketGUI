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
        self.sizer = wx.BoxSizer()
        self.sizer.Add(self.text_object, 1, wx.EXPAND)

    def check(self):
        self.status = self.check_function()
        if self.status == True:
            self.text_object.SetBackgroundColour("GREEN")
            self.text_object.SetLabel(self.name)
            self.text_object.GetParent().Layout()
            self.text_object.GetParent().Update()
            # self.text_object.Update()

        else:
            self.text_object.SetBackgroundColour("RED")
            self.text_object.SetLabel(self.name + "\n" + str(self.status))
            self.text_object.GetParent().Layout()
            self.text_object.GetParent().Update()
            # self.text_object.Update()

        self.checked = True


class numbers_panel(wx.Panel):
    def __init__(self, parent, data_path, id=-1, *args, **kwargs):
        super(numbers_panel, self).__init__(parent, id=-1, *args, **kwargs)
        self.data_path = data_path
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

    def update(self):
        with open(self.data_path, 'r') as fo:
            data = fo.readlines()
        data = data[-1].split(',')
        for i in range(SENSOR_NUMBER):
            if data[i] == 't':
                self.sensor[i].text_object.SetBackgroundColour("GREEN")
                self.sensor[i].text_object.SetLabel(self.sensor[i].name + ':\n' + 'True')
            elif data[i] == 'f':
                self.sensor[i].text_object.SetBackgroundColour("RED")
                self.sensor[i].text_object.SetLabel(self.sensor[i].name + ':\n' + 'False')
            else:
                self.sensor[i].text_object.SetLabel(self.sensor[i].name + ':\n' + str(data[i]))
            self.sensor[i].text_object.GetParent().Layout()
            self.sensor[i].text_object.GetParent().Update()


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
            self.panel_sizer.Add(self.sensor[i].sizer, 1, wx.EXPAND)
            self.sensor[i].text_object.Center()
            if not i % 2 == 0:
                self.sensor[i].text_object.SetBackgroundColour("LIGHT GRAY")
        self.check_btn = wx.Button(self, -1, label="check")
        self.check_btn.Bind(wx.EVT_BUTTON, self.check)
        self.panel_sizer.Add(self.check_btn, 1, wx.EXPAND)

    def check(self, event):
        for i in range(SENSOR_NUMBER):
            if i % 2 == 0:
                self.sensor[i].text_object.SetBackgroundColour("DARK WHITE")
            else:
                self.sensor[i].text_object.SetBackgroundColour("LIGHT GRAY")
        for sensor in self.sensor:
            sensor.check()


class main_frame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(main_frame, self).__init__(parent, *args, **kwargs)
        self.panel = numbers_panel(self, -1, style=wx.SUNKEN_BORDER, data_path='examplen.txt')
        self.panel.Center()
        self.panel.update()


if __name__ == '__main__':
    app = wx.App()
    frame = main_frame(None)
    frame.SetSize((500, 500))
    frame.Show()
    app.MainLoop()
