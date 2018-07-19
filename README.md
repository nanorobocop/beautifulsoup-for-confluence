# Create/Modify and Publish Confluence page

## Preface
Confluence uses so called 'storage' format for pages.

This format is XML-based with namespaces in tags and attributes.

In order to understand those namespaces in BeautifulSoup 4 library, it is required to disable optimization.

`element.py.patch` does this task.

## Working with namespaced XML

```python
soup = BeautifulSoup('<ac:structured-macro ac:name="expand" ac:schema-version="1"><ac:parameter ac:name=""></ac:parameter><ac:rich-text-body></ac:rich-text-body></ac:structured-macro>', 'html.parser')
soup.find_all('ac:parameter')[0]['ac:name'] = 'title'       # Modify namespaced attribute
soup.find_all('ac:parameter')[0].string = 'Hello World!'    # Modify namespaced value
```

## Usage:
1. Built container with patched BeautifulSoup
```bash
docker build -t confluence .
```

2. Add your page constructor inside confluence.py using example above

3. Run following command:
```bash
docker run --rm -it confluence python3 confluence.py --endpoint 'CONFLUENCE_ENDPOINT' --page-id 'CONFLUENCE_PAGE_ID' --username 'USERNAME' --password 'PASSWORD'
```

