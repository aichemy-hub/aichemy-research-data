from pathlib import Path
import yaml
from datetime import datetime, timezone


def define_env(env):
    """
    mkdocs-macros hook: load resources from YAML and expose helper functions.
    This is called once at build time.
    """
    data_path = Path("data") / "resources.yml"
    resources = yaml.safe_load(data_path.read_text())

    # Make the full list available as {{ resources }} in templates
    env.variables["resources"] = resources

    @env.macro
    def all_resources_sorted():
        """
        Return all resources sorted by date.
        Usage in Markdown: {% for r in all_resources_sorted() %} ... {% endfor %}
        """

        return sorted(resources, key="date", reverse=True)

    @env.macro
    def last_updated():
        return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
