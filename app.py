from jinja2 import Template
import streamlit as st
import json


def index():
    st.title('📄 Document Filler')
    st.write('''
        Selecione o documento base `.md` a ser preenchido
        juntamente com o arquivo `.json` contendo os dados.
    ''')

    with st.form(key='form'):
        template_file = st.file_uploader('Documento base', type='md')
        context_file = st.file_uploader('Dados', type='json')
        submit_button = st.form_submit_button('Enviar')

        if submit_button and template_file and context_file:
            st.session_state['template'] = template_file.read().decode('utf-8')
            st.session_state['context'] = json.load(context_file)
            st.query_params['page'] = 'document'
            st.rerun()


def document():
    with st.spinner('Carregando...'):
        template = Template(st.session_state['template'])
        context = st.session_state['context']
        st.markdown(template.render(context), unsafe_allow_html=True)

    if st.button('Voltar para a página inicial'):
        st.session_state.pop('template')
        st.session_state.pop('context')
        st.query_params['page'] = 'index'
        st.rerun()


if __name__ == '__main__':
    st.set_page_config(
        page_title='Markdown Filler',
        page_icon='📄'
    )
    current_page = globals()[
        st.query_params.get('page', 'index')
    ]
    current_page()
