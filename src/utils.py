from flask import jsonify, url_for

class APIException(Exception):
    def __init__(self, message, status_code=400, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["message"] = self.message
        return rv

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults else ()
    arguments = rule.arguments if rule.arguments else ()
    return len(defaults) >= len(arguments)

def generate_sitemap(app):
    links = ["/admin/"]
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            if "/admin/" not in url:
                links.append(url)

    links_html = "".join([f"<li><a href='{y}'>{y}</a></li>" for y in links])
    return f"""
        <div style="text-align: center;">
        <img style="max-height: 80px" src='https://storage.googleapis.com/breathecode/boilerplates/rigo-baby.jpeg' />
        <h1>Welcome to your Star Wars API</h1>
        <ul style="text-align: left;">{links_html}</ul>
        </div>
    """


