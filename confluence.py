#!/usr/bin/env python3

from PythonConfluenceAPI import ConfluenceAPI
from bs4 import BeautifulSoup
import argparse


def init_args():
    parser = argparse.ArgumentParser(description='Create Confluence page (so called "storage" object) and publish on Confluence.')
    
    parser.add_argument(
        '--username',
        required=True,
        help='Username for Confluence.'
    )

    parser.add_argument(
        '--password',
        required=True,
        help='Password for Confluence.'
    )

    parser.add_argument(
        '--endpoint',
        required=True,
        help='Confluence endpoint.'
    )

    parser.add_argument(
        '--page-id',
        required=True,
        help='Page id.')

    return parser.parse_args()

def create_storage():
    soup = BeautifulSoup('<ac:structured-macro ac:name="expand" ac:schema-version="1"><ac:parameter ac:name=""></ac:parameter><ac:rich-text-body></ac:rich-text-body></ac:structured-macro>', 'html.parser')
    soup.find_all('ac:parameter')[0]['ac:name'] = 'title'       # Modify namespaced attribute
    soup.find_all('ac:parameter')[0].string = 'Hello World!'    # Modify namespaced value
    return soup

def publish(soup, args):
    client = ConfluenceAPI(
        username=args.username,
        password=args.password,
        uri_base=args.endpoint
    )

    EXPAND_FIELDS = 'body.storage,space,ancestors,version'
    content = client.get_content_by_id(
            content_id=args.page_id,
            expand=EXPAND_FIELDS
    )

    content_data = {
        'id': args.page_id,
        'type': 'page',
        #'space': {'key': space_key},
        'title': 'New Page',
        'body': {
            'storage': {
                'value': str(soup),
                'representation': 'storage'
            }
        },
        #'ancestors': [] if not ancestor_id else [{'id': ancestor_id}]
        "version": {"number": content['version']['number'] + 1},
    }

    client.update_content_by_id(
        content_data=content_data,
        content_id=args.page_id
    )


args = init_args()

soup = create_storage()
print(soup)

publish(soup, args)
