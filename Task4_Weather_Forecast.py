from tkinter import *
import json
import requests

def data(event):
    if(city_name.get()):
        city=city_name.get()
        api="2f44068457b17f0f95e722a946f8e1b1"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
        response=requests.get(url).json()
        longitute=response["coord"]["lon"]
        latitude=response["coord"]["lat"]
        url2=f"https://timeapi.io/api/Time/current/coordinate?latitude={latitude}&longitude={longitute}"
        response2=requests.get(url2).json()
        weather_lbl=Label(win,text="Weather",font=("times new roman",14,"bold"),
                          fg="brown",bg="light grey")
        weather_lbl.place(x=50,y=180)
        temp=Label(win,text="Temperature",font=("times new roman",14,"bold"),
                              fg="brown",bg="light grey")
        temp.place(x=50,y=225)
        pressure=Label(win,text="Pressure",font=("times new roman",14,"bold"),
                          fg="brown",bg="light grey")
        pressure.place(x=50,y=270)
        time=Label(win,text="Time",font=("times new roman",14,"bold"),
                          fg="brown",bg="light grey")
        time.place(x=50,y=315)
        humidity=Label(win,text="Humidity",font=("times new roman",14,"bold"),
                          fg="brown",bg="light grey")
        humidity.place(x=50,y=360)
    
    #output 

        weather_out_res=StringVar()
        temp_out_res=StringVar()
        humidity_out_res=StringVar()
        pressure_out_res=StringVar()
        time_out_res=StringVar()

        weather_out_res.set(response["weather"][0]["main"])
        temp_out_res.set(response["main"]["temp"])
        pressure_out_res.set(response["main"]["pressure"])
        time_out_res.set(response2["time"])
        humidity_out_res.set(response["main"]["humidity"])

        weather_out=Entry(win,textvariable=weather_out_res,font=("times new roman",12,"italic"),
                          fg="brown",bg="light grey",relief=FLAT,borderwidth=1,state="readonly")
        weather_out.place(x=190,y=180)
        temp_out=Entry(win,textvariable=temp_out_res,font=("times new roman",12,"italic"),
                          fg="brown",bg="light grey",relief=FLAT,borderwidth=1,state="readonly")
        temp_out.place(x=190,y=225)
        pressure_out=Entry(win,textvariable=pressure_out_res,font=("times new roman",12,"italic"),
                          fg="brown",bg="light grey",relief=FLAT,borderwidth=1,state="readonly")
        pressure_out.place(x=190,y=270)
        time_out=Entry(win,textvariable=time_out_res,font=("times new roman",12,"italic"),
                          fg="brown",bg="light grey",relief=FLAT,borderwidth=1,state="readonly")
        time_out.place(x=190,y=315)
        humidity_out=Entry(win,textvariable=humidity_out_res,font=("times new roman",12,"italic"),
                          fg="brown",bg="light grey",relief=FLAT,borderwidth=1,state="readonly")
        humidity_out.place(x=190,y=360)

        city_name.set("")
        input_field.update()
    
    

win=Tk()
win.title("WEATHER FORECAST APP")
win.geometry("400x500+0+0")
win.resizable(False,False)

city_name=StringVar()

input_label=Label(win,text="Enter city name : ",font=("Calbari",14,"italic"))
input_label.place(x=15,y=20)

input_field=Entry(win,textvariable=city_name,font=("times new roman",12),relief=RIDGE,borderwidth=3)
input_field.place(x=170,y=20,height=30,width=200)

btn=Button(text="SUBMIT",relief=RAISED,font=("times new roman",12,"bold"),
           borderwidth=2,bg="green",fg="white")
btn.place(x=160,y=75)
btn.bind("<Button-1>",data)

ico=PhotoImage(file='weather.png')
win.iconphoto(False,ico)


win.mainloop()

