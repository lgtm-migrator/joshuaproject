# AUTOGENERATED! DO NOT EDIT! File to edit: 00_url.ipynb (unless otherwise specified).

__all__ = ['api_key', 'url_path_query', 'url_upgotd', 'url_pgs_cntry', 'url_upgs_cntry', 'url_pg_cntry',
           'url_pg_cntries', 'url_cntry', 'url_lang']

# Cell
from functools import partial
from datetime import date
from urllib3.util.url import Url

# Cell
api_key = 'your_api_key' # 'w3NOS49TW7fg'

# Cell
def url_path_query(path: str, cntry: str=None, pgid: str=None,\
                   lang=None, extra=None, month=None, day=None,\
                   api_key=api_key)->str:
    """Builds and returns a string url to query `path` for `cntry`
    with optional `pgid`,`extra`,`month` and `day`."""
    query = ''
    if cntry is not None:
        query = query+'ROG3='+str(cntry)
    if pgid  is not None:
        query = query+'&PeopleID3='+str(pgid)
    if lang  is not None:
        query = query+'&ROL3='+str(lang)
    if extra is not None:
        query = query+'&'+str(extra)
    if 'upgotd' in path:
        today = date.today()
        if isinstance(day, int):
            day = str(day)
        if isinstance(month, int):
            month = str(month)
        if day is None:
            day = today.strftime("%-d")
        if month is None:
            month = today.strftime("%-m")
        query = query+'&LRofTheDayMonth='+month
        query = query+'&LRofTheDayDay='  +day
    query = query+'&api_key='+api_key
    return Url(scheme='https', host='joshuaproject.net', \
               path=path, query=query).url

# Cell
url_upgotd = partial(url_path_query, '/api/v2/upgotd')
url_upgotd.__doc__ = """Get data for the Unreached People Group of the Day."""

# Cell
url_pgs_cntry = partial(url_path_query, '/api/v2/people_groups')
url_pgs_cntry.__doc__ = """Get all people groups in a specific `cntry` country."""

# Cell
url_upgs_cntry = partial(url_pgs_cntry, extra='LeastReached=Y')
url_upgs_cntry.__doc__ = """Get all unreached people groups in a specific `cntry` country."""

# Cell
url_pg_cntry = partial(url_pgs_cntry)
url_pg_cntry.__doc__ = """Get a specific people group in a specific `cntry` country."""

# Cell
url_pg_cntries = partial(url_pgs_cntry)
url_pg_cntries.__doc__ = """Get all countries a specific `pgid` people group lives in"""

# Cell
url_cntry = partial(url_path_query, '/api/v2/countries')
url_cntry.__doc__ = """Get summary data for `cntry`."""

# Cell
url_lang = partial(url_path_query, '/api/v2/languages')
url_lang.__doc__ = """Get summary data for `lang` language."""