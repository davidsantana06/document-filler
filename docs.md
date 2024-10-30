### 📚 Docs

This simple usage guide includes technical aspects for easy customization. The primary components are outlined below.

The **📖 Template** (`storage/template.md.j2`) is a Markdown file designed to be filled using **Jinja2** directives. If the file name is changed, its reference in the source code must also be updated to ensure proper functionality.

The **🔠 Context** (`storage/context.json`) is a JSON file containing the data that will be incorporated into the template, forming the final document content. Like the template, any change to this file's name requires an update in the source code.

Once generated, the completed document will appear on a **🌐 Streamlit Page**, accessible upon running the application. To save it as a PDF, go to **⋮** > **Print**, make any necessary adjustments, and save the file.
