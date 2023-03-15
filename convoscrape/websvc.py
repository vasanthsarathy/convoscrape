import os
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import json
import random
from dash import Dash, Input, Output, callback, dash_table
import pandas as pd

from dash import html

from convoscrape.scrape import run_scraper
from convoscrape.convoutils import get_current_corpora
from convoscrape.convoutils import update_corpus
from convoscrape.utils import search_help

from convokit import Corpus

import pathlib


ROOT = os.path.abspath(os.getcwd())


app = dash.Dash(__name__, title="cscrape", external_stylesheets=[dbc.themes.YETI, dbc.icons.FONT_AWESOME])
server = app.server #nee

LINE_BREAK = dbc.Row(html.Br())
LINE = dbc.Row(html.Hr())

DEFAULT_VALUE = "from:anadoluajansi since:2023-02-05 until:2023-02-27"


temp_data_table = pd.DataFrame()



# Top heading and logo
heading = [html.H2("🏗️ CONVOSCRAPE (v0.1)"),
           html.H5("snscrape → convokit"),
           dcc.Markdown("[repo](https://github.com/vasanthsarathy/convoscrape)")]
HEADER_ROW = dbc.Row(dbc.Col(heading, width={'size':5, 'offset':1}, align="center"))

# Input row
input_group = dbc.InputGroup(
    [
        dbc.Input(id="search-text-input",
                  placeholder="Enter your search string here ...",
                  value=DEFAULT_VALUE),
        dbc.Button("Search", id="search-button", n_clicks=0),
    ]
)

INPUT_ROW = dbc.Row(dbc.Col([dcc.Markdown("### Enter a search string:"),
                             input_group],
                            width={'size':10, 'offset':1}))

slider_num_returns = dcc.Slider(1, 100, 1,
                                value=10,
                                marks=None,
                                tooltip={"placement": "bottom",
                                         "always_visible": True},
                                id='slider-num-returns'),


SLIDER_ROW = dbc.Row(dbc.Col(slider_num_returns,
                             width={'size':10, 'offset':1}))


SPINNER_ROW = dbc.Row(dbc.Spinner(html.Div(id="spinner")))


output_table = html.Div(id="output-table")

OUTPUT_ROW = dbc.Row(dbc.Col(output_table,
                             width={'size':10, 'offset':1}))


SAVED_ROW = dbc.Row(dbc.Col(dbc.Alert(id="alert-saved", color="success", is_open=False, duration=2000), width={'size':10, 'offset':1}))

tab1_content = dbc.Card(dbc.CardBody([INPUT_ROW,
                LINE_BREAK,
                SLIDER_ROW,
                LINE_BREAK,
                SPINNER_ROW,
                OUTPUT_ROW,
                LINE_BREAK,
                SAVED_ROW]))

tab2_content = dbc.Card(dbc.CardBody([]))

tab3_content = dbc.Card(dbc.CardBody([dcc.Markdown(search_help)]))

tabs = dbc.Tabs([dbc.Tab(tab1_content, label="Search"),
                 dbc.Tab(tab2_content, label="Explore Corpus"),
                 dbc.Tab(tab3_content, label="Help")])

TABS_ROW = dbc.Row(dbc.Col(tabs,
                           width={'size':6,
                                  'offset':1}))
# DASH APP LAYOUT
app.layout = html.Div([LINE_BREAK,
                       HEADER_ROW,
                       LINE_BREAK,
                       LINE,
                       LINE_BREAK,
                       TABS_ROW])

############# CALLBACKS ############################
@app.callback(
    [Output("output-table", "children"),
    Output('spinner', 'value')],
    [Input("search-button", "n_clicks"),
     State("search-text-input", "value"),
     State("slider-num-returns", "value")])
def search(n_clicks, search_string, num_terms):
     global temp_data_table

     if n_clicks:
        temp_data_table = pd.DataFrame()
        # Run the snscraper function and put into pandas dataframe
        df = run_scraper(search_string, num_terms)

        df_limited = df[['text', 'speaker']]

        temp_data_table = df

        # initialize a dash table with this dataframe
        table = dash_table.DataTable(data=df_limited.to_dict('records'),
                                     columns=[{"name": i, "id": i} for i in df_limited.columns],
                                     style_data={
                                         'whiteSpace': 'normal',
                                         'height': 'auto'},
                                     id='tbl')

        # Add a header that says "Results"
        results_header = dcc.Markdown("## RESULTS:")


        # Inputs to add data to corpora
        select_corpora = get_select_dropdown()

        # Button to add the results to the corpus
        add_to_corpus_button = dbc.Button("Add to corpus",
                                          id="add-to-corpus-button",
                                          color="success",
                                          n_clicks=0)

        input_group_corpora = dbc.InputGroup([select_corpora, add_to_corpus_button])

        return [results_header, input_group_corpora, LINE_BREAK, SAVED_ROW, LINE_BREAK, table], ""
     else:
        raise dash.exceptions.PreventUpdate


@app.callback([Output("alert-saved", "is_open"),
               Output("alert-saved", "children")],
              [Input("add-to-corpus-button", "n_clicks"),
               State("select-corpora", "value")])
def add_to_corpus(n_clicks, corpus_name):
    global temp_data_table
    if n_clicks:
        if not corpus_name:
            print("Choose a corpus!")
            return False, ""
        else:
            print("Updating")
            success = update_corpus(corpus_name, temp_data_table)
            if success:
                return True, ["Saved!"]
            return False, ["Failed saving"]
    else:
        raise dash.exceptions.PreventUpdate


def get_select_dropdown():
    # get current corpora
    corpora = get_current_corpora()
    if corpora:
        options = []
        for corpus in corpora:
            options.append({"label": corpus, "value": corpus})
        options.append({"label": "NEW", "value": "NEW"})
        select = dbc.Select(id="select-corpora",
                            placeholder="Select corpora ...",
                            options=options)
    return select


#########################

def main():
    server.run(debug=True, port=8010)

if __name__ == "__main__":
    app.run_server(debug=True)
