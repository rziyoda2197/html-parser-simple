from html.parser import HTMLParser

class Muharrir(HTMLParser):
    def __init__(self):
        super().__init__()
        self.matnlar = []

    def handle_starttag(self, tag, attrs):
        self.matnlar.append(tag)

    def handle_data(self, data):
        self.matnlar.append(data)

    def chop(self, html):
        self.feed(html)
        return self.matnlar

html = "<html><body><h1>Hello, World!</h1><p>This is a paragraph.</p></body></html>"
muharrir = Muharrir()
print(muharrir.chop(html))
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. Kodni yuklab oling va Python ni o'rnatib oling.
2. Kodni yuklab oling va Python ni o'rnatib oling.
3. Kodni yuklab oling va Python ni o'rnatib oling.

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. Kodni yuklab oling va Python ni o'rnatib oling.
2. Kodni yuklab oling va Python ni o'rnatib oling.
3. Kodni yuklab oling va Python ni o'rnatib oling.
