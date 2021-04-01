# NBA libraries
from nba_api.stats.endpoints import leaguegamefinder, leaguestandings, playergamelog

# Dash libraries
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import base64
import requests
import pandas as pd

LIMITLESS_LOGO = "limitless-logo.png"
encode_image = base64.b64encode(open(LIMITLESS_LOGO, 'rb').read())

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        # html.H2("Menu", className="display-4"),
        html.Img(
            src="data:image/png;base64,{}".format(encode_image.decode()),
            style={'height': '20%', 'width': '100%'}
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Eastern Conference", href="/eastern-conference", active="exact"),
                dbc.NavLink("Western Conference", href="/western-conference", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):

    response = requests.get("http://gateway:9999/retrieve")

    standings_json = response.json()
    standings = pd.json_normalize(standings_json, record_path=['0', 'Standings'])
    df_cleaned_standings = standings[['TeamCity', 'TeamName', 'Conference', 'ConferenceRecord', 'PlayoffRank',
                                      'Division', 'DivisionRecord', 'DivisionRank', 'WINS', 'LOSSES', 'WinPCT']]
    df_west_standings = df_cleaned_standings[df_cleaned_standings['Conference'] == 'West']
    df_east_standings = df_cleaned_standings[df_cleaned_standings['Conference'] == 'East']

    if pathname == "/":
        # return html.P("This is the content of the home page!")
        return html.P("Welcome to AWTY!")
    elif pathname == "/eastern-conference":
        return html.Div(children=[
            dash_table.DataTable(
                id='east-standings-table',
                columns=[{'name': i, 'id': i} for i in df_east_standings.columns],
                data=df_east_standings.to_dict('records'),
            ),
            html.Div(id='standing-table-container')
        ])
    elif pathname == "/western-conference":
        return html.Div(children=[
            dash_table.DataTable(
                id='west_standings-table',
                columns=[{'name': i, 'id': i} for i in df_west_standings.columns],
                data=df_west_standings.to_dict('records'),
            ),
            html.Div(id='standing-table-container')
        ])
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
