import altair as alt
import pandas as pd
import numpy as np
# import plotly.plotly as pl
import plotly.offline as plo
import plotly.graph_objs as go

from what2_dsp.types import FloatArr
from what2_dsp.analyze import compute_spectrum

from IPython.core.display import HTML


def mk_time(signal: FloatArr, scale: float | None = None):
    if scale is None:
        scale = (len(signal) - 1) / 10

    return np.linspace(
        0, scale, len(signal)
    )

def wave(signal: FloatArr, scale: float | None = None):

    if scale is None:
        scale = (len(signal) - 1) / 10

    time = mk_time(signal, scale)

    data = pd.DataFrame({
        "f(x)": signal,
        "x": time,
    })

    return alt.Chart(data).mark_line().encode( # type: ignore reportUnknownMemberType
        x='x',
        y='f(x)',
    )

def spectrum(signal: FloatArr, scale: float | None = None):

    spect = compute_spectrum(signal, scale)

    time = mk_time(signal, scale)[:spect.shape[1]]
    freq = np.linspace(0, 10, spect.shape[0])

    layout = go.Layout(
        title = "Spectrogram",
        xaxis = go.layout.XAxis(title="Time"),
        yaxis = go.layout.YAxis(title="Frequency"),
    )

    trace_data = go.Heatmap(
        x = time,
        y = freq,
        z = spect,
    )

    data = [trace_data]
    
    out = plo.plot({
            "data":data,
            "layout": layout,
        },
    )

    return HTML(
        filename=out
    )

