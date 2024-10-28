from jinja2 import Template
from pathlib import Path
from typing import Dict
import streamlit as st
import json


_ROOT_DIR = Path(__file__).resolve().parent
_STORAGE_DIR = _ROOT_DIR / 'storage'
_TEMPLATE_FILE = _STORAGE_DIR / 'template.md.j2'
_CONTEXT_FILE = _STORAGE_DIR / 'context.json'


def get_template() -> str:
    with open(_TEMPLATE_FILE, 'r', encoding='utf-8') as file:
        return file.read()


def get_context() -> Dict[str, object]:
    with open(_CONTEXT_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == '__main__':
    st.set_page_config(
        page_title='Markdown Filler',
        page_icon='📄'
    )

    with st.spinner('Loading...'):
        template = Template(get_template())
        context = get_context()
        content = template.render(context)

    st.markdown(content, unsafe_allow_html=True)
