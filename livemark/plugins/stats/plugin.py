import os
from datetime import datetime
from ...plugin import Plugin


class StatsPlugin(Plugin):
    priority = 60
    profile = {
        "type": "object",
        "properties": {
            "format": {"type": "string"},
        },
    }

    def process_markup(self, markup):
        config = self.get_config(markup)
        if not config:
            return

        # Prepare context
        format = config.get("format", "%Y-%m-%d %H:%M:%S")
        current = datetime.fromtimestamp(os.path.getmtime(markup.document.source))

        # Update markup
        markup.add_style("style.css")
        markup.add_markup(
            "markup.html",
            action="prepend",
            target="#livemark-main",
            format=format,
            current=current,
        )
