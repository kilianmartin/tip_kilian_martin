import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from flask_login import login_required

import requests
import json


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


def k1_fetch():
    k1_endpoint = "https://eydvdcrr2v9awbf-iboardadw.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi1/incvol/"

    k1_r = requests.get(k1_endpoint)
    k1_kpi_data = k1_r.json()["items"]


    k1_months = []
    k1_incidences_numbers = []
    k1_priorities = []

    for dict in k1_kpi_data:
        k1_months_year = dict["month"][0:4]
        k1_months_month = dict["month"][4:]

        k1_months.append(f'{k1_months_month}/{k1_months_year}')
        k1_incidences_numbers.append(dict["incidences_number"])
        k1_priorities.append(dict["priority"])


    k1_df = pd.DataFrame({
        "Months": k1_months,
        "Number of incidents": k1_incidences_numbers,
        "Priority": k1_priorities
    })

    return k1_df

def k2_fetch():
    #k2_endpoint = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi2/incsolved/" ##REPLACE WITH MINE!
    k2_endpoint = "https://eydvdcrr2v9awbf-iboardadw.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi2/incsolved/" ##REPLACE WITH MINE!

    k2_r = requests.get(k2_endpoint)
    k2_kpi_data = k2_r.json()["items"]



    k2_months = []
    k2_incidences_numbers = []


    for dict in k2_kpi_data:
        k2_months_year = dict["month"][0:4]
        k2_months_month = dict["month"][4:]

        k2_months.append(f'{k2_months_month}/{k2_months_year}')
        k2_incidences_numbers.append(dict["incidences_number"])



    k2_df = pd.DataFrame({
        "Months": k2_months,
        "Number of incidents": k2_incidences_numbers
    })
    
    return k2_df

def k3_fetch(month_selected):
    """
    if month_selected == "Mar": 
        k3_endpoint = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi3/sla/201803" ##REPLACE LATER
    elif month_selected == "Feb":
        k3_endpoint = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi3/sla/201802" ##REPLACE LATER
    else:
        k3_endpoint = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi3/sla/201801" ##REPLACE LATER
    """
    if month_selected == "Mar": 
        k3_endpoint = "https://eydvdcrr2v9awbf-iboardadw.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi3/sla/201803" ##REPLACE LATER
    elif month_selected == "Feb":
        k3_endpoint = "https://eydvdcrr2v9awbf-iboardadw.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi3/sla/201802" ##REPLACE LATER
    else:
        k3_endpoint = "https://eydvdcrr2v9awbf-iboardadw.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi3/sla/201801" ##REPLACE LATER


    k3_r = requests.get(k3_endpoint)
    k3_kpi_data = k3_r.json()["items"][0]

    percents = []
    types = []
    priorities = []

    revelant_keys = list(k3_kpi_data.keys())[1:]

    for key in revelant_keys:
        percents.append(k3_kpi_data[key])
        

        if "br" in key:
            types.append("Breached")
            priorities.append(key.replace("br", ""))
        else:
            types.append("Met")
            priorities.append(key.replace("mt", ""))
    
    k3_df = pd.DataFrame({
    "Priority": priorities,
    "Percent": percents,
    "SLA adherence": types
    })
    
    return k3_df

def k4_fetch():
    
    #k4_endpoint = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi4/BL/"
    k4_endpoint = "https://eydvdcrr2v9awbf-iboardadw.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi4/BL/"

    k4_r = requests.get(k4_endpoint)
    k4_kpi_data = k4_r.json()["items"]

    months = []
    incident_numbers = []


    for key in k4_kpi_data:
        incident_number = key["incidences_number"]
        incident_numbers.append(incident_number)
        
        month = key["month"]

        k4_months_year = key["month"][0:4]
        k4_months_month = key["month"][4:]

        months.append(f'{k4_months_month}/{k4_months_year}')


    k4_df = pd.DataFrame({
        "Months": months,
        "Number of incidents": incident_numbers
    })
    
    return k4_df

