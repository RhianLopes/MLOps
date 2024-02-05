# MLOps: Machile Learning e APIs

Construção de uma API python com Flask com dois endpoints de inferência de analise de sentimento de uma frase positiva ou negativa com textblob e um modelo serializado de preco de casas a partir de uma base do kaggle.

Executando a API:
```
python main.py
```

Requisições local para inferência com a API:

```
curl --location 'http://localhost:5000/sentiment/Python é legal' \
--header 'Authorization: Basic ZXhhbXBsZTpleGFtcGxl'
```

```
curl --location 'http://localhost:5000/quotation/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic ZXhhbXBsZTpleGFtcGxl' \
--data '{
    "size": 120,
    "year": 2001,
    "parking": 2
}'
```