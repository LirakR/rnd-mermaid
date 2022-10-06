import requests


response = requests.post(
    url="http://localhost:9000/visualize/create",
    json={
        "path": "/home/lirakr/repos/bi3-models/bi3_models/bi3_api/models.py",
        "direction": "LR",
    }
)

mermaid_content = response.json()["data"]


head = """
<head>
<meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>1Mermaid Test</title>
    <style>
        .mermaid {
            width: 3000px;
        }
    </style>
</head>
"""
body = f"""
<body>
    <div class="mermaid">
        {mermaid_content}
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/9.1.7/mermaid.min.js" integrity="sha512-1ypa9tdUrJAWv5g28Mb5x0zXaUuI4SBofKff88OGyk5D/oOd4x1IPxYHsx3K81bwBKt8NVUvGgw7TgNZ6PJX2A==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
</body>
"""

html = f"<html>{head}{body}</html>"


with open("./test.html", "w") as f:
    f.write(html)
