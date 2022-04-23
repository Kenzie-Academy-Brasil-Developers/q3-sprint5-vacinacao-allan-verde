<h1 align="center">
  API - Vacinação
</h1>

<p align = "center">
Este é o backend da aplicação Autenticação e Autorização - O objetivo dessa aplicação é que o usuário consiga se cadastrar, fazer login, alterar dados e deletar dados com algumas rotas privada.
</p>

[Link da api](https://vacinacao-allan.herokuapp.com)

### Criação de vacina
`POST /vaccinations - FORMATO DA REQUISIÇÃO`
```json
{
  "cpf": "12312312300",
  "name": "    kenZiNHO   jUniOR ",
  "vaccine_name": "  pFIZER ",
  "health_unit_name": "  SAnTa     rItA   "
}
```
#### Caso dê tudo certo, a resposta será assim:
`POST /vaccinations - FORMATO DA RESPOSTA - STATUS 201`
```json
{
  "cpf": "12312312300",
  "first_shot_date": "Sat, 20 Apr 2022 00:00:00 GMT",
  "health_unit_name": "Santa Rita",
  "name": "Kenzinho Junior",
  "second_shot_date": "Fri, 22 Jul 2022 00:00:00 GMT",
  "vaccine_name": "Pfizer"
}
```
#### Possíveis erros:
##### CPF já cadastrado.
`POST /vaccinations - FORMATO DA RESPOSTA - STATUS 400`
```json
{
  "error": "CPF já cadastrado"
}
```
##### Formato do CPF inválido.
`POST /vaccinations - FORMATO DA RESPOSTA - STATUS 400`
```json
{
  "error": "O CPF deve possuir 11 caracteres numéricos"
}
```
##### Chave a mais, a menos ou incorreta.
`POST /vaccinations - FORMATO DA RESPOSTA - STATUS 400`
```json
{
  "error": {
    "expected": [
      "health_unit_name",
      "name",
      "vaccine_name",
      "cpf"
    ],
    "received": [
      "cpsf",
      "name",
      "vaccine_name",
      "health_unit_name"
    ]
  }
}
```
##### Tipo de dado diferente de string.
`POST /vaccinations - FORMATO DA RESPOSTA - STATUS 400`
```json
{
  "error": "chave <exemplo> possui tipo diferente de string"
}
```