def k5_fetch():
    """
    k5_endpoint_1 = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi5/av/201801"
    k5_endpoint_2 = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi5/av/201802"
    k5_endpoint_3 = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi5/av/201803"
    """

    k5_endpoint_1 = "https://eydvdcrr2v9awbf-iboardadw.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi5/av/201801"
    k5_endpoint_2 = "https://eydvdcrr2v9awbf-iboardadw.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi5/av/201802"
    k5_endpoint_3 = "https://eydvdcrr2v9awbf-iboardadw.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi5/av/201803"
    endpoints = [k5_endpoint_3, k5_endpoint_2, k5_endpoint_1]


    months = []
    monthly_availabilities = []

    output_dict = {}

    for k5_endpoint in endpoints:

        k5_r = requests.get(k5_endpoint)
        k5_kpi_data = k5_r.json()["items"]


        output_dict[k5_kpi_data[0]["month"]] = {}

        for dict in k5_kpi_data:
            service = dict["service"]

            month = dict["month"]
            unav_time = dict["unavailability_time"]
            av_per = dict["availability_percentage"]

            output_dict[month][service] = [unav_time, av_per]
    
    
    #output_dict = {'201801': {'.COM': [2.3, 0.9968493150684932], 'FLIGHT DISPATCHING': [1.6166666666666667, 0.9977853881278539], 'FLIGHT TRACKING AND CONTROL': [4, 0.9945205479452055], 'MAD-HUB OPERATIONAL MANAGEMENT SYSTEM': [8.55, 0.9882876712328768]}, '201802': {'.COM': [2.8666666666666667, 0.9960730593607305], 'MAD-HUB OPERATIONAL MANAGEMENT SYSTEM': [8.683333333333334, 0.9881050228310503], 'STATIONS OPERATIONAL MANAGEMENT SYSTEM': [11.716666666666667, 0.9839497716894977]}, '201803': {'.COM': [3.933333333333333, 0.9946118721461187], 'FLIGHT DISPATCHING': [2.966666666666667, 0.9959360730593607], 'STATIONS OPERATIONAL MANAGEMENT SYSTEM': [2.533333333333333, 0.9965296803652968]}}

    return output_dict

def k6_fetch():
    """
    k6_endpoint_1 = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi6/monav/201801"
    k6_endpoint_2 = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi6/monav/201802"
    k6_endpoint_3 = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi6/monav/201803" 
    """
    
    k6_endpoint_1 = "https://eydvdcrr2v9awbf-iboardadw.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi6/monav/201801"
    k6_endpoint_2 = "https://eydvdcrr2v9awbf-iboardadw.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi6/monav/201802"
    k6_endpoint_3 = "https://eydvdcrr2v9awbf-iboardadw.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi6/monav/201803"

    endpoints = [k6_endpoint_1, k6_endpoint_2, k6_endpoint_3]

    months = []
    monthly_availabilities = []

    for k6_endpoint in endpoints:

        k6_r = requests.get(k6_endpoint)
        k6_kpi_data = k6_r.json()["items"][0]

        month = k6_kpi_data["month"]

        k6_months_year = k6_kpi_data["month"][0:4]
        k6_months_month = k6_kpi_data["month"][4:]

        months.append(f'{k6_months_month}/{k6_months_year}')
        
        monthly_availability = round(k6_kpi_data["monthly_av"], 5)*100
        monthly_availabilities.append(monthly_availability)


    k6_df = pd.DataFrame({
        "Months": months,
        "Monthly Availability (in %)": monthly_availabilities
    })
    
    return k6_df


def create_dash_kpi1(flask_app):

    
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname=("/kpi1/"), external_stylesheets=external_stylesheets)


    dash_app.layout = html.Div(children=[
        html.H1(children='Number of incidents - by priority'),

        html.Div(children='''
            How many incidents do we have and how severe are they?
        '''),

        dcc.Graph(
            id='kpi1',
            figure= px.bar(k1_fetch(), x="Months", y="Number of incidents", color="Priority", barmode="group"),
            


        )
    ], style={'font-family': ' Arial, Helvetica, sans-serif'})
    
    
    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function])
    
    
    return dash_app


