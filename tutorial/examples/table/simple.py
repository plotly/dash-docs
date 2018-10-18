import dash
import dash_table
import pandas as pd


df = pd.DataFrame([
    {
        'Average MW Per Plant': 15.3, 'Generation (GWh)': 10826,
        'Installed Capacity (MW)': 4395, 'Number of Solar Plants': 289, 'State': 'California'},
    {
        'Average MW Per Plant': 22.5, 'Generation (GWh)': 2550,
        'Installed Capacity (MW)': 1078, 'Number of Solar Plants': 48, 'State': 'Arizona'},
    {
        'Average MW Per Plant': 21.6, 'Generation (GWh)': 557,
        'Installed Capacity (MW)': 238, 'Number of Solar Plants': 11, 'State': 'Nevada'},
    {
        'Average MW Per Plant': 7.9, 'Generation (GWh)': 590,
        'Installed Capacity (MW)': 261, 'Number of Solar Plants': 33, 'State': 'New Mexico'},
    {
        'Average MW Per Plant': 5.9, 'Generation (GWh)': 235,
        'Installed Capacity (MW)': 118, 'Number of Solar Plants': 20, 'State': 'Colorado'},
    {
        'Average MW Per Plant': 15.6, 'Generation (GWh)': 354,
        'Installed Capacity (MW)': 187, 'Number of Solar Plants': 12, 'State': 'Texas'},
    {
        'Average MW Per Plant': 4.5, 'Generation (GWh)': 1162,
        'Installed Capacity (MW)': 669, 'Number of Solar Plants': 148, 'State': 'North Carolina'},
    {
        'Average MW Per Plant': 4.1, 'Generation (GWh)': 84,
        'Installed Capacity (MW)': 53, 'Number of Solar Plants': 13, 'State': 'New York'
    }
], columns=[
    'State', 'Number of Solar Plants', 'Installed Capacity (MW)',
    'Average MW Per Plant', 'Generation (GWh)'])


app = dash.Dash(__name__)

app.layout = dash_table.Table(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    dataframe=df.to_dict("rows"),
)

if __name__ == '__main__':
    app.run_server(debug=True)
