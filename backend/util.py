import streamlit as st

import plotly.graph_objs as go

def display_dataframe(df, n_head=5, n_tail=5, n_random_sample=None):
    """
    Display the head, tail, or a random sample of a DataFrame using Streamlit.

    Parameters:
        df (pd.DataFrame): The DataFrame to display.
        n_head (int): Number of rows to display from the head of the DataFrame.
        n_tail (int): Number of rows to display from the tail of the DataFrame.
        n_random_sample (int): Number of random rows to display from the DataFrame. Overrides head and tail display if specified.
    """
    if n_random_sample:
        st.write(
            f"Random sample of {n_random_sample} rows from the DataFrame:")
        st.write(df.sample(n_random_sample))
    else:
        st.write("Head of the DataFrame:")
        st.write(df.head(n_head))
        st.write("Tail of the DataFrame:")
        st.write(df.tail(n_tail))


def plotly_dataframe(df, x_axis, y_axis, legend=True, colormap='Viridis',
                     marker='x', marker_size=2, x_lim=None, y_lim=None, target_class=None):
    """
    Create a Plotly scatter plot between y_axis vs x_axis. Optionally group by a target class.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data to plot.
        x_axis (str): The column name for the x-axis.
        y_axis (str): The column name for the y-axis.
        legend (bool, optional): Whether to show legend. Defaults to True.
        colormap (str, optional): The colormap to use. Defaults to 'Viridis'.
        marker (str, optional): The marker style. Defaults to 'x'.
        marker_size (int, optional): The size of the marker. Defaults to 2.
        x_lim (list, optional): The limits for the x-axis in the form [min_x, max_x]. Defaults to None.
        y_lim (list, optional): The limits for the y-axis in the form [min_y, max_y]. Defaults to None.
        target_class (str, optional): The column name for nominal classification. Defaults to None.

    Returns:
        plotly.graph_objs.Figure: The Plotly figure.
    """
    fig = go.Figure()

    if target_class and target_class in df.columns:
        unique_classes = df[target_class].unique()
        for class_value in unique_classes:
            class_df = df[df[target_class] == class_value]

            fig.add_trace(go.Scatter(
                x=class_df[x_axis],
                y=class_df[y_axis],
                mode='markers',
                marker=dict(
                    symbol=marker,
                    size=marker_size,
                    colorscale=colormap),
                name=f"{y_axis} ({class_value})"
            ))

    else:
        fig.add_trace(go.Scatter(
            x=df[x_axis],
            y=df[y_axis],
            mode='markers',
            marker=dict(
                symbol=marker,
                size=marker_size,
                color=df[y_axis],
                colorscale=colormap),
            name=y_axis
        ))

    # Ensure x-axis ticks show only actual values in the data at regular
    # intervals
    unique_x_vals = df[x_axis].unique()
    unique_x_vals.sort()
    # Adjust the interval as needed
    tick_interval = max(1, len(unique_x_vals) // 10)
    tickvals = unique_x_vals[::tick_interval]

    # Update layout
    fig.update_layout(
        xaxis=dict(
            title=x_axis,
            range=x_lim,
            tickmode='array',
            tickvals=tickvals),
        # only show those x-ticks that exist in data
        yaxis=dict(title=y_axis, range=y_lim),
        showlegend=legend,
    )

    return fig
