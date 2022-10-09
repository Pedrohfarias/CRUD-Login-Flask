# CRUD e Login Com Flask

## Sobre o projeto
https://loginecrudflaskapp.herokuapp.com/

Essa é uma API Restful, que resumidamente gerencia usuários e seus logins/logouts, onde existem rotas para 
o realizar operações dos usuários (CRUD) além de rotas para Login e Logout dos usuários

## Tecnologias utilizadas

- Python
- Flask
- SQLAlchemy
- Hash
- JWT
- Postgresql
- Heroku


## Documentação da API

#### Get all users

```http
  GET /usuarios
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `None` | `None` | Retorna todos os usuários do banco |

#### Get user

```http
  GET /usuarios/${username}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `username`      | `string` | **Obrigatório**. O Username de um usuário |

#### Create user

```http
  POST /cadastro
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `None`      | `None` | **Payload:** {"nome":"exemp","login":"exemp ","senha":"exemp","admin":true} |


#### Delete user

```http
  DELETE /usuarios/${username}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `username`  | `string` | **Obrigatório**. O Username de um usuário e Token JWT do Login |

#### Update user

```http
  PUT /usuarios/${username}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `username`  | `string` | **Payload:** {"nome":"exemp","senha":"exemp","admin":true} |

#### Login

```http
  POST /login
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `None`  | `None` | **Payload:** {"login":"exemp","senha":"exemp"} |

#### Logout

```http
  POST /logout
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `None`  | `None` | **Obrigatório**. Informar o Token JWT. |


# Autor
Pedro Farias <br/>
Email: pedrofariasuepb@gmail.com <br/>
Linkedin: https://br.linkedin.com/in/pedro-farias-a2a142194?trk=public_profile_browsemap
