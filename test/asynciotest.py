import asyncio

def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host,80)
    r=yield from connect