def create_dash_kpi2(flask_app):
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname=("/kpi2/"))


    dash_app.layout = html.Div(children=[
        html.H1(children='KPI2'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Graph(
            id='example-graph',
            figure= px.bar(k2_fetch(), x="Months", y="Number of incidents", barmode="group")

        )
    ], style={'font-family': ' Arial, Helvetica, sans-serif'})
    
    
    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function])
    
    return dash_app


def create_dash_kpi3(flask_app):

    
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname=("/kpi3/"))


    dash_app.layout = html.Div(children=[
        html.H1(children='SLA Adherence - March 2018'),

        html.Div(children='''
            Are we adhering to our SLAs?
        '''),

        dcc.Graph(
            id='kpi3-3',
            figure= px.bar(k3_fetch("Jan"), x="Priority", y="Percent", color="SLA adherence", barmode="group")


        ),

        html.H1(children='SLA Adherence - Feb. 2018'),

        html.Div(children='''
            Are we adhering to our SLAs?
        '''),

        dcc.Graph(
            id='kpi3-2',
            figure= px.bar(k3_fetch("Feb"), x="Priority", y="Percent", color="SLA adherence", barmode="group")


        ),

        html.H1(children='SLA Adherence - Jan. 2018'),

        html.Div(children='''
            Are we adhering to our SLAs?
        '''),

        dcc.Graph(
            id='kpi3-1',
            figure= px.bar(k3_fetch("Mar"), x="Priority", y="Percent", color="SLA adherence", barmode="group")


        )

    ], style={'font-family': ' Arial, Helvetica, sans-serif'})
    
    
    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function])
    
    return dash_app


def create_dash_kpi4(flask_app):
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname=("/kpi4/"))


    dash_app.layout = html.Div(children=[
        html.H1(children='Backlog of incidents'),

        html.Div(children='''
            How many incidents do we have in our backlog?
        '''),

        dcc.Graph(
            id='kpi4',
            figure= px.bar(k4_fetch(), x="Months", y="Number of incidents", barmode="group")

        )
    ], style={'font-family': ' Arial, Helvetica, sans-serif'})
    
    
    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function])
    
    return dash_app



def create_dash_kpi5_constructor(k5_dict):
    
    children = []
    
    for month in k5_dict.keys():
        
        months_year = month[0:4]
        months_month = month[4:]
        
        
        children.append(html.H1(children=f'Critical services in {months_month}/{months_year}'))
        
        for service in k5_dict[month].keys():
            
            service_array = []
            service_array.append(html.H2(children=f'{months_month}/{months_year}: {service}'))
            
            kpis = k5_dict[month][service]

            service_array.append(html.P(children=f'Downtime: {round(kpis[0], 2)} mins'))
            
            kpi_list1 = [kpis[1] * 100]

            kpi_df = pd.DataFrame({
                "% Availability": kpi_list1
            })
            

            service_array.append(dcc.Graph(
                figure= px.bar(kpi_df, x="% Availability", 
                orientation='h', height=200, range_x=[97.5, 100])
                .update_yaxes(showticklabels=False, title_font_color="rgba(0, 0, 0, 0)")
                .update_layout({'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                })


                ))

            service_div = html.Div(service_array, style={'background-color': '#f7f7f7', 'padding': '10px', 'margin-bottom': '10px'})
            
            children.append(service_div)

    return children





def create_dash_kpi5(flask_app):
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname=("/kpi5/"))

    k5_dict = k5_fetch()

    children = create_dash_kpi5_constructor(k5_dict)

    dash_app.layout = html.Div(children, style={'font-family': ' Arial, Helvetica, sans-serif'})
    
    
    
    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function])
    
    return dash_app


def create_dash_kpi6(flask_app):
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname=("/kpi6/"))


    dash_app.layout = html.Div(children=[
        html.H1(children='Monthly Availability of critical services'),

        html.Div(children='''
            How well are our most critical services available?
        '''),

        dcc.Graph(
            id='kpi6',
            figure= px.bar(k6_fetch(), x="Months", y="Monthly Availability (in %)", barmode="group", range_y=[90, 100])

        )
    ], style={'font-family': ' Arial, Helvetica, sans-serif'})
    
    
    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function])
    
    return dash_app