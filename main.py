
import pandas as pd
import dash
from dash import dcc
from dash import html
from app import app
from app import server
from dash import dcc, html, Input, Output, State
import pandas as pd
import openpyxl
import csv


csv_file_for_word = open('datasets/test.csv', encoding="utf8")
csv_word_file_reader = csv.reader(csv_file_for_word)

all_word_csv = []
all_moderate_word_csv = []
all_rural_word_csv = []

def separete_csv_word_list():
    for info in csv_word_file_reader:
        all_word_csv.append(info)

    for a in range(len(all_word_csv)):
        all_moderate_word_csv.append(all_word_csv[a][0])
        all_rural_word_csv.append(all_word_csv[a][1])

        #print(all_rural_word_csv)
separete_csv_word_list()



def processing(dummy_moderate_text):
    temp = str(dummy_moderate_text)
    temp1 = temp.replace('।', " ")
    temp2 = temp1.replace(',', " ")
    temp3 = temp2.replace('\'', " ")
    temp4 = temp3.replace('\"', " ")
    temp5 = temp4.replace('-', " ")
    temp6 = temp5.replace('?', " ")
    processed_moderate_data = temp6

    # print(processed_moderate_data)
    global test_2
    test_2 = processed_moderate_data
    c = build_word_list(processed_moderate_data)
    processed_moderate_data = ""
    return c




def build_word_list(processed_moderate_data):
    processed_moderate_data_word_list = list(processed_moderate_data.split(" "))

    b = matching_and_changing(processed_moderate_data_word_list)
    return b


def matching_and_changing(processed_moderate_data_word_list):
    for c in range(len(processed_moderate_data_word_list)):
        unchanged_word_dummy_list_temp_2.append(processed_moderate_data_word_list[c])
        for d in range(len(all_moderate_word_csv)):
            if processed_moderate_data_word_list[c] == all_moderate_word_csv[d]:
                unchanged_word_dummy_list_temp.append(processed_moderate_data_word_list[c])
                processed_moderate_data_word_list[c] = all_rural_word_csv[d]

    a = back_to_text(processed_moderate_data_word_list)
    processed_moderate_data_word_list.clear()
    return a



def back_to_text(processed_moderate_data_word_list):
    for i in processed_moderate_data_word_list:
        global expected_rural_text
        expected_rural_text = expected_rural_text + str(i) + " "

    z = ""
    z = expected_rural_text
    global test,test_3
    test = expected_rural_text
    test_3 = expected_rural_text
    expected_rural_text = ""
    return z



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.H1(children='Hello ( - )', style={'textAlign': 'center'}),
        html.H3(children='Shuvo: Welcome to my Language Converter Dashboard.', style={'textAlign': 'center'}),
        html.Br(),
        html.Br(),
    ]),
#
#  html.Div([
# html.H2(children="Paste your moderate bangla data here to convert it into nokhalian language !!! ",style={'textAlign': 'center'}),
#     dcc.Textarea(
#         id='textarea-state-example',
#         value='Write data here and press Convert',
#         style={'height':'250px','width':'90%','margin-left': '5%','margin-right': '5%'},
#     ),
#     html.Button('Convert', id='textarea-state-example-button', n_clicks=0,style={"margin-left":'92%'}),
# html.Br(),
# html.Br(),
#     html.Div(id='textarea-state-example-output', style={'whiteSpace': 'pre-line','margin-left': '5%','margin-right': '5%'})
# ])

    html.Div([
        html.H2(children="Paste your moderate bangla data here to convert it into nokhalian language !!! ",style={'textAlign': 'center'}),
        dcc.Input(id = 'data',
                  type="text",
                  placeholder="write data here and press enter",
                  debounce=True,
                  style={'height':'250px','width':'90%','margin-left': '5%','margin-right': '5%'})
    ]),
    html.Br(),
    html.Br(),
    html.H2(children="Here is your converted Nokhalian language !!! ",style={'textAlign': 'center'}),
    dcc.Textarea(id="out-all-types",style={'height':'250px','width':'90%','margin-left': '5%','margin-right': '5%'})

])

@app.callback(
    Output("out-all-types", "value"),
    Input("data", "value")
)

def update_output(*vals):
    x =  " | ".join((str(val) for val in vals if val))
    y = processing(x)
    return y

# @app.callback(
#     Output('textarea-state-example-output', 'children'),
#     Input('textarea-state-example-button', 'n_clicks'),
#     State('textarea-state-example', 'value')
# )
# def update_output(n_clicks, value):
#     if n_clicks > 0:
#         x = processing(value)
#         return 'Here is your converted Nokhalian language !!! \n{}'.format(x)


if __name__ == '__main__':
    app.run_server(debug=False)