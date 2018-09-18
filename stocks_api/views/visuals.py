from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
import requests
from urllib.parse import urlparse
import json

# Imports from Jupyter Notebook
import pandas as pd
from math import pi
from pandas.io.json import json_normalize
from bokeh.plotting import figure, output_file, save


class VisualsAPIView(APIViewSet):

    def retrieve(self, request, id=None):
        """Hit IEX API to retrieve info on one stock.
        """
        url_to_parse = request.current_route_url()  # returns http://localhost:6543/api/v1/visuals/goog/?type=candle
        chart_type = urlparse(url_to_parse).query  # returns type=candlestick
        print(chart_type)
        url = 'https://api.iextrading.com/1.0/stock/{}/chart/5y'.format(id)
        response = requests.get(url)
        df = json_normalize(json.loads(response.text))
        df["date"] = pd.to_datetime(df["date"])

        inc = df.close > df.open
        dec = df.open > df.close
        w = 12*60*60*1000  # half day in ms

        TOOLS = "pan,wheel_zoom,box_zoom,reset,save,hover"

        p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title='{} Candlestick'.format(id.upper()))
        p.xaxis.major_label_orientation = pi/4
        p.grid.grid_line_alpha = 0.3

        p.segment(df.date, df.high, df.date, df.low, color="black")
        p.vbar(df.date[inc], w, df.open[inc], df.close[inc], fill_color="#00FF00", line_color="black")
        p.vbar(df.date[dec], w, df.open[dec], df.close[dec], fill_color="#ff0000", line_color="black")
        p.xaxis.axis_label = "Date"
        p.xaxis.axis_label_text_color = "#aa6666"
        p.xaxis.axis_label_text_font_size = "20pt"
        p.xaxis.axis_label_standoff = 30
        p.yaxis.axis_label = "Price (USD)"
        p.yaxis.axis_label_text_color = "#aa6666"
        p.yaxis.axis_label_standoff = 30
        p.yaxis.axis_label_text_font_size = "20pt"

        output_file("./static/candlestick.html", title="candlestick.py example")
        save(p)
        import codecs
        f = codecs.open('./static/candlestick.html', 'r')
        body = f.read()
        # print(body)

        return Response(body=body, status=200)
        # message = 'Here is the info for Ticker Symbol: {}'.format(id)
        # return Response(json={'company': message}, status=200)
