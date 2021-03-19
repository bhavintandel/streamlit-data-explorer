"""
Module to explore various types of data
"""

import streamlit as st

SOURCES = ["Local"]
LOCAL_IMAGE_FILE_TYPES = ["png", "jpeg", "jpg"]
LOCAL_FILE_TYPES = ["csv", "pdf", "jpg", "txt", "png", "jpeg", "tsv", "xlsx", "json", "docx"]


def read_csv(file_buffer):
    import pandas as pd

    _data = pd.read_csv(file_buffer)

    return 'csv', _data


def read_excel(file_buffer):
    import pandas as pd

    _data = pd.read_excel(file_buffer)

    return 'csv', _data


def read_json(file_buffer):
    import json

    _data = json.load(file_buffer)

    return 'json', _data


def read_image(file_buffer):
    from PIL import Image

    img = Image.open(file_buffer)

    return 'img', img


def read_txt(file_buffer):

    _data = str(file_buffer.read(), "utf-8")

    return 'txt', _data


def read_doc(file_buffer):
    import docx2txt

    _data = docx2txt.process(file_buffer)  # Parse in the uploadFile Class directory

    return 'txt', _data


def read_pdf(file_buffer):
    from PyPDF2 import PdfFileReader

    pdf_reader = PdfFileReader(file_buffer)
    count = pdf_reader.numPages
    all_page_text = ""
    for i in range(count):
        page = pdf_reader.getPage(i)
        all_page_text += page.extractText()

    return 'pdf', all_page_text


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
                data = read_excel(file_buffer)
            elif file_buffer.name.endswith('.json'):
                data = read_json(file_buffer)
            elif file_buffer.name.endswith('.pdf'):
                data = read_pdf(file_buffer)
            elif file_buffer.name.endswith('.txt'):
                data = read_txt(file_buffer)
            elif file_buffer.name.endswith('.docx'):
                data = read_doc(file_buffer)

    return data


st.title("Data Explorer")

st.sidebar.title("Selection")
source_type = st.sidebar.selectbox("Source", SOURCES)

data = load_data(source_type)

if data:
    raw_data = st.checkbox('Display Sample Raw Data')
    if raw_data:
        if data[0] == 'csv':
            st.dataframe(data[1])
        elif data[0] == 'img':
            st.image(data[1])
        elif data[0] == 'pdf':
            st.write(data[1][:1000])
        elif data[0] == 'txt':
            st.write(data[1][:1000])
        elif data[0] == 'json':
            st.json(data[1])


