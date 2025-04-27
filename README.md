
# API de Conversão de Moeda 💰

Esta API fornece funcionalidades para converter valores entre diferentes moedas, obter taxas de câmbio atuais e listar as moedas suportadas.

## Endpoints 🚀

### 1. **Conversão de Moeda** 🔄

- **URL**: `/convert`
- **Método**: `GET`
- **Parâmetros**:
  - `from`: A moeda de origem (ex: USD).
  - `to`: A moeda de destino (ex: BRL).
  - `amount`: O valor a ser convertido.
  
- **Exemplo de requisição**:

```http
GET /convert?from=USD&to=BRL&amount=100
```

- **Resposta**:

```json
{
  "from": "USD",
  "to": "BRL",
  "amount": 100,
  "converted_amount": 568.28,
  "rate": 5.6828
}
```

### 2. **Taxa de Câmbio Atual** 💱

- **URL**: `/rate`
- **Método**: `GET`
- **Parâmetros**:
  - `from`: A moeda de origem (ex: USD).
  - `to`: A moeda de destino (ex: BRL).

- **Exemplo de requisição**:

```http
GET /rate?from=USD&to=BRL
```

- **Resposta**:

```json
{
  "from": "USD",
  "to": "BRL",
  "rate": 5.6828
}
```

### 3. **Listagem de Moedas Suportadas** 🌍

- **URL**: `/currencies`
- **Método**: `GET`

- **Exemplo de requisição**:

```http
GET /currencies
```

- **Resposta**:

```json
{
  "currencies": [
    "USD", "EUR", "BRL", "JPY", "GBP", "AUD", "CAD", "INR", "CNY", "MXN", "SAR", ...
  ]
}
```

## Como Rodar 🖥️

### Pré-requisitos

- Python 3.x
- Biblioteca `Flask`
- Biblioteca `requests`

### Instalação 🔧

1. Clone este repositório:

```bash
git clone https://github.com/CauanNeves/API-Currency-Converter
cd API-Currency-Converter
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Crie uma conta na [ExchangeRate-API](https://www.exchangerate-api.com/) e obtenha a chave da API.

4. Defina a chave da API no código (em `app.py`):

```python
API_KEY = 'SUA_CHAVE_DE_API_AQUI'
```

5. Rode a aplicação:

```bash
python app.py
```

A API estará disponível em `http://localhost:5000`.

## Testes 🧪

Você pode testar a API diretamente no seu navegador ou usando ferramentas como o [Postman](https://www.postman.com/) ou `curl`.

### Exemplo de uso com `curl`:

```bash
curl "http://localhost:5000/convert?from=USD&to=BRL&amount=100"
```

## Contribuições 🤝

Sinta-se à vontade para contribuir! Para isso, basta fazer um fork deste repositório e abrir um pull request.
