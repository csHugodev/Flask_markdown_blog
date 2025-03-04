import mistune
from mistune import markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from config import Config
import os

class CodeRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        if not info:
            return f"<pre><code>{mistune.escape(code)}</code></pre>"

        try:
            lexer = get_lexer_by_name(info, stripall=True)
        except Exception:
            lexer = get_lexer_by_name("text", stripall=False)

        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)

markdown_parser = mistune.create_markdown(renderer=CodeRenderer(), plugins=["strikethrough"])

def convert_md_to_html(post_name):
    post_path = os.path.join(Config.POSTS_FOLDER, post_name)
    print("NOMBRE DEL POST A BUSCAR:", post_path)
    if not os.path.exists(post_path):
        return "POST NO ENCONTRADO", 404

    with open(post_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    titulo = lines[0].strip() if len(lines) > 0 else "SIN TÍTULO"
    autor = lines[1].strip() if len(lines) > 1 else "DESCONOCIDO"
    fecha = lines[2].strip() if len(lines) > 2 else "FECHA NO DISPONIBLE"
    print(titulo)
    content = "".join(lines[3:])
    html_output = markdown_parser(content)

    return html_output, titulo, autor, fecha
