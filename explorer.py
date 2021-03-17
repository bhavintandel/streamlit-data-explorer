"""
Module to explore various types of data
"""

import streamlit as st

SOURCES = ["Local"]
LOCAL_IMAGE_FILE_TYPES = ["png", "jpeg", "jpg"]
LOCAL_FILE_TYPES = ["csv", "pdf", "jpg", "txt", "png", "jpeg", "tsv", "xlsx"]

st.title("Data Explorer")

st.sidebar.title("Selection")
source_type = st.sidebar.selectbox("Source", SOURCES)


def read_csv(file_buffer):
    import pandas as pd

    _data = pd.read_csv(file_buffer)

    return 'csv', _data


def read_image(file_buffer):
    from PIL import Image

    img = Image.open(file_buffer)

    return 'img', img


def load_data(source_type):
    """
    Loads the data vased on selection
    :param source_type:
    :type source_type:
    :return:
    :rtype:
    """

    data = None

    if source_type == "Local":
        file_buffer = st.sidebar.file_uploader(label="Upload file", type=LOCAL_FILE_TYPES)
        if file_buffer:
            st.write("Filename: {name}".format(name=file_buffer.name))
            if file_buffer.name.endswith('.csv'):
                data = read_csv(file_buffer)
            elif file_buffer.name.endswith(tuple(LOCAL_IMAGE_FILE_TYPES)):
                data = read_image(file_buffer)
            elif file_buffer.name.endswith('.xlsx'):
                st.write("Received Excel file")

    return data


data = load_data(source_type)

if data:
    if data[0] == 'csv':
        st.write(data[1])
    elif data[0] == 'img':
        st.image(data[1])
