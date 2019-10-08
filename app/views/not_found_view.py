from pygments import highlight
from flask import render_template
from app.views import BaseView

text = """
# Not Found

**There doesn't seem to be anything here.**"""


class NotFoundView(BaseView):
    def __init__(self):
        super().__init__()
        self.text = highlight(text, self.markdown_lexer, self.html_formatter)
        self.count = text.count('\n') + 1

    def dispatch_request(self, error):
        return render_template(
            'view.html',
            text=self.text,
            lines=self.count,
            disabled=['clone', 'save', 'raw', 'download']
        ), 404