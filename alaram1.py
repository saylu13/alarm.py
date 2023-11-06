from tkinter import *
import datetime
import time

hour = ['00', '01', '02', '03', '04', '05', '06', '07',
        '08', '09', '10', '11', '12', '13', '14', '15',
        '16', '17', '18', '19', '20', '21', '22', '23', '24']

minutes = ['00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60']

seconds = ['00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60']


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        if now == set_alarm_timer:
            wakeup_text.config(text="Your Time is Up")
        break


def alarm_time():
    wakeup_text.config(text="Alarm Set")
    set_alarm_timer = f"{hour_options.get()}:{mins_options.get()}:{sec_options.get()}"
    alarm(set_alarm_timer)


window = Tk()
window.title("Alarm CLock")
window.config(padx=40, pady=30)
alarm_text = Label(text="Alarm Clock", font=("Helvetica 20 bold"), fg="purple")
alarm_text.grid(row=0, column=2, columnspan=3)
set_text = Label(text="Set Time", font=("Helvetica 15 bold"), fg="red")
set_text.grid(row=1, column=2, columnspan=3)

hour_options = StringVar(window)
hour_options.set(hour[0])
hr = OptionMenu(window, hour_options, *hour)
hr.config(bg="grey")
hr.grid(row=2, column=2, )

mins_options = StringVar(window)
mins_options.set(minutes[0])
mins = OptionMenu(window, mins_options, *minutes)
mins.config(bg="grey")
mins.grid(row=2, column=3)

sec_options = StringVar(window)
sec_options.set(seconds[0])
sec = OptionMenu(window, sec_options, *seconds)
sec.config(bg="grey")
sec.grid(row=2, column=4)

hr_text = Label(text="Hr", )
hr_text.grid(row=3, column=2, )
min_text = Label(text="Min")
min_text.grid(row=3, column=3)
sec_text = Label(text="Sec")
sec_text.grid(row=3, column=4)

set_button = Button(text="Set", width=10, font=("Helvetica 10 bold"), fg="black", bg="red", command=alarm_time)
set_button.grid(row=4, column=2, columnspan=3, rowspan=1)

format_text = Label(text="Enter time in 24-Hour format", font=("Helvetica 10 bold"), fg="blue")
format_text.grid(row=5, column=2, columnspan=3)

wakeup_text = Label(text="", font=("Helvetica 15 bold"), fg="red")
wakeup_text.grid(row=6, column=2, columnspan=3)

window.mainloop()