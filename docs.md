### 📚 Docs

A simple usage guide, including technical aspects for customization. Below are the main elements described.

### 📖 Template

A base Markdown file to be filled out, which must follow the directives of [**🔗 Jinja2**](https://jinja.palletsprojects.com/en/stable/). To change the file name, it is necessary to update the reference in the source code. An example can be accessed at [`/storage/template.md.j2`](/storage/template.md.j2).

### 🔠 Context

A JSON file that contains the context to be incorporated into the template, meaning the data that should be present in the final document. Like the template, changing the name requires updating the source code. An example can be accessed at [`storage/context.json`](/storage/context.json).

### 🌐 Web Page

The final document will be available on a Streamlit page, which will open upon running the application. To export it as a PDF, go to **⋮** > **Print**, make any necessary adjustments, and save the file.
