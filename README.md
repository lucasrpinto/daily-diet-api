# 🥗 Daily Diet API

API REST em Python com Flask para controle de dietas alimentares.

---

## 🚀 Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [MySQL](https://www.mysql.com/)
- [Docker](https://www.docker.com/) (recomendado para o banco)

---

## 📦 Funcionalidades

- **Criar dieta**: `POST /diet`
- **Listar todas as dietas**: `GET /diets`
- **Buscar uma dieta por ID**: `GET /diet/<id>`
- **Atualizar dieta**: `PUT /diet/<id>`
- **Deletar dieta**: `DELETE /diet/<id>`

---

## 📄 Exemplo de JSON para criação/atualização

```json
{
  "name": "Café da manhã leve",
  "description": "Iogurte com frutas e granola",
  "diet": true
}
```

> O campo `diet` é opcional no `POST` e será `true` por padrão se não enviado.

---

## ⚙️ Configuração do ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/daily-diet-api.git
   ```

2. Crie um ambiente virtual e ative:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados MySQL (pode usar Docker):

   ```yaml
   # Exemplo docker-compose.yml
   services:
     db:
       image: mysql:latest
       environment:
         MYSQL_ROOT_PASSWORD: admin
         MYSQL_DATABASE: dayly_diet
         MYSQL_USER: admin
         MYSQL_PASSWORD: admin
       ports:
         - "3306:3306"
   ```

5. Rode a aplicação:

   ```bash
   flask --app app run
   ```

---

## 🧪 Testando a API

Você pode testar com ferramentas como:
- [Insomnia](https://insomnia.rest/)
- [Postman](https://www.postman.com/)

Ou até mesmo com `curl` via terminal.

---

## 📌 Observações

- A API retorna todas as dietas cadastradas com `GET /diets`
- A data é gerada automaticamente no momento da criação
- O campo `diet` é um booleano que representa se a refeição está dentro da dieta

---

## 📄 Licença

Esse projeto é livre para uso pessoal e educacional.