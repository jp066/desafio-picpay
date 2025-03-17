# PicPay Simplificado - API RESTful

Este projeto é uma API RESTful que simula um sistema simplificado de pagamentos inspirado no PicPay. Desenvolvido com **Python e Django**, o sistema permite transações financeiras entre usuários e lojistas com regras de negócio específicas e tratamento adequado de erros.

## 🚀 Funcionalidades
- 📌 **Cadastro de Usuários e Lojistas:**
  - Nome completo, CPF (ou CNPJ para lojistas), e-mail e senha únicos.
  - Cada usuário possui uma carteira associada.

- 💰 **Transferências de Dinheiro:**
  - Usuários podem enviar dinheiro para lojistas e outros usuários.
  - Lojistas apenas recebem transferências.
  - Validação de saldo antes de realizar a transferência.

- 🔍 **Serviço Autorizador Externo:**
  - Consulta via API externa para autorização de transferência (`GET https://util.devi.tools/api/v2/authorize`).

- 🔄 **Transações Seguras:**
  - Implementação de rollback caso ocorra algum problema durante a transferência.

- ✉️ **Envio de Notificações:**
  - Notificação enviada via API externa após transferências bem-sucedidas (`POST https://util.devi.tools/api/v1/notify`).
  - Tratamento de possíveis indisponibilidades do serviço externo.

- 📂 **Arquitetura Limpa e Organizada:**
  - Aplicação do padrão de projetos Service Layer e Repository.
  - Separação adequada de responsabilidades.

- 🐳 **Docker:**
  - Configuração Docker para fácil deploy e execução do projeto.

## 📦 Tecnologias Utilizadas
- **Python 3.10+**
- **Django 4.x**
- **SQLite / PostgreSQL** (Escolha de acordo com o ambiente)
- **Requests (para chamadas externas)**

## 🔧 Instalação e Execução
1. Clone o repositório:
```bash
    git clone https://github.com/seuusuario/picpay-simplificado.git
```

2. Acesse o diretório do projeto:
```bash
    cd picpay-simplificado
```

3. Crie e ative um ambiente virtual:
```bash
    python -m venv env
    source env/bin/activate  # Linux/Mac
    .\env\Scripts\activate  # Windows
```

4. Instale as dependências:
```bash
    pip install -r requirements.txt
```

5. Execute as migrações do banco de dados:
```bash
    python manage.py migrate
```

6. Inicie o servidor de desenvolvimento:
```bash
    python manage.py runserver
```

### 🐳 Usando Docker
```bash
    docker-compose up --build
```

## 📮 Endpoints Principais
- `POST /transfer/`
```json
{
  "value": 100.0,
  "payer": 4,
  "payee": 15
}
```
- `GET /authorize/` (Consulta externa para autorização)
- `POST /notify/` (Envio de notificação após transferência)

## ✅ Testes
- Para rodar os testes, utilize:
```bash
    python manage.py test
```

## 📌 Melhorias Futuras
- Implementar autenticação JWT para segurança.
- Melhorar tratamento de erros e logs.
- Criar testes mais robustos (unitários e de integração).
- Implementar caching para melhorar a performance.

## 📜 Licença
Este projeto é apenas para fins educativos e não deve ser usado comercialmente.
