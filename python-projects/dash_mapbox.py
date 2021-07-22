import yaml
import pandas
import numpy
import dash
import dash_table
import dash_core_components
import dash_html_components
from dash.dependencies import Input, Output
import plotly.offline
import plotly.graph_objects


def yml_loader(filepath):
    "Loads a yml file"
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data


def main():
    yaml_file = yml_loader("env_config.yml")
    mapbox_access_token = yaml_file["mapbox"]["access_token"]
    
    raw_data = pandas.read_csv("census-population-and-housing-linc.csv", sep=";", header=0)
    print(raw_data)


main()
